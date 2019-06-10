import os

import jieba
import json

from _utils import find_all_file,cut_filename

ROOT=os.path.dirname(os.path.abspath(__file__))
fc =lambda str:" ".join(jieba.cut(str))
path=lambda ROOT,*a:os.path.join(ROOT,*a)

def get_target_file(need_TW = False):
    '''
    生成测试文件列表
    '''
    for file_path in find_all_file(path(ROOT,'res'),suffix_filter='utf8'):
        name = cut_filename(file_path)
        if name[2] == ".utf8":
            if "tw" not in name[1]:
                yield file_path
            elif "tw" in name[1] and need_TW:
                yield file_path

if __name__ == "__main__":
    '''
    使用jieba切分词语并且输出文件
    '''
    jieba.initialize()
    for file_address in get_target_file():
        print('file_address',file_address)
        out = []
        with open(file_address,"r",encoding="utf-8") as file:
            for line in file.readlines():
                out.append(fc(line))
        res_address = file_address.replace('res','test')
        isExists = os.path.exists(cut_filename(res_address)[0])
        if not isExists:
            os.makedirs(os.path.split(res_address)[0])
        with open(res_address,"w",encoding="utf-8") as file:
            file.writelines(out)
            file.write("\nstop code\n")
