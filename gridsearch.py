import requests
import json
import csv
import codecs

# dist的位置可以用api获取：
#  http://api.map.baidu.com/lbsapi/getpoint/index.html
# dest：汇众大厦
dest = '116.313971,40.05305'.split(',')
# dest2: 东直门
dest2 = '116.439366,39.954859'.split(',')

weidubound = [116.280626, 116.451933]
jingdubound = [39.863324, 40.057551]


def prepare_origin(step=0.0005):
    orig1 = []
    orig2 = []
    i = weidubound[0]
    while i < weidubound[1]:
        orig1.append(round(i, 6))
        i += step
    i = jingdubound[0]
    while i < jingdubound[1]:
        orig2.append(round(i, 6))
        i += step

    return orig1, orig2


def call_api(orig1,orig2):
    ak = 'pEvUgdMq9GMbCiaLCDq9Ql6Mjrg2MqKB'  # ak需要去百度地图申请
    url = 'http://api.map.baidu.com/direction/v2/transit?origin={},{}&destination={},{}&ak={}'.format(orig2, orig1,
                                                                                                      dest2[1], dest2[0],
                                                                                                      ak)
    res = requests.get(url)
    #print(res.text)
    json_data = json.loads(res.text)

    duration = []
    for item in json_data['result']['routes']:
        #print(item['duration'])
        duration.append([orig1, orig2, item['duration']])
    return duration


if __name__ == "__main__":
    orig1, orig2 = prepare_origin(0.01)
    result = []
    for i in orig1:
        for j in orig2:
            duration = call_api(i, j)
            print(i, j)
            result.append(duration)
    print(result)
    f = open('result.csv', 'w')
    writer = csv.writer(f)
    for i in result:
        writer.writerow(i)
    f.close()