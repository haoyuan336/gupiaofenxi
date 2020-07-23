import pandas as pd 
import requests 
import datetime
import json
d = "20150608"
befordaycount = 5
def getData(code, start, end):
    url = "https://q.stock.sohu.com/hisHq?code={}&start={}&end={}".format(code, start, end)
    res = requests.get(url)
    return json.loads(res.text) 
def convertWeek(dt):
    week = datetime.datetime.strptime(dt,"%Y-%m-%d").weekday()
    return week
def getBeforData(index, list, beforCount): 
    data = []
    for i in range(index + 1, index + 1 + beforCount): 
        if i < len(list):
            data.append(list[i])
    return data
def connectData(beforData, currentData):
    # print(beforData)
    list = []
    for data in beforData:
        for i in range(1, 10):
            # list
            list.append(data[i])
    list.append(currentData)
    return list
    # return [beforData, currentData]

data = getData('cn_600519', 20200113,20200720)[0]['hq']
# print(data)
allData = []
indexList = []
for index in range(0,len(data)) : 
    hq = data[index]
    week = convertWeek(hq[0])
    if week == 0: 
        fiveData = getBeforData(index, data, befordaycount)
        print(len(fiveData))
        if len(fiveData) == befordaycount: 
            print('找到了')
            indexList.append(hq[0])
            for i in fiveData:
                print(i[0])
            d = connectData(fiveData,hq[4])
            allData.append(d)


column = ['num1', 'num2', 'num3', 'num4', 'num5', 'num6', 'num7', 'num8', 'num9']
columnlist = []
for i in range(0,5):
    for col in column:
        columnlist.append("{}:{}".format(i + 1,col))

columnlist.append("result")
csvdata = pd.DataFrame(columns=columnlist, index=indexList,data=allData)     
csvdata.to_csv("/Users/workspace/gupiaofenxi/pythonLearn/test.csv")   


# print(allData)    
# print(len(allData[0]))  
# for         
            
# list1 = []
# for i in range(1, 10): 
#     for j in range(1,10):
#         # print("i:{}, j:{} ,result: {}".format(i, j, i * j))
#         list1.append([i,j,i * j])
# column = ['num1','num2','result']
# test = pd.DataFrame(columns= column, index = None,data=list1)
# test.to_csv("/Users/chy/Desktop/pythonLearn/test.csv")
# dataframe = pd.read_csv("/Users/chy/Desktop/pythonLearn/test.csv")