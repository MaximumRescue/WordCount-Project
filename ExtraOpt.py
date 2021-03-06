import sys, wx
from os.path import join, isdir, isfile, dirname

# get the correct path
def cur_file_dir():    
    path = sys.path[0]
    if isdir(path):
        return path
    elif isfile(path):
        return dirname(path)

# get the preserved words list
def get_prelist(fname):
    filename = join(cur_file_dir(), fname).replace('\\', '\\\\')
    fhandle = open(filename, 'r')
    wholestr = fhandle.read()
    prelist = wholestr.split(' ')
    for word in prelist:
        if word == "" or word == "\n" or word == "\t":
            prelist.remove(word)
    return prelist

# A method to get filename by dialog
def dialog_get():
    app = wx.App()
    frame = wx.Frame(None)
    openwildcard = "All files(*.*)|*.*|" + \
                    "C/C++ files(*.c;*.cpp;*.h)|*.c;*cpp;*.h|" + \
                    "Java source files(*.java)|*.java|" + \
                    "Python source files(*.py)|*.py|" + \
                    "Text files(*.txt)|*.txt"
    # Create open file dialog
    openFileDialog = wx.FileDialog(frame, "Choose a file to open",
                                   wildcard=openwildcard, 
                                   style=wx.FD_OPEN | wx.FD_FILE_MUST_EXIST)
    openFileDialog.ShowModal()
    dir = openFileDialog.GetDirectory()
    filename = openFileDialog.GetFilename()
    openFileDialog.Destroy()
    return dir, filename