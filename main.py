
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
    for file in ofiles:  # You could shorten this to one lin
        extension = os.path.splitext(file)[1]
        extension = extension[1:]
        shutil.move(source + file, source + extension + '/' + file)

if __name__ == '__main__':
    get_files()