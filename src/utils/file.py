import os
from config.file import path

def remove_files(path):
    for root, _, files in os.walk(path, topdown=False):
        for file in files:
            file_path = os.path.join(root, file)
            try:
                os.remove(file_path)
            except OSError as e:
                print(f"Error occurred while removing {file_path}: {e}")
                            
def save_file(content, path, filename, extension):
    try:
        file = os.path.join(path, filename + '.' + extension) 
        with open(file, 'wb') as f:
            f.write(content)
    except:
        print('ERROR: not able to save the file.')