import datetime as DateTime;

# 股票数据的细节数据
class Stock_Detail:
    # code = '';
    # dateTime = DateTime.datetime.today();
    # start = 0.0;
    # max = 0.0;
    # min = 0.0;
    # end = 0.0;
    # count = 0.0;
    # amount = 0.0;

    def __init__(self, iCode, iTime, iStart, iMax, iMin, iEnd, iCount, iAmount):
        self.code = iCode;
        self.dateTime = iTime;
        self.start = iStart;
        self.max = iMax;
        self.min = iMin;
        self.end = iEnd;
        self.count = iCount;
        self.amount = iAmount;
