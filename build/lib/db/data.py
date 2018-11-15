import requests


def get_books():
    response = requests.get('http://blog.konghy.cn/2018/04/29/setup-dot-py/')
    print(response.text)
    response.close()
    return '挪威的森林'
