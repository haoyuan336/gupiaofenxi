import pandas as pd
import tensorflow as tf

list1 = []
for i in range(1, 10): 
    for j in range(1,10):
        # print("i:{}, j:{} ,result: {}".format(i, j, i * j))
        list1.append([i,j,i * j])
column = ['num1','num2','result']
test = pd.DataFrame(columns= column, index = None,data=list1)
test.to_csv("/Users/chy/Desktop/pythonLearn/test.csv")
dataframe = pd.read_csv("/Users/chy/Desktop/pythonLearn/test.csv")
# train,test=train_
print(dataframe.head())
def df_to_dataset(dataframe,shuffle=True,batch_size=32):
    dataframe = dataframe.copy()
    labels = dataframe.pop('result')
    ds= tf.data.Dataset.from_tensor_slices((dict(dataframe),labels))
    if shuffle:
        ds = ds.shuffle(buffer_size=len(dataframe))
    ds = ds.batch(batch_size)
    return ds    
batch_size = 5
# train_ds = df_to_dataset()
