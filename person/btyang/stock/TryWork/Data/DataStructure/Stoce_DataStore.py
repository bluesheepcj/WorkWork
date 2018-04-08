import datetime as DateTime;
import Stock_Detail;
import Stock_Stock;
import sys;
sys.path.append("../TrainData/")
import TrainData;


class Stock_DataStore:
    #Stock_Stock
    stocks=[];

    #插入数据
    def Insert(self,iStockCode,iStrDetail):
        strDatetime = iStrDetail[0]+' '+iStrDetail[1];
        datetime = DateTime.datetime.strptime(strDatetime, '%Y/%m/%d %H:%M');
        start=float(iStrDetail[2]);
        max=float(iStrDetail[3]);
        min=float(iStrDetail[4]);
        end=float(iStrDetail[5]);
        count=float(iStrDetail[6]);
        amount=float(iStrDetail[7]);
        stockDetail = Stock_Detail.Stock_Detail(iStockCode,datetime,start,max,min,end,count,amount);

        thisStock = [x for x in self.stocks if x.code == iStockCode];
        if(len(thisStock)==0):
            newStock = Stock_Stock.Stock_Stock(iStockCode);
            newStock.Insert(stockDetail);
            self.stocks.append(newStock);
        else:
            thisStock[0].Insert(stockDetail);

    #根据日期获取可用的数据
    def getTrainData(self,dateStart = DateTime.datetime.strptime("1980/01/01", '%Y/%m/%d').date(),dateEnd=DateTime.date.today()):
        trainData = [];
        #stock by stock取数
        for stock in self.stocks:
            stock.days = sorted(stock.days, key=lambda day: day.date);
            #使用index一天天取数
            for index in range(len(stock.days)-1):
                if stock.days[index].date >= dateStart and stock.days[index].date < dateEnd:#取在时间范围内的数据
                    oneTrain = TrainData.TrainData(stock.days[index],stock.days[index+1]);
                    if(len(oneTrain.data) == 240):
                        trainData.append(oneTrain);
        return trainData;

