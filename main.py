import sys
from FileInfo import FileInfo
from DirInfo import DirInfo
from ExtraOpt import get_prelist, dialog_get
# get all valid arguments
args = sys.argv[1:]
# create a dictionary to contain all operations
fnames, indexs = [], [-1]
relation = {}
for arg in args:
    if arg[0] != '-':
        fnames.append(arg)
# determine the position of each file
for fname in fnames:
    indexs.append(args.index(fname))
    relation[fname] = []
# link the operations to the files
for i in range(0, len(indexs) - 1):
    for j in range(indexs[i] + 1, indexs[i + 1]):
        relation[fnames[i]].append(args[j])
# determine the operations on one file
outputfile, prelistfile = "", ""
for fname in fnames:
    if '-o' in relation[fname]:
        outputfile = fname
    elif '-e' in relation[fname]:
        prelistfile = fname
    else:
        desfile = fname
# use dialog to open file
if args == ['-x']:
    path, fname = dialog_get()
    onefile = FileInfo(path, fname)
    print(onefile.char_num())
    print(onefile.line_num())
    print(onefile.word_num([]))    
# dealing with the directory
elif '-s' in relation[desfile]:
    directory = DirInfo(sys.path[0])
    tmplist = desfile.split('.')
    type = '.' + tmplist[-1]
    localinfo = directory.build_infolist(type)
    for info in localinfo:
        str = ""
        if '-c' in relation[desfile]:
            print(info.char_num())
            str += info.char_num()
        if '-w' in relation[desfile]:
            print(info.word_num([]))
            str += info.word_num([])
        if '-l' in relation[desfile]:
            print(info.line_num())
            str += info.line_num()
        if '-a' in relation[desfile]:
            print(info.line_detail())
            str += info.line_detail()
        if prelistfile != "":
            # get the preserved word list
            prelist = get_prelist(prelistfile)
            print(info.word_num(prelist))
            str += info.word_num(prelist)
        if outputfile != "":
            info.write_file(outputfile, str)
else:
    thisfile = FileInfo(sys.path[0], desfile)
    thisstr = ""
    if '-c' in relation[desfile]:
        print(thisfile.char_num())
        thisstr += thisfile.char_num()
    if '-w' in relation[desfile]:
        print(thisfile.word_num([]))
        thisstr += thisfile.word_num([])
    if '-l' in relation[desfile]:
        print(thisfile.line_num())
        thisstr += thisfile.line_num()
    if '-a' in relation[desfile]:
        print(thisfile.line_detail())
        thisstr += thisfile.line_detail()
    if prelistfile != "":
        # get the preserved word list
        prelist = get_prelist(prelistfile)
        print(thisfile.word_num(prelist))
        thisstr += thisfile.word_num(prelist)
    if outputfile != "":
        thisfile.write_file(outputfile, thisstr)
