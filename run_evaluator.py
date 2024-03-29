"""Translates source sequences into target sequences, and optionally evaluates
BLEU score if groundtruth target sequences are provided.
"""
import os
from datetime import date
import pandas as pd
import tensorflow as tf
from absl import app
from absl import flags

from commons import tokenization
from model import TransformerModel
from model_runners import SequenceTransducerEvaluator

flags.DEFINE_integer(
    'encoder_stack_size', 6, 'Num of layers in encoder stack.')
flags.DEFINE_integer(
    'decoder_stack_size', 6, 'Num of layers in decoder stack.')
flags.DEFINE_integer(
    'hidden_size', 768, 'The dimensionality of the embedding vector.')
flags.DEFINE_integer(
    'num_heads', 8, 'Num of attention heads.')
flags.DEFINE_integer(
    'filter_size', 2048, 'The depth of the intermediate dense layer of the'
                         'feed-forward sublayer.')
flags.DEFINE_float(
    'dropout_rate', 0.1, 'Dropout rate for the Dropout layers.')
flags.DEFINE_integer(
    'extra_decode_length', 50, 'The max decode length would be'
                               ' the sum of `tgt_seq_len` and `extra_decode_length`.')
flags.DEFINE_integer(
    'beam_width', 4, 'Beam width for beam search.')
flags.DEFINE_float(
    'alpha', 0.6, 'The parameter for length normalization used in beam search.')
flags.DEFINE_integer(
    'decode_batch_size', 32, 'Number of sequences in a batch for inference.')
flags.DEFINE_integer(
    'src_max_length', 100, 'The number of tokens that source sequences will be '
                           'truncated or zero-padded to in inference mode.')

flags.DEFINE_string(
    'vocab_path', None, 'Path to the vocabulary file.')
flags.DEFINE_string(
    'source_text_filename', None, 'Path to the source text sequences to be '
                                  'translated.')
flags.DEFINE_string(
    'target_text_filename', None, 'Path to the target (reference) text '
                                  'sequences that the translation will be checked against,')
flags.DEFINE_string(
    'translation_output_filename', 'translations.txt', 'Path to the output '
                                                       'file that the translations will be written to.')
flags.DEFINE_string(
    'model_dir', None, 'Path to the directory that checkpoint files will be '
                       'written to.')
flags.DEFINE_string(
    'is_target_language_amharic', 'False', 'boolean value '
                                           'the target language is Amharic or not.')

FLAGS = flags.FLAGS


def main(_):
    vocab_path = FLAGS.vocab_path
    model_dir = FLAGS.model_dir

    encoder_stack_size = FLAGS.encoder_stack_size
    decoder_stack_size = FLAGS.decoder_stack_size
    hidden_size = FLAGS.hidden_size
    num_heads = FLAGS.num_heads
    filter_size = FLAGS.filter_size
    dropout_rate = FLAGS.dropout_rate

    extra_decode_length = FLAGS.extra_decode_length
    beam_width = FLAGS.beam_width
    alpha = FLAGS.alpha
    decode_batch_size = FLAGS.decode_batch_size
    src_max_length = FLAGS.src_max_length

    source_text_filename = FLAGS.source_text_filename
    target_text_filename = FLAGS.target_text_filename
    translation_output_filename = FLAGS.translation_output_filename
    is_target_language_amharic = bool(FLAGS.is_target_language_amharic)

    # Get the current working directory
    current_dir = os.getcwd()

    # transformer model
    subtokenizer = tokenization.restore_subtokenizer_from_vocab_files(vocab_path)
    vocab_size = subtokenizer.vocab_size
    model = TransformerModel(vocab_size=vocab_size,
                             encoder_stack_size=encoder_stack_size,
                             decoder_stack_size=decoder_stack_size,
                             hidden_size=hidden_size,
                             num_heads=num_heads,
                             filter_size=filter_size,
                             dropout_rate=dropout_rate,
                             extra_decode_length=extra_decode_length,
                             beam_width=beam_width,
                             alpha=alpha)

    ckpt = tf.train.Checkpoint(model=model)
    latest_ckpt = tf.train.latest_checkpoint(model_dir)
    if latest_ckpt is None:
        raise ValueError('No checkpoint is found in %s' % model_dir)
    print('Loaded latest checkpoint ', latest_ckpt)
    ckpt.restore(latest_ckpt).expect_partial()

    # build evaluator
    evaluator = SequenceTransducerEvaluator(
        model, subtokenizer, decode_batch_size, src_max_length)

    # translates input sequences, and optionally evaluates BLEU score if
    # groundtruth target sequences are provided
    if target_text_filename is not None:
        case_insensitive_score, case_sensitive_score = evaluator.evaluate(
            source_text_filename, target_text_filename, translation_output_filename)
        today = date.today()
        data = {'Model_Name': ['Transformer'],
                'Case_sensitive_BLUE_score': [case_sensitive_score],
                'Case_insensitive_BLUE_score': [case_insensitive_score],
                'Date': [today]
                }
        evaluation_file_path = os.path.join(current_dir, "tf-transformer/output/BLUE_evaluation.csv")

        df = pd.DataFrame(data)
        if os.path.exists(evaluation_file_path):
            df.to_csv(evaluation_file_path, mode='a', header=False)
        else:
            df.to_csv(evaluation_file_path, index=False, header=True)

        print('BLEU(case insensitive): %f' % case_insensitive_score)
        print('BLEU(case sensitive): %f' % case_sensitive_score)
    else:
        evaluator.translate(
            source_text_filename, is_target_language_amharic, translation_output_filename)
        print('Inference mode: no groundtruth translations.\nTranslations written '
              'to file "%s"' % translation_output_filename)


if __name__ == '__main__':
    flags.mark_flag_as_required('source_text_filename')
    flags.mark_flag_as_required('model_dir')
    flags.mark_flag_as_required('vocab_path')
    app.run(main)
