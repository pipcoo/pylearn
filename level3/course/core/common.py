# -*- coding:utf-8 -*-

import uuid,hashlib,time,pickle

# from config.setting import FILEDB

def create_uuid():
    return  str(uuid.uuid1())

def create_md5():
    m=hashlib.md5()
    m.update(bytes(str(time.time()),encoding='utf-8'))
    return m.hexdigest()


class dbfile(object):

    def __init__(self,file_name,file_type):
        self.file_name = file_name
        self.file_type = file_type
        self.file_path = FILEDB + '/' + file_type
        self.datafile = file_path + '/' + file_name
        if not os.path.exists(self.file_path):
            os.mkdir(self.file_path)

    # def save(self,data):
    #     with open (self.datafile,'w') as df:r
    #         pickle.dump(df,data)




def save():
    with open('',w) as fp:
        pickle.dump(data,fp)



if __name__ == '__main__':
    print(create_uuid())
    print(create_md5())