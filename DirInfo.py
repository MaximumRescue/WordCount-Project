from FileInfo import FileInfo
from os import listdir
from os.path import isfile, join
# A class used to deal with the directory
class DirInfo:
    def __init__(self, pathname):
        self.path = pathname
    
    # build up the file list in this directory
    def build_filelist(self, type=''):
        # get all files and directories from the path
        all_list = listdir(self.path)
        # get a file instead of a directory
        files = []
        for file in all_list:
            if type != '':
                if isfile(join(self.path, file)) and file.endswith(type):
                    files.append(file)
            elif isfile(join(self.path, file)):
                files.append(file)
        return files
    
    # build up the directory list in this directory
    def build_dirlist(self):
        # get all files and directories from the path
        all_list = listdir(self.path)
        # get a file instead of a directory
        dirs = []
        for file in all_list:
            if isfile(join(self.path, file)) == False:
                dirs.append(file)
        return dirs  
      
    # build up the information list from the file list
    def build_infolist(self, type=''):
        filenames = self.build_filelist(type)
        dirnames = self.build_dirlist()
        # get information by creating a FileInfo object
        infos = []
        for fname in filenames:
            info = FileInfo(self.path, fname)
            infos.append(info)
        # deal with the inner directory
        for dirname in dirnames:
            new_path = join(self.path, dirname)
            newdir = DirInfo(new_path)
            new_infos = newdir.build_infolist(type)
            infos = infos + new_infos
        return infos

# some test codes, you can ignore them
if __name__ == "__main__":
    import sys
    dirinfo = DirInfo(sys.path[0])
    for info in dirinfo.build_infolist('.txt'):
        print(info.fname)
    
