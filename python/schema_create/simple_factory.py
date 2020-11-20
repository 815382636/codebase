from abc import ABCMeta, abstractmethod


class Payment(metaclass=ABCMeta):  # ABC是Abstract Base Class的缩写。

    @abstractmethod  # 抽象方法
    def pay(self, money):
        pass


class AliPay(Payment):

    def __init__(self, yu_e_bao=False):
        self.yu_e_bao = yu_e_bao

    def pay(self, money):

        if self.yu_e_bao:
            print(f'use yu_e_bao pay {money}')

        else:
            print(f'use zhifubao pay {money}')


class WeChat(Payment):

    def pay(self, money):
        print(f'use Wechat pay {money}')


class Paymethod():

    @staticmethod
    def create_payment(method):

        if method == 'yu_e_bao':
            return AliPay(True)

        elif method == 'zhifubao':
            return AliPay(False)

        elif method == 'Wechat':
            return WeChat()
        else:
            print('method error')


f = Paymethod.create_payment('zhifubao')
f.pay(30)  # use zhifubao pay 30
f = Paymethod.create_payment('Wechat')
f.pay(300)
