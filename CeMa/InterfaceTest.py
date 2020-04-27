'''
postman小技巧：
1.curl复制
2.code码
'''
# 面向过程编程
'''实例一get'''

import requests
import json

url = 'http://39.98.138.157:5001/api/demo'
# 字典
data = {"limit": "1"}
# 将字典换成json格式
data = json.dumps(data)
headers = {
    "Content-Type": "application/json"  # 字典类型
}

# 发送请求
res = requests.get(url=url, params=data, headers=headers)
# 返回接口消息体和状态码
print(res.text, res.status_code)

'''实例二post'''
url = 'http://39.98.138.157:5001/api/login'
# 字典
data = {"username": "admin", "password": "123456"}
# 将字典换成json格式
data = json.dumps(data)
headers = {
    "Content-Type": "application/json"  # 字典类型
}

# 发送请求
res = requests.post(url=url, data=data, headers=headers)
# 返回接口消息体和状态码
print('第二个接口', res.text, res.status_code)

'''封装:面向函数编程'''


def test_demo():
    url = 'http://39.98.138.157:5001/api/demo'
    # 字典
    data = {"limit": "1"}
    # 将字典换成json格式
    data = json.dumps(data)
    headers = {
        "Content-Type": "application/json"  # 字典类型
    }

    # 发送请求
    res = requests.get(url=url, params=data, headers=headers)
    # 返回接口消息体和状态码
    print(res.text, res.status_code)


def test_login():
    url = 'http://39.98.138.157:5001/api/login'
    # 字典
    data = {"username": "admin", "password": "123456"}
    # 将字典换成json格式
    data = json.dumps(data)
    headers = {
        "Content-Type": "application/json"  # 字典类型
    }

    # 发送请求
    res = requests.post(url=url, data=data, headers=headers)
    # 返回接口消息体和状态码
    print('第二个接口', res.text, res.status_code)


test_demo()
test_login()

'''unittest,htmlTestRuner用例组织框架，测试报告'''
import unittest
# import TestCase(unittest.TestCase):
def test_demo():
    url = 'http://39.98.138.157:5001/api/demo'
    # 字典
    data = {"limit": "1"}
    # 将字典换成json格式
    data = json.dumps(data)
    headers = {
        "Content-Type": "application/json"  # 字典类型
    }

    # 发送请求
    res = requests.get(url=url, params=data, headers=headers)
    # 返回接口消息体和状态码
    print(res.text, res.status_code)


def test_login():
    url = 'http://39.98.138.157:5001/api/login'
    # 字典
    data = {"username": "admin", "password": "123456"}
    # 将字典换成json格式
    data = json.dumps(data)
    headers = {
        "Content-Type": "application/json"  # 字典类型
    }

    # 发送请求
    res = requests.post(url=url, data=data, headers=headers)
    # 返回接口消息体和状态码
    print('第二个接口', res.text, res.status_code)


if __name__ == '__main__':
    unittest.main()
'''pip install pytest或conda install pytest'''
import pytest

pytest.main(['-s', 'InterfaceTest.py', '--html=yideng.html'])

'''使用data.yaml文件记录数据'''
import yaml


def read_yaml():
    with open("yaml路径", 'r')as f:
        cfg = yaml.load(f.read())
        return cfg


data = read_yaml()
print(data)
print(data['api_url'])
url = data['api_url']
