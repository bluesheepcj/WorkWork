import datetime as DateTime;

# 一支股票一天的数据
class Stock_Day:
    # stockCode = "";
    # date = DateTime.date.today();
    # details = [];

    #构造函数
    def __init__(self, iStockCode, iDate):
        self.stockCode = iStockCode;#String
        self.date = iDate; #date,iDetail.dateTime.date()
        self.details = []; #Stock_Detail

    #插入数据
    def Insert(self,iDetail):
        thisDetail = [a for a in self.details if a.dateTime == iDetail.dateTime];
        if(len(thisDetail)==0):
            self.details.append(iDetail);