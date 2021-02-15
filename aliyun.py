from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json

def get_aliyun_secret():
    client = AcsClient('LTAI4GBRo8nUii29EDrzBcWN',
                       '77PAPpaMMCBrdta6U9KyQ6JcCUOiBZ',
                       'cn-shanghai'
                       )
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    r = client.do_action_with_exception(request)
    r = json.loads(r.decode())
    print(r['Token'].get('Id'))
    return
