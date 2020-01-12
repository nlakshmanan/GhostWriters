import gpt_2_simple as gpt2
#import gpt_2_simple as g_anger
#import gpt_2_simple as g_joy
#import gpt_2_simple as g_sadness
#import gpt_2_simple as g_fear
from datetime import datetime
import tensorflow as tf

def choose_model(mood,text):

        ### To-do: update model names
        if mood=='anger':
            #generated_text = g_anger.generate(sess_anger,model_name='355M',run_name='anger1',length=250,temperature=0.7,prefix=text,return_as_list=True)
            with g1.as_default():
                sess1 = gpt2.start_tf_sess()
                gpt2.load_gpt2(sess1,run_name="anger1")
                generated_text = gpt2.generate(sess1,model_name='355M',run_name='anger1',length=150,temperature=0.7,prefix=text,return_as_list=True)
        elif mood=='joy':
            #generated_text = g_joy.generate(sess_joy,model_name='355M',run_name='joy1',length=250,temperature=0.7,prefix=text,return_as_list=True)
            with g2.as_default():
                sess2 = gpt2.start_tf_sess()
                gpt2.load_gpt2(sess2,run_name="joy1")
                generated_text = gpt2.generate(sess2,model_name='355M',run_name='joy1',length=150,temperature=0.7,prefix=text,return_as_list=True)
        elif mood=='sadness':
            #generated_text = g_sadness.generate(sess_sadness,model_name='355M',run_name='sadness1',length=250,temperature=0.7,prefix=text,return_as_list=True)
            with g3.as_default():
                sess3 = gpt2.start_tf_sess()
                gpt2.load_gpt2(sess3,run_name="sadness1")
                generated_text = gpt2.generate(sess3,model_name='124M',run_name='sadness1',length=150,temperature=0.7,prefix=text,return_as_list=True)
        elif mood=='fear':
            with g4.as_default():
                sess4 = gpt2.start_tf_sess()
                gpt2.load_gpt2(sess4, run_name="fear1")
                generated_text = gpt2.generate(sess4,model_name='355M',run_name='fear1',length=150,temperature=0.7,prefix=text,return_as_list=True)
            #generated_text = g_fear.generate(sess_fear,model_name='355M',run_name='fear1',length=250,temperature=0.7,prefix=text,return_as_list=True)
                #generated_text = fearBox.generate(sess, return_as_list=True)
                pass

        return generated_text


def main():
        #emotionSeries = ['joy','joy','joy','joy','anger','anger','sadness','joy','joy']
        emotionSeries= ['sadness','joy','anger','fear']
        f_in = open("input.txt")
        f_out = open("output.txt","a+")

        data = f_in.read().replace('\n','')
        #f_out.write(data)

        for i in emotionSeries:
                data = choose_model(i,data)
                data_as_string = data[0]
                data_as_list = data_as_string.split('\n')
                print("data as list length: ",len(data_as_list))
                final_string = ' '.join(data_as_list[:-2])
                next_iter = ' '.join(data_as_list[-2:])
                f_out.write(final_string)
                data = next_iter

        f_out.write("\n----- End of generation -----")
        f_in.close()
        f_out.close()

if __name__ == "__main__":
        g1 = tf.Graph()
        g2 = tf.Graph()
        g3 = tf.Graph()
        g4 = tf.Graph()
        sess1 = gpt2.start_tf_sess()
        sess2 = gpt2.start_tf_sess()
        sess3 = gpt2.start_tf_sess()
        sess4 = gpt2.start_tf_sess()
        #sess_anger = g_anger.start_tf_sess()
        #g_anger.load_gpt2(sess_anger,run_name="anger1")
        #sess_joy = g_joy.start_tf_sess()
        #g_joy.load_gpt2(sess_joy,run_name="joy1")
        #sess_sadness = g_sadness.start_tf_sess()
        #g_sadness.load_gpt2(sess_sadness,run_name="sadness1")
        ##sess_fear = g_fear.start_tf_sess()
        ##g_fear.load_gpt2(sess_fear,run_name="fear1")
        main()
