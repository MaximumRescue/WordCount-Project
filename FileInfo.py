from os.path import join
import re
# A class used to get this file's information
class FileInfo:
    def __init__(self, _path, _fname):
        self.path = _path
        self.fname = _fname
        self.filename = join(self.path, self.fname).replace('\\', '\\\\')
    
    # return the character number of a file
    def char_num(self):
        # open the file with the name 'filename'
        f = open(self.filename, 'r', encoding='utf-8')
        totalstr = f.read()
        f.close()
        return self.fname + ', 字符数：' + str(len(totalstr))

    # return the word number of a file
    def word_num(self, pre_wordlist):
        # open the file with the name 'filename'
        f = open(self.filename, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        # get the word by regex expression
        linewords = []
        for i in range(0, len(lines)):
            linewords.append(re.findall(r'[A-Za-z]{2,}', lines[i]))
        # count the number of words
        count = 0
        for lineword in linewords:
            for word in lineword:
                if word.isalpha() == False:
                    lineword.remove(word)
                elif len(word) == 1:
                    lineword.remove(word)
                elif word in pre_wordlist:
                    lineword.remove(word)
            if lineword != ['']:
                count += len(lineword)
        return self.fname + ', 单词数：' + str(count)

    # return the line number of a file
    def line_num(self):
        # open the file with the name 'filename'
        f = open(self.filename, 'r', encoding='utf-8')
        lines = f.readlines()
        f.close()
        return self.fname + ', 行数：' + str(len(lines))

    # return line details of a file
    def line_detail(self):
        # open the file with the name 'filename'
        f = open(self.filename, 'r', encoding='utf-8')
        # get all line string into a list
        lines = f.readlines()
        f.close()
        # distinguish different lines
        codelines, emptylines, commentlines = [], [], []
        for line in lines:
            tmpline = line.replace(' ', '')
            tmpline = tmpline.replace('\t', '')
            tmpline = tmpline.replace('\n', '')
            if len(tmpline) == 1 or len(tmpline) == 0:
                emptylines.append(line)
            elif tmpline.startswith('//'):
                commentlines.append(line)
            else:
                codelines.append(line)
        return self.fname + ', 代码行/空行/注释行：' + str(len(codelines)) + '/'\
                + str(len(emptylines)) + '/' + str(len(commentlines))

    # write the information to the file
    def write_file(self, filename, info):
        f = open(filename, 'a', encoding='utf-8')
        f.write(info)
        f.close()
