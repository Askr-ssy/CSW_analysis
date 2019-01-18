import os
import jieba

fc =lambda str:" ".join(jieba.cut(in_str))

def get_target_file(need_TW = False):
    dir_path = os.path.dirname(os.path.abspath(__file__))
    for file in os.listdir("test"):
        name = file.split(".")
        if name[1] == "utf8":
            if not "tw" in name[0]:
                yield os.path.join(dir_path,"test",file)
            elif "tw" in name[0] and need_TW:
                yield os.path.join(dir_path,"test",file)

if __name__ == "__main__":
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
