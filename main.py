import requests
import json
import pprint
from bs4 import BeautifulSoup as bs
ak = 'pEvUgdMq9GMbCiaLCDq9Ql6Mjrg2MqKB'#ak需要去百度地图申请
address = '汇众大厦'

orig='116.445088,39.925269'.split(',')
orig2='116.441351,39.925186'.split(',')
#可以看出，500米左右的一步大概对应0.0001的偏移。
leftpoint = 116.280626,39.923554
uppoint = 116.385261,40.057551
rightpoint = 116.499669,39.913814
downpoint = 116.401933,39.863324
#维度范围从116.280626到116.401933
#经度范围从39.923554到39.913814

dest='116.313971,40.05305'.split(',')
print(dest[1],dest[0])


#url = 'http://api.map.baidu.com/geocoder/v2/?address={}&output=json&ak={}'.format(address,ak)
url = 'http://api.map.baidu.com/direction/v2/transit?origin={},{}&destination={},{}&ak={}'.format(orig[1], orig[0], dest[1], dest[0], ak)
res = requests.get(url)
json_data = json.loads(res.text)
#pprint.pprint(json_data)#美观打印数据结构
#print('================================')
#print(json_data['result']['routes'][0]['duration'])
#print(json_data['result']['routes'][1]['duration'])
for item in json_data['result']['routes']:
    print(item['duration'])
#with open("test.txt","w") as f:
#    f.write(res.text)
#然后看看怎么解析这个json吧