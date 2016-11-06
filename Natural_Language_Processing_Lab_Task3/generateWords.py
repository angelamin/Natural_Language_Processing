import sys
import codecs


def generateWords(outputSegment_file, outputWords_file):
    input_data = codecs.open(outputSegment_file, 'r', 'utf-8')
    output_data = codecs.open(outputWords_file, 'w', 'utf-8')
    output_list = []
    for segw in input_data.readlines():
        segw = segw.strip()
        if segw not in output_list:
            output_list.append(segw)

    for word in output_list:
        if (word not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "-"]):
            output_data.write(word + "\n")

    input_data.close()
    output_data.close()


if __name__ == '__main__':
    print "please input the segment output file, words output file"
    outputSegment_file = sys.argv[1]
    outputWords_file = sys.argv[2]
    generateWords(outputSegment_file, outputWords_file)