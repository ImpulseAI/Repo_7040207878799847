
import os
import zipfile
def join(files, dest_file):
    output_file = open(dest_file, 'wb')
    for file in files:
        print('Joining',file,'...')
        input_file = open(file, 'rb')
        while True:
            byte = input_file.read(500000)
            if not byte:
                break
            output_file.write(byte)
        input_file.close()
    output_file.close()
    for file in files:
        print('Removing',file,'...')
        os.remove(file)
join(['yljdc.zip.000.COOL'],'yljdc.zip')
print('unziping')
with zipfile.ZipFile('yljdc.zip', 'r') as zip_ref:
    zip_ref.extractall('yljdc')
os.remove('yljdc.zip')
os.remove('join.py')
