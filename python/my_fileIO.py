import json

"""
使用魔法
"""
# json.loads json.dumps  针对于字符串
# json.load json.dump   针对于文件

params = {
    'symbol': '123456',
    'type': 'limit',
    'price': 123.4,
    'amount': 23
}

with open('params.json', 'w') as fout:
    params_str = json.dump(params, fout)

with open('params.json', 'r') as fin:
    original_params = json.load(fin)
