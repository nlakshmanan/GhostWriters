import gpt_2_simple as gpt2
from datetime import datetime

gpt2.download_gpt2(model_name="124M")
file_name = "./../data/sadness.txt"

#fine_tune
sess = gpt2.start_tf_sess()
gpt2.finetune(sess,
              dataset=file_name,
              model_name='124M',
              steps=1000,
              restore_from='fresh',
              run_name='sadness1',
              print_every=10,
              sample_every=200,
              save_every=500
              )
gpt2.generate(sess,model_name='124M',run_name='sadness1')
