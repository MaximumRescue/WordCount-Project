
# return the character number of a file
def char_num(filename):
    # open the file with the name 'filename'
    f = open(filename, 'r')
    totalstr = f.read()
    return filename + ', 字符数：' + str(len(totalstr))

# return the word number of a file
def word_num(filename):
    # open the file with the name 'filename'
    f = open(filename, 'r')
    totalstr = f.read()
    # count the number of words
    count = 0
    for c in totalstr:
        if c == "," or c == " " or c == '\n':
            count = count + 1
    return filename + ', 单词数：' + str(count + 1)

# return the line number of a file
def line_num(filename):
    # open the file with the name 'filename'
    f = open(filename, 'r')
    lines = f.readlines()
    return filename + ', 行数：' + str(len(lines))

# write the information to the file
def write_file(info):
    f = open("result.txt", 'w')
    f.write(info)