checkpoint_folder = './checkpoint'
log_folder = './log'
embedding_dim = 256
encoder_hidden_dim = 256
decoder_hidden_dim = 256
max_question_len = 50
NULL = '--NULL--'
OOV = '--OOV--'
SOS = '--SOS--'
EOS = '--EOS--'
NULL_ID = 0
OOV_ID = 1
SOS_ID = 2
EOS_ID = 3
keep_prob = 0.8
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
answer_vocab_size = 100000
question_vocab_size = 38800
beam_width = 10
num_encoder_rnn_layers = 4
num_encoder_residual_layers = 2
num_decoder_rnn_layers = 2
num_decoder_residual_layers = 1