import re


s = '<h1>你好</h1>666*Notice*\toh\rsee\ngood&nbsp;'



def clear_special_char(content):
    '''
    正则处理特殊字符
    :param content:原文本
    :return: 清除后的文本
    '''
    s = re.sub(r"</?(.+?)>|&nbsp;|\t|\r", "", content)
    s = re.sub(r"\n", " ", s)
    s = re.sub(r"\*", "\\*", s)

    return s


print(clear_special_char(s))


