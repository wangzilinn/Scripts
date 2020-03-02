from typing import Dict


class FormatChineseNumeralToArabic:
    """将字符串中的汉字数字转为阿拉伯数字"""
    chinese_arabic_dict: Dict[str, int] = {"一": 1, "二": 2, "三": 3, "四": 4, "五": 5, "六": 6, "七": 7, "八": 8, "九": 9,
                                           "十": 10, "百": 100, "千": 1000, "万": 10000, "亿": 100000000,
                                           "零": 0}
    unify_chinese_character_dict: Dict[str, str] = {"两": "二", "俩": "二",
                                                    "仨": "三"}

    @staticmethod
    def convert(origin_str: str):
        """外部调用接口"""
        pretreated_str = FormatChineseNumeralToArabic.__pretreat(origin_str)
        chinese_numerl_list = FormatChineseNumeralToArabic.__extract_chinese_numerl(pretreated_str)
        for item in chinese_numerl_list:
            pretreated_str = pretreated_str.replace(item, str(FormatChineseNumeralToArabic.__chinese_to_arbic(item)), 1)
        return pretreated_str

    @staticmethod
    def __pretreat(input_str):
        """将句子中的两/俩/仨等等换成二/三
        """
        for char in FormatChineseNumeralToArabic.unify_chinese_character_dict:
            input_str = input_str.replace(char, FormatChineseNumeralToArabic.unify_chinese_character_dict[char])
        return input_str

    @staticmethod
    def __is_chinese_number(char):
        """检查参数字符是否为中文数字字符"""
        for key in FormatChineseNumeralToArabic.chinese_arabic_dict:
            if key == char:
                return True
        return False

    @staticmethod
    def __extract_chinese_numerl(input_str):
        """将句子中的数字块提取出来, 返回一个包含所有中文数字块的列表"""
        return_list = []
        str_length = len(input_str)
        char_pointer = 0
        while char_pointer < str_length:
            # 在第一次遇到中文数字时进入循环
            if FormatChineseNumeralToArabic.__is_chinese_number(input_str[char_pointer]):
                numeral_block = ""
                while FormatChineseNumeralToArabic.__is_chinese_number(input_str[char_pointer]):
                    numeral_block += input_str[char_pointer]
                    char_pointer += 1
                # 一个数字块结束
                return_list.append(numeral_block)
            char_pointer += 1
        return return_list

    @staticmethod
    def __chinese_to_arbic(input_str):
        """将纯的中文数字字符串转为阿拉伯数字"""

        def parse_simple_logic(input_str):
            """对于符合"..+数字+倍数+数字+倍数+数字"逻辑的字符串进行处理,
            正例:二十三, 三百四十二,
            反例:二百万, 二十万零五十"""
            char_pointer = len(input_str) - 1  # 指向最后一个字符
            result_number = 0
            while char_pointer >= 0:
                single_numeral = FormatChineseNumeralToArabic.chinese_arabic_dict[input_str[char_pointer]]
                if single_numeral < 10:  # 说明是0到9, 直接加
                    result_number += single_numeral
                else:  # 不是0~9 说明是倍数
                    multiplier = single_numeral
                    char_pointer -= 1  # 往前再读一个数,作为乘数的因数
                    single_numeral = FormatChineseNumeralToArabic.chinese_arabic_dict[input_str[char_pointer]]
                    result_number += multiplier * single_numeral
                char_pointer -= 1
            return result_number

        def locate_wan_or_yi_character(input_str):
            """检查字符串中第一个"万""亿"字符的位置, 以及那个字符代表的乘数
            如果找不到,则返回-1,1
            第一个返回值:字符的位置,
            第二个返回值:字符代表的乘数
            """
            locate_yi = input_str.find("亿")
            locate_wan = input_str.find("万")
            if locate_yi == -1 and locate_wan == -1:  # 没找到
                return -1, 1
            elif locate_yi == -1 and locate_wan != -1:  # 仅找到了"万"
                return locate_wan, 10000
            elif locate_yi != -1 and locate_wan == -1:  # 仅找到了"亿"
                return locate_yi, 100000000
            elif locate_yi < locate_wan:  # 都找到了, 比较位置
                return locate_yi, 100000000
            else:
                return locate_wan, 10000

        """开始对不同种类的输入字符串进行分类处理"""
        # "零"字符只有在单独存在时有意义, 否则可以直接删除:
        if input_str == "零":
            return FormatChineseNumeralToArabic.chinese_arabic_dict[input_str[0]]
        input_str = input_str.replace("零", "")  # 删除字符串所有的"零"
        str_length = len(input_str)
        # 如果是单个数字, 直接解析返回
        if str_length == 1:
            return FormatChineseNumeralToArabic.chinese_arabic_dict[input_str[0]]
        # 以十开头的字符(由于十开头的如"十二"的十前面没有数比较特殊, 即如果是"一十二"就可以用下面的解析)
        if input_str[0] == "十" and str_length == 2:
            return 10 + FormatChineseNumeralToArabic.chinese_arabic_dict[input_str[1]]
        # 如果字符串小于一万, 则肯定符合简单中文数字逻辑, 直接调用上述函数即可
        elif input_str.find("万") == -1 and input_str.find("亿") == -1:
            return parse_simple_logic(input_str)
        # 如果字符串中含有"万", "亿"字符, 则需要对字符串在这些字符处分段, 对每段进行单独处理, 再合并
        else:
            return_number = 0
            while True:
                location, multiplier = locate_wan_or_yi_character(input_str)
                if location != -1:
                    segmented_str = input_str[:location]
                    input_str = input_str[location + 1:]  # 下次循环使用本次切割后剩下的字符串
                else:
                    segmented_str = input_str
                return_number += parse_simple_logic(segmented_str) * multiplier
                if location == -1:
                    break
            return return_number



