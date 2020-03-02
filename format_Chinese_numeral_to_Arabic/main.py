from FormatChineseNumeralToArabic import *
from tkinter.filedialog import *

"""测试:"""
# input_str = ["第三十六章", "第三千五百二十五和第五十个", "第五百亿二十万零五十三条", "第十章与第十二章", "第零章"]
# print([FormatChineseNumeralToArabic.convert(item) for item in input_str])

Tk().withdraw()
folder_path = askdirectory()
for file_name in os.listdir(folder_path):
    new_file_name = FormatChineseNumeralToArabic.convert(file_name)
    print(new_file_name)
    old_full_file_name = folder_path + "/" + file_name
    new_full_file_name = folder_path + "/" + new_file_name
    os.rename(old_full_file_name, new_full_file_name)

