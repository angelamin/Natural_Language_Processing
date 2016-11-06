# coding=UTF-8
import sys
import codecs


def segmenter(test_file, outputTestBI_file):
    input_data = codecs.open(test_file, 'r', 'utf-8')
    outputTestBI_data = codecs.open(outputTestBI_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            for w in word:
               outputTestBI_data.write(w + '\tB')
               outputTestBI_data.write("\n")
    input_data.close()
    outputTestBI_data.close()


if __name__ == '__main__':
    print "please input test_file, outputTestBI_file"
    test_file = sys.argv[1]
    outputTestBI_file = sys.argv[2]
    segmenter(test_file, outputTestBI_file)
