# Read line by line and output a line as sentence only if it contains a '.' and has more than one words.
import os
import errno
import re


def parse(filename):
    skip_first_10 = 1
    fp = open(filename)

    line = ' '

    data = ''
    cnt = 1
    dialogs = []
    d_start = False

    while line:
        line = fp.readline()
        if not line.strip('\n'):
            continue
        if line.strip() == "Written by":
            line = fp.readline()
            line = fp.readline()
            continue
        if line.strip(".\n").strip().isnumeric():
            continue
        if line.isupper():
            if(d_start == True):
                if(len(data) != 0):
                    skip_first_10 = skip_first_10 + 1
                    if skip_first_10 > 10 and re.search("[a-zA-Z]", data) != None:
                        data = re.sub(' +', ' ', data)
                        word_list = data.split()
                        if len(word_list) != 1:
                            if word_list[0] == word_list[-1]:
                                data = " ".join(word_list[1:-1])
                        #d_list.append(curr_char_name)
                        #d_list.append(data)
                        dialogs.append(data)
                data = ''
            d_start = True
            curr_char_name = line.strip("\n")
            continue

        # print("Line {}: {}".format(cnt, line.strip()))
        data = data + ' ' + line.strip("\n").strip()
        cnt += 1

    fp.close()



    output_file = filename.replace("input_files", "output", 1)
    if not os.path.exists(os.path.dirname(output_file)):
        try:
            os.makedirs(os.path.dirname(output_file))
        except OSError as exc:  # Guard against race condition
            if exc.errno != errno.EEXIST:
                raise

    with open(output_file, 'w') as f:
        for item in dialogs:
            f.write("%s\n" % item)

    count_sentences_file = "./output/count_dialogs.csv"
    with open(count_sentences_file, 'a') as f:
        f.write(output_file + ',' + str(len(dialogs)) + '\n')


def split_into_dialogs():
    rootdir = "./input_files/dialogs/"
    for root_1, subdirs_1, files_1 in os.walk(rootdir):
        for item in subdirs_1:
            full_path_1 = rootdir + str(item) + '/'
            # print(rootdir + str(item) + '/')
            for root_2, subdirs_2, files_2 in os.walk(full_path_1):
                for file in files_2:
                    full_path_2 = full_path_1 + str(file)
                    parse(full_path_2)


def validate_and_group_sentences():
    set_files = []

    with open("./output/count_dialogs.csv") as f:
        list2 = [row.split(',')[0] for row in f]

    f_out = open("./output/big_dialogs_file.txt", "a")

    for file in list2:
        filename = file.split('/')[-1]
        if filename in set_files:
            continue
        set_files.append(filename)
        f_in = open(file)
        for line in f_in.readlines():
            f_out.write(line)


#split_into_dialogs()
validate_and_group_sentences()

#filename = './input_files/dialogs/Adventure/lordoftheringsthetwotowers_dialog.txt'
#parse(filename)



