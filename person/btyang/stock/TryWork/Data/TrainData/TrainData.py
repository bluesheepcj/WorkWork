import numpy as np

class TrainData:
    # data : feature
    # label : ans

    #训练数据，包括feature数据以及label数据
    def __init__(self, today, tomorrow):
        today.details = sorted(today.details, key=lambda a: a.dateTime);
        tomorrow.details = sorted(tomorrow.details, key=lambda a: a.dateTime);
        #使用lambda表达获取每分钟的数据变化
        self.data = list(map(lambda x: x.end / x.start - 1.0000000, today.details));
        # print(self.data);
        #获取第二日开盘数据变化幅度
        # self.label = [tomorrow.details[0].start / today.details[len(today.details) - 1].end - 1.0];
        self.label = [tomorrow.details[len(tomorrow.details) - 1].end / today.details[len(today.details) - 1].end - 1.0];



