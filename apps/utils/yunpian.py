# -*- coding: utf-8 -*-
# pip install requests
from _sha1 import sha1

import requests
import urllib.request
import time
import uuid
import hmac
import base64
import datetime
import json


def params(accesskeyid, mobiles, tpl_code, tpl_params, sign_name):
    p = [
        ["SignatureMethod", "HMAC-SHA1"],
        ["SignatureNonce", uuid.uuid4().hex],
        ["AccessKeyId", accesskeyid],
        ["SignatureVersion", "1.0"],
        ["Timestamp", time_now_fmt()],
        ["Format", "JSON"],

        ["Action", "SendSms"],
        ["Version", "2017-05-25"],
        ["RegionId", "cn-hangzhou"],
        ["PhoneNumbers", "{0}".format(mobiles)],
        ["SignName", sign_name],
        ["TemplateParam", json.dumps(tpl_params, ensure_ascii=False)],
        ["TemplateCode", tpl_code],
        ["OutId", "123"],
    ]
    return p


def time_now_fmt():
    r = datetime.datetime.utcfromtimestamp(time.time())
    r = time.strftime("%Y-%m-%dT%H:%M:%SZ", r.timetuple())
    return r


def special_url_encode(s):
    r = urllib.parse.quote_plus(s).replace("+", "%20").replace("*", "%2A").replace("%7E", "~")
    return r


def encode_params(lst):
    s = "&".join(list(map(
        lambda p: "=".join([special_url_encode(p[0]), special_url_encode(p[1])]),
        sorted(lst, key=lambda p: p[0])
    )))
    return s


def prepare_sign(s):
    r = "&".join(["GET", special_url_encode("/"), special_url_encode(s)])
    return r


def sign(access_secret, prepare_str):
    k = "{0}{1}".format(access_secret, "&")
    r = hmac.new(k.encode(), prepare_str.encode(), sha1).digest()
    base_str = base64.b64encode(r).decode()
    return special_url_encode(base_str)


def _send_sms_ali(mobiles, tpl_code, tpl_params):
    prefix_url = "https://dysmsapi.aliyuncs.com/?"

    accesskeyid = ""
    accesssecret = ""
    sign_name = "许许生鲜"

    params_lst = params(accesskeyid, mobiles, tpl_code, tpl_params, sign_name)
    eps = encode_params(params_lst)
    prepare_str = prepare_sign(eps)
    sign_str = sign(accesssecret, prepare_str)

    url = "{0}Signature={1}&{2}".format(prefix_url, sign_str, eps)

    r = requests.get(url)
    if r.status_code != 200:
        return False
    else:
        jn = json.loads(r.text)
        if jn.get("Code") == "OK":
            return True
        else:
            return False


if __name__ == "__main__":
    # 签名校验测试，与测试样例一致，待拿到正式参数时再做测试修改
    _tpl_code = "SMS_137865184"
    _tpl_params = {"code": "0000"}
    _send_sms_ali("17607177645", _tpl_code, _tpl_params)
