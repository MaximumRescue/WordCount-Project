from FileInfo import FileInfo
from os import listdir
from os.path import isfile, join
# A class used to deal with the directory
class DirInfo:
    def __init__(self, pathname):
        self.path = pathname
    
    # build up the file list in this directory
    def build_filelist(self):
        # get all files and directories from the path
        all_list = listdir(self.path)
        # get a file instead of a directory
        files = []
        for file in all_list:
            if isfile(join(self.path, file)):
                files.append(file)
        return files
    
    # build up the information list from the file list
    def build_infolist(self):
        filenames = self.build_filelist()
        # get information by creating a FileInfo object
        infos = []
        for fname in filenames:
            info = FileInfo(fname)
            infos.append(info)
        return infos