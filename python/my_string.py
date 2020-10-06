import re


def delete_punctuation(content):
    """
    删除字符串中存在的标点符号和换行符等
    :param content: 字符串
    :return: content: 无标点的字符串
    """
    return re.sub(r'[^\w ]', '', content)


"""
使用魔法
"""
# -----------------------------------------------------------------------
# 字符串的格式化
print(f"你是{3+2}")
