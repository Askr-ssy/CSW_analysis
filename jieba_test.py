import os
import jieba
import json

from _utils import find_all_file

ROOT=os.path.dirname(os.path.abspath(__file__))
fc =lambda str:" ".join(jieba.cut(str))
path=lambda ROOT,*a:os.path.join(ROOT,*a)

def get_target_file(need_TW = False):
    '''
    生成测试文件列表
    '''
    for file in find_all_file(path(ROOT,'test')):
        name = file.split(".")
        if name[1] == "utf8":
            if not "tw" in name[0]:
                yield os.path.join(dir_path,"test",file)
            elif "tw" in name[0] and need_TW:
                yield os.path.join(dir_path,"test",file)

if __name__ == "__main__":
    '''
    使用jieba切分词语并且输出文件
    '''
    jieba.initialize()
    for file_address in get_target_file():
        out = []
        with open(file_address,"r",encoding="utf-8") as file:
            for line in file.readlines():
                out.append(fc(line))
        res_address = file_address.replace("test","res")
        isExists = os.path.exists(os.path.split(res_address)[0])
        if not isExists:
            os.makedirs(os.path.split(res_address)[0])
        print(res_address)
        with open(res_address,"w",encoding="utf-8")as file:
            file.writelines(out)
            file.write("\nstop code\n")
