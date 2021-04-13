from urllib import request, error, parse, robotparser
import chardet
"""
    request 打开和读取urls
    error   包含request产生的常见错误，使用try捕捉
    parse   包含解析url的方法
    robotparser 解析robot.txt文件
"""


def main():
    url = 'https://www.baidu.com'
    rsp = request.urlopen(url)
    html = rsp.read()
    cs = chardet.detect(html)
    print(cs)
    html = html.decode()
    # print(html)


if __name__ == '__main__':
    main()
