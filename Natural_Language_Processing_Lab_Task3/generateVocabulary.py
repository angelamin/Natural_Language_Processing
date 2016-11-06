import sys
import codecs


def generateVocabulary(outputWords_file, outputVocabulary_file):
    input_data = codecs.open(outputWords_file, 'r', 'utf-8')
    output_data = codecs.open(outputVocabulary_file, 'w', 'utf-8')
    input_list = []
    output_list = []
    for word in input_data.readlines():
        word = word.strip()
        input_list.append(word)

    for i in input_list:
        for j in input_list:
            if i == j:
                output_list.append(i)
                output_list.append(i + i)
            else:
                output_list.append(i+j)
    for vact in output_list:
        output_data.write(vact + "\n")
    input_data.close()
    output_data.close()

if __name__ == '__main__':
    print "please input the outputWords_file, outputVocabulary_file"
    outputWords_file = sys.argv[1]
    outputVocabulary_file = sys.argv[2]
    generateVocabulary(outputWords_file, outputVocabulary_file)