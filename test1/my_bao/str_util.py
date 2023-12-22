def str_reverse(s):
    """
    功能是反转字符串
    :param s:   将被反转的字符
    :return:    反转后的字符串
    """
    return s[::-1]


def substr(s, x, y):
    """
    功能是字符串切片
    :param s:   要切片的字符串
    :param x:   开始切片的位置
    :param y:   结束切片的位置
    :return:    切片后的字符
    """
    return s[x:y:]


if __name__ == '__main__':
    print(str_reverse("charlotte"))
    print(substr("hanser", 0, 4))
