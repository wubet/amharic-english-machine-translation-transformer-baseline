# Amharic-English-Machine-Translation-Transformer-Baseline

clone the " 
amharic-english-machine-translation-baseline" repository.

using SSH command.

```buildoutcfg
git clone git@github.com:wubet/amharic-english-machine-translation-baseline.git
```
Or using the https command
```buildoutcfg
git clone https://github.com/wubet/amharic-english-machine-translation-baseline.git
```
Change the directory into the main repository.
```buildoutcfg
cd amharic-english-machine-translation-transformer-baseline
```
Clone the "unified-amharic-english-corpus" repository that contains Amharic-English dataset.

using SSH command.
```buildoutcfg
git clone https://github.com/wubet/unified-amharic-english-corpus.git
```

Clone the "tf-transformer
" repository that is a TensorFlow 2.x implementation of Transformer model (Attention is all you need) for Neural Machine Translation (NMT) authored by Chao ji.

using SSH command.
```buildoutcfg
git clone git@github.com:chao-ji/tf-transformer.git
```
Or using the https command
```buildoutcfg
git clone https://github.com/chao-ji/tf-transformer.git
```
Change directory to Update the submodule
```buildoutcfg
cd tf-transformer
```
Update the submodule by running
```buildoutcfg
git submodule update --init --recursive
```
Return to main directory
```buildoutcfg
cd ..
```

Execute the pre-process file
```buildoutcfg
python pre-process.py
```

We need to transliterate the Gee'z character representation into latin character representation.

For development or validation
```buildoutcfg
python tf-transformer/commons/create_transliteration.py \
  --original_filenames=tf-transformer/unified-amharic-english-corpus/datasets/dev.am-en.base.am \
  --transliterate_filenames=tf-transformer/unified-amharic-english-corpus/datasets/dev.am-en.transliteration.am \
```

For training
```buildoutcfg
python tf-transformer/commons/create_transliteration.py \
  --original_filenames=tf-transformer/unified-amharic-english-corpus/datasets/train.am-en.base.am \
  --transliterate_filenames=tf-transformer/unified-amharic-english-corpus/datasets/train.am-en.transliteration.am \
```

For testing
```buildoutcfg
python tf-transformer/commons/create_transliteration.py \
  --original_filenames=tf-transformer/unified-amharic-english-corpus/datasets/test.am-en.base.am \
  --transliterate_filenames=tf-transformer/unified-amharic-english-corpus/datasets/test.am-en.transliteration.am \
```

Convert raw text files into TFRecord files by running
```buildoutcfg
python tf-transformer/commons/create_tfrecord_machine_translation.py \
  --source_filenames=tf-transformer/unified-amharic-english-corpus/datasets/train.am-en.transliteration.am \
  --target_filenames=tf-transformer/unified-amharic-english-corpus/datasets/train.am-en.base.en \
  --output_dir=tf-transformer/tfrecord \
  --vocab_name=tf-transformer/vocab
```

In the context of machine translation, TFRecord files are a binary file format used to store parallel data in a format that is compatible with TensorFlow. Parallel data refers to a set of source and target language sentences or texts that are aligned with each other. The parallel data is typically preprocessed and tokenized before being stored in TFRecord files. 

To train a model, run
```buildoutcfg
python tf-transformer/run_trainer.py \
  --data_dir=tf-transformer/tfrecord \
  --vocab_path=tf-transformer/vocab \
  --model_dir=checkpoints \
  --source_language=Amharic \
  --target_language=English
```

A vocab file is a text file that contains the vocabulary of the source or target language. The vocabulary is a set of all the unique words or subword units that appear in the training data. The vocab files are used during the preprocessing step of machine translation to tokenize and encode the source and target language data.

To evaluate the model, run
```buildoutcfg
python tf-transformer/run_evaluator.py \
  --source_text_filename=tf-transformer/unified-amharic-english-corpus/datasets/test.am-en.transliteration.am \
  --target_text_filename=tf-transformer/unified-amharic-english-corpus/datasets/test.am-en.base.en \
  --vocab_path=tf-transformer/vocab/vocab \
  --model_dir=checkpoints 
```
The model evaluation is made using BLUE (Bilingual Evaluation Understudy) score.

To translate the source file, run
```buildoutcfg
python tf-transformer/run_evaluator.py \
  --source_text_filename=tf-transformer/unified-amharic-english-corpus/datasets/test.am-en.transliteration.am \
  --translation_output_filename=tf-transformer/unified-amharic-english-corpus/datasets/test.am-en.translated.en \
  --is_target_language_amharic=False \
  --vocab_path=tf-transformer/vocab/vocab \
  --model_dir=checkpoints 
```
The above command translate English to Amharic