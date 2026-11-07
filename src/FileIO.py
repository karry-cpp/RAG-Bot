import pathlib
from collections import defaultdict

class FileIO:
    
    def __init__(self, pth: str | pathlib.Path | None = None):
        self.__file_dict: defaultdict[str, set[str]] = defaultdict(set)

        if pth != None:
            self.root = pth
        else:
            self.root = ''


    def get_files_dict(self, recur: bool = False, pth: str | pathlib.Path | None = None):
        if (pth == None) and self.root == None:
            raise Exception('Path not set')

        if pth == None:
            pth = self.root

        files = []

        if recur == True:
            files = pathlib.Path(pth).rglob('*')
        else:
            files = pathlib.Path(pth).glob('*')

        for file in files:
            self.__file_dict[file.suffix].add(str(file))

        return self.__file_dict
    

    def get_files_ext(self, ext: str, recursive: bool = False, dir: str | pathlib.Path | None = None):
        if pathlib.Path(ext).is_file():
            return set([ext])
        elif (pathlib.Path(self.root) / ext).is_file():
            return set([str(pathlib.Path(self.root) / ext)])
        
        if ext in self.__file_dict:
            return self.__file_dict[ext]

        if dir != None:
            if not pathlib.Path(dir).is_dir():
                fin = pathlib.Path(self.root) / dir
                if not pathlib.Path(fin).is_dir():
                    raise Exception(f'Invalid path for function {self.get_files_ext.__name__} : {dir}')
                else:
                    dir = pathlib.Path(self.root) / dir
        else:
            dir = self.root

        
        files = []
        if recursive == True:
            files = pathlib.Path(dir).rglob(f'*{ext}')

            self.__file_dict[ext].update([str(x) for x in files])
            return self.__file_dict[ext]
        else:
            files = pathlib.Path(dir).glob(f'*{ext}')

        return set([str(x) for x in files])


if __name__ == '__main__':
    ...
    
