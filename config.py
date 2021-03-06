checkpoint_folder = './checkpoint'
log_folder = './log'
embedding_dim = 300
encoder_hidden_dim = 150
decoder_hidden_dim = 150
dot_attention_dim = 150
max_question_len = 20
NULL = '--NULL--'
OOV = '--OOV--'
SOS = '--SOS--'
EOS = '--EOS--'
NULL_ID = 0
OOV_ID = 1
SOS_ID = 2
EOS_ID = 3
keep_prob = 0.7
raw_train_file = './data/zhidao.train.json'
train_file = './generate/train.txt'
raw_dev_file = './data/zhidao.dev.json'
dev_file = './generate/dev.txt'
raw_test_file = './data/zhidao.test.json'
test_file = './generate/test.json'
question_vocab_file = './generate/vocab.question.txt'
answer_vocab_file = './generate/vocab.answer.txt'
stopwords_file = './data/stopwords.txt'
answer_limit = 400
answer_vocab_size = 50000
question_vocab_size = 10000