
import os
import shutil


def get_files():
    source = os.path.expanduser("~/Downloads/")
    files = os.listdir(source)
    for file in files:
        extension = os.path.splitext(file)[1]
        extension = extension[1:]
        try:
            os.makedirs(source + extension)
        except FileExistsError:
            pass

    ofiles = (file for file in os.listdir(source)
             if os.path.isfile(os.path.join(source, file)))
    for file in ofiles:
        # go through every file in the source folder
        extension = os.path.splitext(file)[1]
        extension = extension[1:]
        shutil.move(source + file, source + extension + '/' + file)
        # move from source , every file to (for example) source/exe/filename.exe

if __name__ == '__main__':
    get_files()