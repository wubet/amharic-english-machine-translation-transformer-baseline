# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import os

from absl import flags
from os import path
from transliteration import ethiopic2latin
from absl import app

# coding:gbk

FLAGS = flags.FLAGS

flags.DEFINE_list(
    'original_filenames', None, 'Names of files storing original language '
                                'sequences.')
flags.DEFINE_list(
    'transliterate_filenames', None, 'Names of files storing language transliteration'
                                     'sequences.')


def transliterate_text(original_file_path, transliterate_file_path):
    txt = ''
    with open(original_file_path, encoding="utf8") as original_file:
        with open(transliterate_file_path, "w", encoding="utf8") as transliterate_file:
            # Read original file
            amh_lines = original_file.readlines()
            # Write to transliteration file
            for i in range(len(amh_lines)):
                line = amh_lines[i]
                if len(line) > 2:
                    line = ethiopic2latin(line)
                    transliterate_file.write(line)
        transliterate_file.close();
    original_file.close();


def main(_):
    original_filenames = FLAGS.original_filenames
    transliterate_filenames = FLAGS.transliterate_filenames

    base_path = os.path.abspath(os.getcwd())

    original_file_path = base_path + '/' + original_filenames[0]
    transliterate_file_path = base_path + '/' + transliterate_filenames[0]

    if not path.exists(transliterate_file_path) or os.path.getsize(transliterate_file_path) == 0:
        if path.exists(transliterate_file_path):
            f = open(transliterate_file_path, 'r+')
            f.truncate(0);
            f.close();
        transliterate_text(original_file_path, transliterate_file_path)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    flags.mark_flag_as_required('original_filenames');
    flags.mark_flag_as_required('transliterate_filenames');
    app.run(main);


