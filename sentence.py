import sentencepiece as spm


input_file = 'data/train_tokenizer.txt'
vocab_size = 32000
model_name = 'subword_tokenizer_kor'
model_type = 'bpe'
user_defined_symbols = '[PAD],[UNK],[CLS],[SEP],[MASK],[UNK1],[UNK2],[UNK3],[UNK4],[UNK5]'

input_argument = '--input=%s --model_prefix=%s --vocab_size=%s --user_defined_symbols=%s --model_type=%s'
cmd = input_argument%(input_file, model_name, vocab_size,user_defined_symbols, model_type)

spm.SentencePieceTrainer.Train(cmd)

sp = spm.SentencePieceProcessor()
sp.Load("m.model")