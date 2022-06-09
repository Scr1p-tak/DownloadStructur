
import os
import shutil


def get_files():
    source = r'/home/mrx/Downloads/'
    files = os.listdir(source)
    for file in files:
        extension = os.path.splitext(file)[1]
        extension = extension[1:]
        try:
            os.makedirs('/home/mrx/Downloads/' + extension)
        except FileExistsError:
            pass

    ofiles = (file for file in os.listdir(source)
             if os.path.isfile(os.path.join(source, file)))
    for file in ofiles:  # You could shorten this to one lin
        extension = os.path.splitext(file)[1]
        extension = extension[1:]
        shutil.move(source + file, '/home/mrx/Downloads/' + extension + '/' + file)

if __name__ == '__main__':
    get_files()