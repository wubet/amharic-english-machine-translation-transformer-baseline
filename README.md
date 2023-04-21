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
Clone the "tf-transformer
" repository that is a TensorFlow 2.x implementation of Transformer model (Attention is all you need) for Neural Machine Translation (NMT). Authored by Chao ji.

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
cd..
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