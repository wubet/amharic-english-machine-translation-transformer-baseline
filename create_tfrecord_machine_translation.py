"""Convert parallel corpus (raw text files) into TFRecord files for training
machine translation models.

The parallel corpus should be text files (of unicode characters) s1.txt, t1.txt,
s2.txt, t2.txt, ... where s{i}.txt and t{i}.txt should have the same number of
lines.
"""
import itertools
import os

import tensorflow as tf
from absl import app
from absl import flags

import tokenization
from utils import dict_to_example


FLAGS = flags.FLAGS

flags.DEFINE_list(
    'source_filenames', None, 'Names of files storing source language '
        'sequences.')
flags.DEFINE_list(
    'target_filenames', None, 'Names of files storing target language '
        'sequences.')
flags.DEFINE_float(
    'file_char_limit', 1e6, 'Number of chars to read from each text file.')
flags.DEFINE_integer(
    'target_vocab_size', 32768, 'The desired vocabulary size. Ignored if '
        '`min_count` is not None.')
flags.DEFINE_integer(
    'threshold', 327, 'If the difference between actual vocab size and '
        '`target_vocab_size` is smaller than this, the binary search '
        'terminates. Ignored if `min_count` is not None.')
flags.DEFINE_integer(
    'min_count', 6, 'The minimum count required for a subtoken to be '
        'included in the vocabulary.')
flags.DEFINE_string(
    'vocab_name', 'vocab', 'Vocabulary will be stored in two files: '
        '"vocab.subtokens", "vocab.alphabet"')
flags.DEFINE_integer(
    'total_shards', 100, 'Total number of shards of the dataset (number of the '
        'generated TFRecord files)')
flags.DEFINE_string(
    'output_dir', None, 'Path to the directory that the generated TFRecord '
        'files will be written to')
flags.DEFINE_bool(
    'use_exist_vocab', False, 'Whether to create subtokenizer from existing '
        ' vocabualry. Defaults to False.')
flags.DEFINE_bool(
    'add_eos', True, 'Whether to add special token EOS to the end of the list'
        ' of token ids for each line.')

def main(_):
  source_filenames = FLAGS.source_filenames
  target_filenames = FLAGS.target_filenames
  file_char_limit = FLAGS.file_char_limit
  target_vocab_size = FLAGS.target_vocab_size
  threshold = FLAGS.threshold
  min_count = FLAGS.min_count
  vocab_name = FLAGS.vocab_name
  total_shards = FLAGS.total_shards
  output_dir = FLAGS.output_dir
  use_exist_vocab = FLAGS.use_exist_vocab
  add_eos = FLAGS.add_eos

  base_path = os.path.abspath(os.getcwd())
  parent_directory = os.path.dirname(base_path)
  vocab_name = os.path.join(parent_directory, vocab_name)
  output_dir = os.path.join(parent_directory, output_dir)
  source_filenames = [os.path.join(parent_directory, filename) for filename in source_filenames]
  target_filenames = [os.path.join(parent_directory, filename) for filename in target_filenames]
  train_files_flat = source_filenames + target_filenames

  isExist = os.path.exists(vocab_name)
  if not isExist:
      os.makedirs(vocab_name)

  isExist = os.path.exists(output_dir)
  if not isExist:
      os.makedirs(output_dir)

  if use_exist_vocab:
    print('Resotre subtokenizer from existing vocab: %s...' % vocab_name)
    subtokenizer = tokenization.restore_subtokenizer_from_vocab_files(
        vocab_name)
  else:
    print('Create fresh subtokenizer from raw text files...')
    subtokenizer = tokenization.create_subtokenizer_from_raw_text_files(
        train_files_flat,
        target_vocab_size,
        threshold,
        min_count=min_count,
        file_char_limit=file_char_limit)
    subtokenizer.save_to_file(os.path.join(vocab_name, "vocab"))

  source_files = [tf.io.gfile.GFile(fn) for fn in source_filenames]
  target_files = [tf.io.gfile.GFile(fn) for fn in target_filenames]

  source_data = itertools.chain(*source_files)
  target_data = itertools.chain(*target_files)

  filepaths = [os.path.join(output_dir, '%05d-of-%05d.tfrecord' %
      (i + 1, total_shards)) for i in range(total_shards)]

  writers = [tf.io.TFRecordWriter(fn) for fn in filepaths]
  shard = 0

  for counter, (source_line, target_line) in enumerate(zip(
      source_data, target_data)):
    source_line = source_line.strip()
    target_line = target_line.strip()
    if counter > 0 and counter % 1e5 == 0:
      print('Number of examples saved: %d.' % counter)

    example = dict_to_example(
        {'source': subtokenizer.encode(source_line, add_eos=add_eos),
         'target': subtokenizer.encode(target_line, add_eos=add_eos)})
    writers[shard].write(example.SerializeToString())
    shard = (shard + 1) % total_shards

  for writer in writers:
    writer.close()


if __name__ == '__main__':
  flags.mark_flag_as_required('source_filenames')
  flags.mark_flag_as_required('target_filenames')
  flags.mark_flag_as_required('output_dir')

  app.run(main)
