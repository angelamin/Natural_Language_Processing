# coding=UTF-8
import sys
import codecs


def segmenter(corpus_file, outputPair_file, outputBI_file):
    input_data = codecs.open(corpus_file, 'r', 'utf-8')
    output_data = codecs.open(outputPair_file, 'w', 'utf-8')
    outputBI_data = codecs.open(outputBI_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            for w in word:
                if w != '/':
                    output_data.write(w)
                else:
                    break
            output_data.write("\n")
    output_data.write("\n")
    input_data.close()
    output_data.close()

    segment_data = codecs.open(outputPair_file, 'r', 'utf-8')
    for line in segment_data.readlines():
        line = line.strip()
        if len(line) == 1:
            if (line not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]):
                outputBI_data.write(line + "\tB\n")
        else:
            if (line[0] not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]):
                outputBI_data.write(line[0] + "\tB\n")
            for w in line[1:len(line)]:
                if (w not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]):
                    outputBI_data.write(w + "\tI\n")
    segment_data.close()


if __name__ == '__main__':
    print "please input the corpus file, segment output file"
    corpus_file = sys.argv[1]
    outputPair_file = sys.argv[2]
    outputBI_file = sys.argv[3]
    segmenter(corpus_file, outputPair_file, outputBI_file)
