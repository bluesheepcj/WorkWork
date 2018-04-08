import Stock_Detail;
import Stock_Day;
# 一支股票的数据
class Stock_Stock:
    # code = '';
    # days = [];

    def __init__(self, iCode):
        self.code = iCode; #String
        self.days = []; #Stock_Day

    def Insert(self, iDetail):
        thisDay = [x for x in self.days if x.date == iDetail.dateTime.date()];
        if (len(thisDay) == 0):
            newDay = Stock_Day.Stock_Day(self.code, iDetail.dateTime.date());
            newDay.Insert(iDetail);
            self.days.append(newDay);
        else:
            thisDay[0].Insert(iDetail);
