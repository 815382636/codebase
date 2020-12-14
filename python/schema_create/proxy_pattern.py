class Subject:
    def say(self):
        print("我是真的项目")


class Proxy:
    def say(self):
        print("代理开始")
        s = Subject()
        s.say()
        print("代理结束")


if __name__ == '__main__':
    p = Proxy()
    p.say()
