import os
import random

import re

from Stoce_DataStore import Stock_DataStore
import pandas as pd;

#从地址中获取CSV格式的一分钟数据
def getData(path, idx=99999999, randomArg=0):
    list0 = os.listdir(path)
    list_dir = []
    list_file = []
    pattern = re.compile(r'(SH[\w\W]+)\.csv')
    stockStore = Stock_DataStore();
    # 最大文件取数数量
    index = idx;
    for i in list0:
        # 随机取文件
        if random.randint(0, randomArg) > 0:
            continue;
        # index -= 1;
        if index < 1:
            break;
        if os.path.isdir(path + '/' + i):
            list_dir.append(path + '/' + i)
            print(path + '/' + i)
        else:
            match = pattern.match(i);
            if match:
                print(str(index) + ":reading:" + match.group(1));
                sourceData = pd.read_csv(path + '/' + i, header=None, sep=',',
                                         names=['Date', 'Time', 'Start', 'Max', 'Min', 'End', 'Count', 'Amount'])
                values = sourceData.values;
                for detailList in values:
                    stockStore.Insert(match.group(1), detailList);
                index -= 1;
    return stockStore
