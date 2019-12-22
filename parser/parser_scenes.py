#Read line by line and output a line as sentence only if it contains a '.' and has more than one words.
import os
import errno
import pandas as pd

def parse(filename):

    #fp = open('./input_files/scenes/Action/15minutes_scene.txt', 'r')
    fp = open(filename)

    replace_strings = {".)": ")", "Ms.": "Ms\dot", "Mrs.": "Mrs\dot", "Mr.": "Mr\dot", "Dr.": "Dr\dot" }

    line = ' '

    data = ''
    cnt = 1
    while line:
       line = fp.readline()
       for key in replace_strings:
           line = line.replace(key,replace_strings[key])

       if not line.strip('\n') :
           continue
       if line.isupper():
           continue
       if line.strip() == "Written by":
           line = fp.readline()
           line = fp.readline()
           continue
       if line.strip(".\n").strip().isnumeric():
           continue;

       #print("Line {}: {}".format(cnt, line.strip()))
       data = data + ' ' + line.strip("\n").strip()
       cnt += 1

    fp.close()

    #print(data)
    sentences_temp = data.split('.')
    #if next string is empty append '.' to previous string
    sentences = []
    cnt = -1
    for item in sentences_temp:
        if item == '':
            sentences[cnt] = sentences[cnt] + '.'
        else:
            for key in replace_strings:
                item = item.replace(replace_strings[key],key)
            sentences.append(item + '.')
            cnt = cnt + 1
    sentences_temp = sentences
    sentences = []

    #If a item ends with "..." combine with the next item in sentence
    cnt = -1
    merge_next = False

    for item in sentences_temp:
        if(merge_next):
            sentences[cnt] = sentences[cnt] + ' ' + item
            merge_next  = False
        else:
            sentences.append(item)
            cnt = cnt + 1
            if "..." in sentences[cnt][-3:]:
                merge_next = True



    #print(sentences_temp)
    #print(*sentences, sep = "\n")
    output_file = filename.replace("input_files", "output", 1)
    if not os.path.exists(os.path.dirname(output_file)):
        try:
            os.makedirs(os.path.dirname(output_file))
        except OSError as exc: # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(output_file, 'w') as f:
        for item in sentences:
            f.write("%s\n" % item)

    count_sentences_file = "./output/count_sentences.csv"
    with open(count_sentences_file, 'a') as f:
        f.write(output_file + ',' + str(len(sentences)) + '\n')


def split_into_sentences():
    rootdir = "./input_files/scenes/"
    for root_1, subdirs_1, files_1 in os.walk(rootdir):
        for item in subdirs_1:
            full_path_1 = rootdir + str(item) + '/'
            #print(rootdir + str(item) + '/')
            for root_2, subdirs_2, files_2 in os.walk(full_path_1):
                for file in files_2:
                    full_path_2 = full_path_1 + str(file)
                    parse(full_path_2)

def validate_and_group_sentences():

    set_files = []

    with open("./output/count_sentences_filtered.csv") as f:
        list2 = [row.split(',')[0] for row in f]

    f_out = open("./output/big_scene_file.txt","a")

    for file in list2:
        filename = file.split('/')[-1]
        if filename in set_files:
            continue
        set_files.append(filename)
        f_in = open(file)
        for line in f_in.readlines():
            f_out.write(line)
        

validate_and_group_sentences()





