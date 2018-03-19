class FileInfo:
    def __init__(self, fname):
        self.filename = fname
    
    # return the character number of a file
    def char_num(self):
        # open the file with the name 'filename'
        f = open(self.filename, 'r')
        totalstr = f.read()
        f.close()
        return self.filename + ', 字符数：' + str(len(totalstr)) + '\n'

    # return the word number of a file
    def word_num(self):
        # open the file with the name 'filename'
        f = open(self.filename, 'r')
        totalstr = f.read()
        # count the number of words
        count = 0
        for c in totalstr:
            if c == "," or c == " " or c == '\n':
                count = count + 1
        f.close()
        return self.filename + ', 单词数：' + str(count + 1) + '\n'

    # return the line number of a file
    def line_num(self):
        # open the file with the name 'filename'
        f = open(self.filename, 'r')
        lines = f.readlines()
        f.close()
        return self.filename + ', 行数：' + str(len(lines)) + '\n'

    # write the information to the file
    def write_file(self, filename, info):
        f = open(filename, 'w')
        f.write(info)
        f.close()


