# banned
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
import json
import requests
import base64

accessKey = 'LTAI4GBRo8nUii29EDrzBcWN'
accessSecret = '77PAPpaMMCBrdta6U9KyQ6JcCUOiBZ'
appKey = ''
botServerApi = 'http://127.0.0.1:5700/send_msg'

def get_aliyun_secret():
    client = AcsClient(accessKey,accessSecret,'cn-shanghai')
    request = CommonRequest()
    request.set_method('POST')
    request.set_domain('nls-meta.cn-shanghai.aliyuncs.com')
    request.set_version('2019-02-28')
    request.set_action_name('CreateToken')
    r = client.do_action_with_exception(request)
    r = json.loads(r.decode())
    return r['Token'].get('Id')

def tts(text):
    data = {
        'appkey':'m5gfCX2IKokzef72',
        "text": text,
        'token':get_aliyun_secret(),
        'format':'mp3',
        "sample_rate": "16000",
        "volume":'90',
        "pitch_rate":'0',
        "speech_rate":'-250',
        "voice":'Aiqi'
    }
    header = {
        "Content-Type": "application/json;charset=UTF-8"
    }
    r = requests.post('https://nls-gateway.cn-shanghai.aliyuncs.com/stream/v1/tts',data=json.dumps(data),headers=header)
    return base64.b64encode(r.content).decode()

def send_record(text):
    return '[CQ:record,file=base64://{}]'.format(tts(text))
