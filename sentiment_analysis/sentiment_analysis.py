import sys
import pathlib
import os
from ibm_watson import ToneAnalyzerV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

api_key = '<api_key>'
start_line_number = 784300
failed_iteration =  1868

authenticator = IAMAuthenticator(api_key)
tone_analyzer = ToneAnalyzerV3(version="2019-11-24",authenticator=authenticator)
tone_analyzer.set_service_url('https://gateway.watsonplatform.net/tone-analyzer/api')

f1 = open("anger.txt", "a+")
f2 = open("fear.txt", "a+")
f3 = open("joy.txt", "a+")
f4 = open("sadness.txt", "a+")
logger = open("logger.txt","a+")

#------------Log in date and time ----------------_#
from datetime import date
today = date.today()
d3 = today.strftime("%m/%d/%y")
logger.write("============================================================" + "\n")
logger.write("Execution start date and time =" + str(today) + str (d3) + "\n")
logger.write("============================================================" + "\n")

def classify(s1,iteration):
    #print("length of list is ", len(s1))

    quotient = int(len(s1) / 100)

    for i in range(quotient):
        lb = i * 100
        ub = 100 * (i + 1)
        s1 = s1[lb:ub]
        s = ''.join(s1)
        s = s.replace("\n",'')

        try:
            response = tone_analyzer.tone(s, sentences=True)
            result = response.get_result()

            for sentence in result['sentences_tone']:

                sentence_text = sentence['text']
                main_tone = sorted(sentence['tones'], key=lambda i: i['score'], reverse=True)

                if (len(main_tone) > 0):
                    if main_tone[0]['tone_id'] == "anger":
                        f1.write(sentence_text + "\n")
                    elif main_tone[0]['tone_id'] == "fear":
                        f2.write(sentence_text + "\n")
                    elif main_tone[0]['tone_id'] == "joy":
                        f3.write(sentence_text + "\n")
                    elif main_tone[0]['tone_id'] == "sadness":
                        f4.write(sentence_text + "\n")

        except Exception as ex:
            logger.write("Exception" + str(ex) + '\n')
            return False
    return True
            #print(ex)
    #p = pathlib.Path(f)
    #p.unlink()

def main():
    f_in = open("./output/data/big_scene_file.txt")
    sentences = []
    count = 0;
    iteration = 1

    curr_line_number = 0

    for line in f_in.readlines():
        curr_line_number = curr_line_number + 1
        if curr_line_number >= start_line_number :
            sentences.append(line)
            count = count + 1
            if(count == 100):
                if(iteration >= failed_iteration):
                    ret = classify(sentences,iteration)
                    if(ret == False):
                        logger.write("Started line" + str(start_line_number) + '\n')
                        logger.write("Failed at iteration" + str(iteration) + '\n')
                        break;
                    logger.write("done iteration" + str(iteration) + "\n")
                sentences = []
                count = 0
                iteration = iteration + 1
    f_in.close()

main()
f1.close()
f2.close()
f3.close()
f4.close()
today = date.today()
d3 = today.strftime("%m/%d/%y")
logger.write("============================================================" + "\n")
logger.write("Execution end date and time =" + str(today) + str (d3) + "\n")
logger.write("============================================================" + "\n")
logger.close()
