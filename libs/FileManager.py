import glob
import json, csv
import os
from datetime import datetime

class FileManager():
    def __init__(self):
        pass

    def json_from_json_file_nm(self, filename):
        with open(filename, encoding='utf-8') as f:
            return json.loads(f.read())

    '''
    params
    file_location : './separated/*.json'
    '''
    def get_file_list(self, file_location):
        file_names = glob.glob(file_location)
        print(len(file_names))
        return file_names

    def read_csv_file_into_list(self, filename, encoding='utf-8'):
        with open(filename, newline='', encoding=encoding) as f:
            ll = csv.reader(f)
            return list(ll)
    '''
    params
    from_filename:str
    file_cnt:int default = 10
    target_path default = './separated/'
    '''
    def csv_separate_files(self, from_filename, file_cnt=10, target_path='./separated/'):
        print('started at:', datetime.now())
        print('원본파일 용량에 따라 몇분 걸릴 수 있습니다.')
        # target_path가 없으면 만든다.
        if not os.path.isdir(target_path):
            os.makedirs(target_path)
        ll = open(from_filename, 'r', encoding='utf-8').readlines()
        print('total:', len(ll))
        first_line = ll[0]
        records_per_file = len(ll) // file_cnt
        base_name = os.path.basename(from_filename)
        for i in range(file_cnt):
            print('{} file started'.format(i))
            with open('{}{:02d}_{}'.format(target_path, i, base_name), 'w+', encoding='utf-8') as f:
                if i == 0:
                    f.writelines(ll[i * records_per_file: i * records_per_file + records_per_file])
                elif i == file_cnt - 1:
                    f.writelines(ll[i * records_per_file: len(ll)])
                else:
                    f.writelines(first_line)
                    f.writelines(ll[i * records_per_file: i * records_per_file + records_per_file])

        print('finished at:', datetime.now())

