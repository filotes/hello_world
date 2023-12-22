def print_file_info(file_name):
    """
    打开文件并输出文件的全部内容
    :param file_name:   文件的路径
    :return: None
    """
    file1 = None
    try:
        file1 = open(file_name, "r", encoding="UTF-8")
        cont = file1.read()
        print("文件的内容如下:")
        print(cont)
    except Exception as bug:
        print(f"程序出现异常了，原因是{bug}")
    finally:
        if file1:       # 如果变量是None，表示False，如果有任何内容，就是True
            file1.close()


def append_to_file(file_name, data):
    """
    将数据追加到指定的文档
    :param file_name:   文件路径
    :param data:    追加的文件内容
    :return:    None
    """
    file2 = open(file_name, "a", encoding="UTF-8")
    file2.write(data)
    file2.close()


if __name__ == '__main__':
    print_file_info("C:/test.txt")
