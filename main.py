import argparse
import os.path
import re
import sys
import subprocess


def searchso(sopath, s):
    """
    搜索so文件字符串
    :param s: 需要搜索的字符串
    """
    if 'nt' == os.name:
        commad = os.path.join(os.path.split(sys.argv[0])[0], "commad/strings64.exe")
    else:
        commad = 'strings'
    process = subprocess.Popen([commad, '-a', sopath], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    out, err = process.communicate(timeout=5)
    arrayStr = []
    result = None
    if out is not None:
        print("> {}:开始分析!".format(os.path.split(sopath)[1]))
        print("> commad: strings -a {} | grep {}".format(sopath, s))
        result = out.decode('utf-8')
        if args.saveall is not None and result is not None:
            with open(args.saveall, 'a') as f:
                f.write('<====' + os.path.split(sopath)[1] + "====\n")
                f.write(result)
                f.write("====" + os.path.split(sopath)[1] + "====>\n")
                f.close()
        try:
            if args.ignorecase == 1:
                print("> -i 1 默认忽略大小写")
                items = re.finditer(s, result, re.IGNORECASE)
            else:
                items = re.finditer(s, result)
                print("> -i 0 区分大小写")
            for i in items:
                arg = result[i.start():-1]
                print(arg[:arg.find('\n')])
                if args.output:
                    arrayStr.append(arg[:arg.find('\n')])
        except Exception as e:
            print(e)
        print("> {}:分析完成!".format(os.path.split(sopath)[1]))
        if args.output is not None and len(arrayStr):
            with open(args.output, 'a') as f:
                f.write('<====' + os.path.split(sopath)[1] + "====\n")
                for i in arrayStr:
                    f.write(i + '\n')
                f.write("====" + os.path.split(sopath)[1] + "====>\n")
                f.close()
                print("> 分析结果:", args.output)
    else:
        print("> {}:分析超时 ".format(os.path.split(sopath)[1]), err)


def rangedir(soPath, s):
    """
    遍历soPath 目录下所有so文件
    :param s: 需要搜索的字符串
    :param soPath:
    """
    for root, dirs, files in os.walk(soPath):
        for i in files:
            # print(i)
            searchso(os.path.join(root, i), s)


def main():
    try:
        if os.path.isfile(args.output):
            os.remove(args.output)
        if os.path.isfile(args.saveall):
            os.remove(args.saveall)
    except Exception as e:
        print("remove {}".format(args.output), e)
        return
    if os.path.isdir(args.sofilepath):
        print(args.sofilepath, "> 是一个目录")
        rangedir(args.sofilepath, args.search)
    elif os.path.isfile(args.sofilepath):
        print(args.sofilepath, "> 是一个文件")
        searchso(args.sofilepath, args.search)
    else:
        print(args.sofilepath, "> 错误的参数!")


parser = argparse.ArgumentParser(description="so文件字符串搜索")
parser.add_argument('-f', '--sofilepath', required=True, type=str, help="so文件或目录路径")
parser.add_argument('-s', '--search', required=True, type=str, help="需要搜索的字符串")
parser.add_argument('-i', '--ignorecase', type=int, default=1, help="忽略大小写 type(1|0) 默认为1忽略")
parser.add_argument('-o', '--output', type=str, help=" 参数 保存到文件")
parser.add_argument('-a', '--saveall', type=str, default="./allstr.log", help="保存所有字符串到文件 默认./allstr.log")
args = parser.parse_args()

if __name__ == '__main__':
    main()
    # print(args.sofilepath)
    # print(args.search)
    # print(args.ignorecase)
    # print(args.output)
