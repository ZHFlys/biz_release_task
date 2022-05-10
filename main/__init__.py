# -*- coding: utf-8 -*-#

import json


def biz_test_http(argv):
    argv_json = json.loads(argv)
    argv_msg = argv_json['msg']
    return test_http(argv_msg)


def test_http(msg):
    return '测试同步http方法：%s' % msg


if __name__ == '__main__':
    biz_test_http('{"msg": "test"}')
