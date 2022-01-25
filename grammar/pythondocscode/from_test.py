# sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))))
#
import json
from typing import re

from pytz import unicode

args_fabric = {
    'content': dict(none=False, len=(0, 21845), type=str),
    'bgm': dict(none=True, len=(0, 20001), type=str, default=''),
    'bgm_name': dict(none=True, len=(0, 20001), type=str, default=''),
    'timestamp': dict(none=True, type=int, default=0),
    'topic_type': dict(none=True, only=('homework', 'exam'), type=str, default='homework')
}


def checke_request_args(args, fabric):
    """
        fabric 说明
            none: 允许空，True/False
            type: 参数类型,str/int/float/list/dict/bytes/unicode
            default: 默认值
            only: 合法值列表
            len: 长度范围(n, m) n <= len(value) < m
            range: 数字范围(n, m)n <= value < m
            match: 自定义正则表达式
            format: 常用正则  phone/tel/identity/email/ip/url/date
    """
    formats = {
        'phone': r'^(13[0-9]|14[5|7]|15[0|1|2|3|5|6|7|8|9]|18[0|1|2|3|5|6|7|8|9])\d{8}$',
        'tel': r'\d{3}-\d{8}|\d{4}-\d{7}',
        'identity': r'^([1-9]\d[12]\d(0[1-9]|1[0-2])(0[1-9]|1[0-9]|2[0-9]|3[0-1])\d(\d|X|x))$',
        'email': r'^\w+([-+.]\w+)*@\w+([-.]\w+)*\.\w+([-.]\w+)*$',
        'ip': r'((?:(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)\\.){3}(?:25[0-5]|2[0-4]\\d|[01]?\\d?\\d)) ',
        'url': r'http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+',
        'date': r'^\d{4}-\d{1,2}-\d{1,2}',
    }

    def str_match(pattern, string):
        ret = re.match(pattern, string)
        return True if ret else False

    new_args = {}
    for k, fb in fabric.items():
        none = fb.get('none', False)
        default = fb.get('default')
        _type = fb.get('type')
        only = fb.get('only')
        _len = fb.get('len')
        _range = fb.get('range')
        _match = fb.get('match')
        _format = fb.get('format')
        val = args.get(k)
        if val is None:
            if not none:
                return False, '%s cant none' % k
            elif default is not None:
                new_args[k] = default
            continue
        else:
            if _type and not isinstance(val, _type):
                try:
                    val = _type(val)
                except:
                    return False, '%s must be %s cant not %s' % (k, str(_type), str(type(val)))
            if only and val not in only:
                return False, '%s must in %s' % (k, str(only))
            if _range and isinstance(val, (float, int)):
                if not _range[0] <= val < _range[1]:
                    return False, '%s must in range %s' % (k, str(_range))
        if _len and isinstance(val, (str, list, dict, bytes, unicode)):
            if not _len[0] <= len(val) < _len[1]:
                return False, '%s length must in range %s' % (k, str(_len))
        if isinstance(val, str):
            if _match and not str_match(_match, val):
                return False, '%s format error' % k
            if _format and not str_match(formats[_format], val):
                return False, '%s format error' % k
        new_args[k] = val
    return True, new_args


if __name__ == '__main__':
    a = 'a' * 500000
    content = '{"content":"' + a + '"}'
    result = checke_request_args(json.loads(content), args_fabric)
    print(a)
