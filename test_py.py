# -*- coding: utf-8 -*-#

import json
import requests
import time
import random


def biz_test_async(argv):
    argv_json = json.loads(argv)
    argv_msg = argv_json['msg']
    return test_async(argv_msg)


def test_async(msg):
    success = False
    res_msg = ''
    # 开始了，暂停5秒发进度通知，然后发送QQ消息，暂停5秒后随机发成功或者失败消息
    print('发进度回调')
    time.sleep(5)
    to_qq = '572705296'
    url = 'http://120.78.214.110:5700/send_msg?user_id={}&message={}'.format(to_qq, msg)
    res = requests.get(url, timeout=60)
    print(res.text)
    time.sleep(5)
    if random.randint(1, 3) % 2 == 0:
        print('发送成功回调')
        res_msg = '发送成功回调'
        success = True
    else:
        print('发送失败回调')
        res_msg = '发送失败回调'

    return (success, '测试异步发QQ消息方法：%s，%s' % (msg, res_msg))


if __name__ == '__main__':
    biz_test_async('{"msg": "test"}')
