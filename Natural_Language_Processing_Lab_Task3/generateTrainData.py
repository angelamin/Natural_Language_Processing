# coding=UTF-8
import sys
import codecs


def generateTrain(words_file, vocabulary_file, BI_file, train_file):
    words_data = codecs.open(words_file, 'r', 'utf-8')
    vocabulary_data = codecs.open(vocabulary_file, 'r', 'utf-8')
    BI_data = codecs.open(BI_file, 'r', 'utf-8')
    train_data = codecs.open(train_file, 'w', 'utf-8')
    train_list = []
    BI_list = []
    words_data_list = []
    vocabulary_data_list = []
    i = 0
    #将BI_data中的数据汉字和BI分别存在两个数组中
    for line in BI_data.readlines():
        word_list = line.strip().split()
        #需要加入train文件的汉字
        train_list.append(word_list[0])
        #对应汉字的BI
        BI_list.append(word_list[1])
    #将words_data中的数据分别存在两个数组中以便判断在数组中的位置
    for line in words_data.readlines():
        line = line.strip()
        words_data_list.append(line)
    #将vocabulary_data中的数据分别存在两个数组中以便判断在数组中的位置
    for line in vocabulary_data.readlines():
        line = line.strip()
        vocabulary_data_list.append(line)

    words_len = len(words_data_list)
    vocabulary_len = len(vocabulary_data_list) + words_len + 1
    while i < len(train_list):
        if i == 0:
            if BI_list[i] == "B":
                train_data.write('1' + '\t')
            else:
                train_data.write('0' + '\t')

            first1 = vocabulary_len*0 + words_len
            train_data.write(str(first1) + ':1' + '\t')

            first2 = vocabulary_len * 1 + words_len
            train_data.write(str(first2) + ':1' + '\t')

            first3 = vocabulary_len * 2 + words_data_list.index(train_list[i])
            train_data.write(str(first3) + ':1' + '\t')

            first4 = vocabulary_len * 3 + words_data_list.index(train_list[i + 1])
            train_data.write(str(first4) + ':1' + '\t')

            first5 = vocabulary_len * 4 + words_data_list.index(train_list[i + 2])
            train_data.write(str(first5) + ':1' + '\t')

            first6 = vocabulary_len * 5 + vocabulary_data_list.index(train_list[i]) + words_len + 1
            train_data.write(str(first6) + ':1' + '\t')

            first7 = vocabulary_len * 6 + vocabulary_data_list.index(train_list[i] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first7) + ':1' + '\t')

            first8 = vocabulary_len * 7 + vocabulary_data_list.index(train_list[i + 1]) + words_len + 1
            train_data.write(str(first8) + ':1' + '\t')

            train_data.write('\n')
        elif i == 1:
            if BI_list[i] == "B":
                train_data.write('1' + '\t')
            else:
                train_data.write('0' + '\t')
            first1 = vocabulary_len * 0 + words_len
            train_data.write(str(first1) + ':1' + '\t')

            first2 = vocabulary_len * 1 + words_data_list.index(train_list[i - 1])
            train_data.write(str(first2) + ':1' + '\t')

            first3 = vocabulary_len * 2 + words_data_list.index(train_list[i])
            train_data.write(str(first3) + ':1' + '\t')

            first4 = vocabulary_len * 3 + words_data_list.index(train_list[i + 1])
            train_data.write(str(first4) + ':1' + '\t')

            first5 = vocabulary_len * 4 + words_data_list.index(train_list[i + 2])
            train_data.write(str(first5) + ':1' + '\t')

            first6 = vocabulary_len * 5 + vocabulary_data_list.index(train_list[i - 1] + train_list[i]) + words_len + 1
            train_data.write(str(first6) + ':1' + '\t')

            first7 = vocabulary_len * 6 + vocabulary_data_list.index(train_list[i] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first7) + ':1' + '\t')

            first8 = vocabulary_len * 7 + vocabulary_data_list.index(train_list[i - 1] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first8) + ':1' + '\t')

            train_data.write('\n')
        elif (i == len(train_list) - 2):
            if BI_list[i] == "B":
                train_data.write('1' + '\t')
            else:
                train_data.write('0' + '\t')
            first1 = vocabulary_len * 0 + words_data_list.index(train_list[i - 2])
            train_data.write(str(first1) + ':1' + '\t')

            first2 = vocabulary_len * 1 + words_data_list.index(train_list[i - 1])
            train_data.write(str(first2) + ':1' + '\t')

            first3 = vocabulary_len * 2 + words_data_list.index(train_list[i])
            train_data.write(str(first3) + ':1' + '\t')

            first4 = vocabulary_len * 3 + words_data_list.index(train_list[i + 1])
            train_data.write(str(first4) + ':1' + '\t')

            first5 = vocabulary_len * 4 + words_len
            train_data.write(str(first5) + ':1' + '\t')

            first6 = vocabulary_len * 5 + vocabulary_data_list.index(train_list[i - 1] + train_list[i]) + words_len + 1
            train_data.write(str(first6) + ':1' + '\t')

            first7 = vocabulary_len * 6 + vocabulary_data_list.index(train_list[i] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first7) + ':1' + '\t')

            first8 = vocabulary_len * 7 + vocabulary_data_list.index(train_list[i - 1] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first8) + ':1' + '\t')

            train_data.write('\n')
        elif i == (len(train_list) - 1):
            if BI_list[i] == "B":
                train_data.write('1' + '\t')
            else:
                train_data.write('0' + '\t')
            first1 = vocabulary_len * 0 + words_data_list.index(train_list[i - 2])
            train_data.write(str(first1) + ':1' + '\t')

            first2 = vocabulary_len * 1 + words_data_list.index(train_list[i - 1])
            train_data.write(str(first2) + ':1' + '\t')

            first3 = vocabulary_len * 2 + words_data_list.index(train_list[i])
            train_data.write(str(first3) + ':1' + '\t')

            first4 = vocabulary_len * 3 + words_len
            train_data.write(str(first4) + ':1' + '\t')

            first5 = vocabulary_len * 4 + words_len
            train_data.write(str(first5) + ':1' + '\t')

            first6 = vocabulary_len * 5 + vocabulary_data_list.index(train_list[i - 1] + train_list[i]) + words_len + 1
            train_data.write(str(first6) + ':1' + '\t')

            first7 = vocabulary_len * 6 + vocabulary_data_list.index(train_list[i]) + words_len + 1
            train_data.write(str(first7) + ':1' + '\t')

            first8 = vocabulary_len * 7 + vocabulary_data_list.index(train_list[i - 1]) + words_len + 1
            train_data.write(str(first8) + ':1' + '\t')

            train_data.write('\n')
        else:
            if BI_list[i] == "B":
                train_data.write('1' + '\t')
            else:
                train_data.write('0' + '\t')
            first1 = vocabulary_len * 0 + words_data_list.index(train_list[i - 2])
            train_data.write(str(first1) + ':1' + '\t')

            first2 = vocabulary_len * 1 + words_data_list.index(train_list[i - 1])
            train_data.write(str(first2) + ':1' + '\t')

            first3 = vocabulary_len * 2 + words_data_list.index(train_list[i])
            train_data.write(str(first3) + ':1' + '\t')

            first4 = vocabulary_len * 3 + words_data_list.index(train_list[i + 1])
            train_data.write(str(first4) + ':1' + '\t')

            first5 = vocabulary_len * 4 + words_data_list.index(train_list[i + 2])
            train_data.write(str(first5) + ':1' + '\t')

            first6 = vocabulary_len * 5 + vocabulary_data_list.index(train_list[i - 1] + train_list[i]) + words_len + 1
            train_data.write(str(first6) + ':1' + '\t')

            first7 = vocabulary_len * 6 + vocabulary_data_list.index(train_list[i] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first7) + ':1' + '\t')

            first8 = vocabulary_len * 7 + vocabulary_data_list.index(train_list[i - 1] + train_list[i + 1]) + words_len + 1
            train_data.write(str(first8) + ':1' + '\t')

            train_data.write('\n')
        i = i + 1
if __name__ == '__main__':
    #注意：如果最后是要生成测试文件的话，一定将最后的训练数据存放在testTrain.txt，不要存错地方，因为训练文件训练一次实在太耗时！！！！
    print "please input the words_file, vocabulary_file, BI_file, train_file"
    words_file = sys.argv[1]
    vocabulary_file = sys.argv[2]
    BI_file = sys.argv[3]
    train_file = sys.argv[4]
    generateTrain(words_file, vocabulary_file, BI_file, train_file)