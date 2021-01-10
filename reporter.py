#!/usr/bin/env python
# coding: utf-8

# In[139]:


import random
import requests
import json
import time

from urllib import parse

head={
    'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
    'Accept-Encoding': 'gzip'
}

def daka(identity, date, pos='中国'):
    print(f'{identity}开始签到')
    pos = parse.quote(pos)
    temp = random.randint(358, 365) / 10
    try:
        r = requests.post(
            url='http://yx.ty-ke.com/Home/Monitor/monitor_add',
            headers=head,
            data=f'mobile={identity}&city=%E5%A4%AA%E5%8E%9F%E5%B8%82&jk_type=%E5%81%A5%E5%BA%B7&district=%E5%B0%96%E8%8D%89%E5%9D%AA%E5%8C%BA&address={pos}&created={date}&title={temp}&jc_type=%E5%90%A6&wc_type=%E5%90%A6&is_verify=0&province=%E5%B1%B1%E8%A5%BF%E7%9C%81'
        )
        # 现在要通过字符串创建map，检查结果
        res_map = json.loads(r.text)
    except:
        print('请求错误')
        return False
    if res_map['code'] != '200':
        print(f"签到失败，结果错误[{res_map['msg']}]")
        return False
    else:
        print(f'签到成功，打卡温度:{temp}')
        return True

# 现在我们遍历所有的人，注意里面有生成时间！一天三次
def loop_daka(id_needed_list, date='2020-12-23%2010:00:00'):
    print('打卡开始')
    for identity, pos in id_needed_list:
        daka(identity, date, pos)
    print('打卡结束')

# 每一分钟检查一下，如果快到截止时间，则进行打卡操作。


# In[127]:


id_needed_list=[
        # 编辑的时候注意行末的逗号
        ('这里填写身份证号','你的所在位置'),
]

# 现在要动态生成时间
loop_daka(id_needed_list, '%E6%97%A5%E6%9C%9F%EF%BC%9A' + time.strftime('%Y-%m-%d', time.localtime()))


