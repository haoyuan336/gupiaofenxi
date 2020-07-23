import pandas as pd 
import requests 
import datetime
import json
d = "20150608"
befordaycount = 5
# print(d[0:4])
# print(d[4:6])
# print(d[6:8])
# h = "{}-{}-{}".format(d[0:4],d[4:6],d[6:8])
# print(h)
def getData(code, start, end):
    url = "https://q.stock.sohu.com/hisHq?code={}&start={}&end={}".format(code, start, end)
    res = requests.get(url)
    return json.loads(res.text) 
# print(getData('cn_000002',20150608,20150609))
def convertWeek(dt):
    week = datetime.datetime.strptime(dt,"%Y-%m-%d").weekday()
    return week
def getBeforData(index, list, beforCount): 
    data = []
    for i in range(index + 1, index + 1 + beforCount): 
        data.append(i)

    return data


data = getData('cn_000002', 20150608,20150609)[0]['hq']
# print(data)
for index in range(0,len(data)) : 
    hq = data[index]
    week = convertWeek(hq[0])
    print(week)
    if week == 0: 
        print("周一")
        fiveData = getBeforData(index, data, befordaycount)
        if len(fiveData) == befordaycount: 
            
# list1 = []
# for i in range(1, 10): 
#     for j in range(1,10):
#         # print("i:{}, j:{} ,result: {}".format(i, j, i * j))
#         list1.append([i,j,i * j])
# column = ['num1','num2','result']
# test = pd.DataFrame(columns= column, index = None,data=list1)
# test.to_csv("/Users/chy/Desktop/pythonLearn/test.csv")
# dataframe = pd.read_csv("/Users/chy/Desktop/pythonLearn/test.csv")