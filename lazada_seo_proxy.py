# coding: utf8
from mitmproxy import http
from urllib import request
import json


def response(flow: http.HTTPFlow):
    header_dict = {'Accept': 'application/json', 'Content-Type': 'application/json'}
    # 加上过滤条件
    if 'appsearch' in flow.request.pretty_url:
        if flow.response.status_code == 200:
            try:
                result = flow.response.json()
                print(result)
                # req = request.Request(
                #     url="http://127.0.0.1:5050/lazada/upload?type=seo_keyword", data=json.dumps(result).encode('utf-8'), headers=header_dict
                # )
                # print(request.urlopen(req).read().decode('utf-8'))
            except Exception as e:
                pass
            