from functools import wraps


def requires(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        print("我是装饰器")
        f(*args, **kwargs)

    return decorated


@requires
def add(a, b):
    print(f'{a} + {b} = {a + b}')


if __name__ == '__main__':
    add(1, 1)
