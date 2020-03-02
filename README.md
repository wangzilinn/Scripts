# Scripts

收集方便工作的各种脚本

- [Scripts](#scripts)
  * [统计Git库一周代码量](#统计Git库一周代码量)
  * [将中文数字字符串转为阿拉伯数字字符串](#将中文数字字符串转为阿拉伯数字字符串)
  * [修复Chrome下载文件乱码问题](#修复Chrome下载文件乱码问题)

# 统计Git库一周代码量

## Source:
[Source](https://github.com/wangzilinn/Scripts/tree/master/code_statistic)

项目组内要求每周汇报自己所管理的库的代码情况 这个脚本可以直接统计 比CSDN上面的不知道高到哪里去了

写这个的目的主要是每周要交工作总结,需要统计代码量

> Note: CSDN上的git代码量统计都是一堆代码, 能用但不可读,  因此写了这个可读性很强, 可以充分自定义的脚本, 用于统计代码

## 使用方法:

将这个`.sh`文件放在想要被统计的代码库中, 使用git bash运行, 即可计算出过去一周该库的代码变化情况

## 输出示例:

双击运行后,输出:

```bash
过去一周代码统计:

From 2020-02-24-Mon
To   2020-03-02-Mon

Added lines: 401
Removed lines: 0
Total lines: 401
```


# 将中文数字字符串转为阿拉伯数字字符串

将字符串中的所有中文数字转为阿拉伯数字,如"第三万亿零五千章"转为"第3000000005000章"

## Source:

[Source](https://github.com/wangzilinn/Scripts/tree/master/format_Chinese_numeral_to_Arabic)

## 使用方法:

1. 运行main.py
2. 选择想要转化的文件夹
3. 转换完:此时该文件夹中的子文件(夹)所有中文数字转化为阿拉伯数字
   注意:这不是递归的转换,只会转化第一级的子目录

## 测试字符列表:

1. "第三十六章", 
2. "第三千五百二十五和第五十个", 
3. "第五百亿二十万零五十三条", 
4. "第十章与第十二章", 
5. "第四章"

## 测试结果列表:

1. 第36章
2. 第3525和第50个
3. 第50000200053条
4. 第10章与第12章
5. 第4章

## 包使用情况:

使用Tkinter来提供文件选择框

## 算法概述:

### 普遍情况:

通过分析中文数字表示方式, 可以提取中最根本的表达规律为:

...数字+倍数+数字+倍数+数字

如:

三千五百二十五, 五十三, 六百四十

那么就可以从最低位读起,遇到倍数就再往前读一个,并使两者相乘,整体相加即可

### 特殊情况:

1. 字符串中出现"零"字符,仅在单独出现时有意义
   - 一千零五十=一千五十=1050
   - !!对于一千五这种应该表示为一千零五百的情况程序无法处理, 因为这本身表示不标准!!
2. 字符串为十几的情况, 如"十二", 应该表示为"一十二", 这种情况单独处理
3. 字符串中出现"万","亿"的情况, 在超过以上字符时, 是对超过的部分单独计算并再乘上"亿""万",如一百万,首先他不属于普遍情况(连续两个倍数"百""万"),就需要先将"万"提取出来,单独分析"一百",在乘以"万"即可, "亿"同理



## 程序概述:

1. 对字符串进行预处理
   - 将字符串中的诸如"两","仨",替换为"二", "三"
2. 提取出句子中的中文数字部分
   - 如输入"第三千五百二十五和第五十个", 则如返回["三千五百二十五","五十"]的列表
3. 对提取出的纯中文数字进行处理:
   0. 对0的处理
   1. 对于单个字符的情况, 直接处理
      - "一"->1
      - "八"->8
   2. 对十几的字符, 单独处理
   3. 对于存在"亿""万"的, 在以上字符位置对字符串做满足普遍规律的分段处理,再相加

## 需求来源:

课件中经常存在中文标号的情况, 在该情况下使用按名称排序会导致排序后不是正常顺序, 故写个脚本把字符串中的所有中文数字转为阿拉伯数字,即可正常排序

# 修复Chrome下载文件乱码问题

chrome下载中文文件名经常有乱码的情况(尤其是从知网下载的论文), 写了个脚本把乱码转换成人话

## Source:

[Source](https://github.com/wangzilinn/Scripts/tree/master/chrome_download_file_name_garbled_solution)

## 解释器运行环境:

python3.6

## 使用方法:

下载main.py运行即可

## 使用示例:

### 原始文件夹:

![image](https://https://github.com/wangzilinn/Scripts/blob/master/chrome_download_file_name_garbled_solution/img/%E7%A4%BA%E4%BE%8B_%E5%AD%98%E6%94%BE%E4%B9%B1%E7%A0%81%E6%96%87%E4%BB%B6%E7%9A%84%E6%96%87%E4%BB%B6%E5%A4%B9.JPG)

### 使用转换脚本:

分别输入文件夹路径及要转换的文件拓展名
![image](https://https://github.com/wangzilinn/Scripts/blob/master/chrome_download_file_name_garbled_solution/img/%E7%A4%BA%E4%BE%8B_%E6%93%8D%E4%BD%9C%E8%BF%87%E7%A8%8B.JPG)

### 运行结果:

![image](https://github.com/wangzilinn/Scripts/blob/master/chrome_download_file_name_garbled_solution/img/%E7%A4%BA%E4%BE%8B_%E8%BD%AC%E7%A0%81%E7%BB%93%E6%9E%9C.JPG)

