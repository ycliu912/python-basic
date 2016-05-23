#-*-coding: utf-8 -*-
import json
import codecs

s = json.loads('{"name":"test", "type":{"name":"seq", "parameter":["", ""]}}')
print s
print s.keys()
print s["name"]
print s["type"]["name"]
print s["type"]["parameter"]

#f = file(r'json.templete')
f = codecs.open('ok','r', 'utf_8_sig')
jsonobj = json.load(f)
#列表用序号来查询
print jsonobj
#print jsonobj['Key']
f.close