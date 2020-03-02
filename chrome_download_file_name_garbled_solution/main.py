import os


def get_file_paths(file_dir, type):
    L=[]
    for root, dirs, files in os.walk(file_dir):
        for file in files:
            if os.path.splitext(file)[1] == type:
                L.append(os.path.join(root, file))
    return L


print("注意:在待转换的文件夹中必须全部都是乱码文件, 否则可能会导致转换失败")
print("注意:转码之前请先做文件备份")
path = input("请输入存在乱码的文件的上一层文件夹路径：")
extension_name = input("请输入要转码文件的拓展名: 如\".caj\", \".pdf\": ")
file_paths_list = get_file_paths(path, extension_name)
for garbled_path in file_paths_list:
    garbled_file_name = garbled_path.split("\\")[-1]
    recoded_file_name = garbled_file_name.encode('iso-8859-1').decode("GBK")
    recoded_path = garbled_path.replace(garbled_file_name, recoded_file_name)
    os.rename(garbled_path, recoded_path)
print("转换完成")


