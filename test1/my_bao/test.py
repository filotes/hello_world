import my_bao.str_util
import my_bao.file_util

print(my_bao.str_util.str_reverse("hanser,charlotte"))

print(my_bao.str_util.substr("hanser, charlotte", 0, 12))

my_bao.file_util.print_file_info("C:/test.txt")

my_bao.file_util.append_to_file("C:/test.txt", "你干嘛~哎呦")
