import requests
import json

def history_of_today():
    r = requests.post('https://www.ipip5.com/today/api.php?type=json')
    s = r.json()
    mes = '历史上的今天  ' + s['today']
    for i in s['result']:
        mes += '#$@$#'
        mes += i['year'] + ' ' + i['title']
    return mes
    #s = '今天是：\\{}'.format(r['today'])
    #for text in r['content']:
    #    s += '#$@$#' + text
    #return s

def random_acg_pic():
    r = requests.post('http://www.dmoe.cc/random.php?return=json')
    s = r.json()
    return '[CQ:image,file={}]'.format(s['imgurl'])

def spirit_guy():
    r = requests.post('https://cdn.ipayy.net/says/api.php?encode=json')
    s = r.json()
    return s['say']

def random_hitokoto():
    r = requests.get('https://v1.hitokoto.cn/?c=a&c=b&c=c&c=f')
    s = r.json()
    return s['hitokoto'] + '#$@$#from:' + s['from']
