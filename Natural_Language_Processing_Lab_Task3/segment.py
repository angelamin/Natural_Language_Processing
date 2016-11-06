import sys
import codecs


def segmenter(corpus_file, outputSegment_file):
    input_data = codecs.open(corpus_file, 'r', 'utf-8')
    output_data = codecs.open(outputSegment_file, 'w', 'utf-8')
    for line in input_data.readlines():
        word_list = line.strip().split()
        for word in word_list:
            for w in word:
                if w != '/':
                    output_data.write(w + "\n")
                else:
                    break
    input_data.close()
    output_data.close()


# def generateWords(outputSegment_file, outputWords_file):
#     input_data = codecs.open(outputSegment_file, 'r', 'utf-8')
#     output_data= codecs.open(outputWords_file, 'r+', 'utf-8')
#     for segw in input_data.readlines():
#         for word in output_data.readlines():
#             if segw == word:
#                 break
#             else:
#                 outputWords_file.write(segw + "\n")


if __name__ == '__main__':
    print "please input the corpus file, segment output file"
    corpus_file = sys.argv[1]
    outputSegment_file = sys.argv[2]
    outputWords_file = sys.argv[3]
    segmenter(corpus_file, outputSegment_file)
    # generateWords(outputSegment_file, outputWords_file)