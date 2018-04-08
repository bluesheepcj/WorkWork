from abc import ABCMeta, abstractmethod

import datetime as DateTime;

from InterfaceData import InterfaceData
import pandas as pd
import tensorflow as tf
import os;
import re;
import random

import DataRead.ReadFromCsvOneMin as read;
import Trans;
from Stoce_DataStore import Stock_DataStore

class TestData(InterfaceData):
    def GetData(self):
        print("Log:TestData GetData")
        # path="../../resource/dataSource";
        path="/Users/yangbotian/Downloads/股票2003.1-2003.6一分钟csv";
        stockStore = read.getData(path,idx=50,randomArg=1);

        #从对象里获取训练和测试数据
        trainPart = stockStore.getTrainData(dateEnd=DateTime.datetime.strptime("2003/06/20", '%Y/%m/%d').date());
        testPart = stockStore.getTrainData(dateStart=DateTime.datetime.strptime("2003/06/20", '%Y/%m/%d').date());
        # featureData, labelData = self.TrainData2ndarray_2(AllTrainAndLabelData);
        trainFeatureData, trainLabelData = Trans.TrainData2ndarray_2(trainPart);
        testFeatureData, testLabelData = Trans.TrainData2ndarray_2(testPart);

        x = tf.placeholder(tf.float32, [None, 240])
        W = tf.Variable(tf.random_normal([240, 2]))
        b = tf.Variable(tf.random_normal([2]))
        y = tf.nn.softmax(tf.matmul(x, W) + b)
        y_ = tf.placeholder("float", [None, 2])
        cross_entropy = -tf.reduce_sum(y_ * tf.log(y))
        train_step = tf.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)

        init = tf.initialize_all_variables()

        with tf.Session() as sess:
            sess.run(init);
            for i in range(10000):
                # batch_xs = featureData[:int(len(featureData) * 0.9)]
                # batch_ys = labelData[:int(len(labelData) * 0.9)]
                batch_xs = trainFeatureData
                batch_ys = trainLabelData
                sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})
            correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
            # correct_prediction = tf.mul(y,y_) > 0;
            # tf.cond(tf.mul(y,y_) > 0,lambda: true,lambda: false);
            # correct_prediction = tf.where((y[0]>0.0 and y_[0]>0.0) or (y[0]<=0.0 and y_[0]<=0.0),1,0);
            accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
            # test_batch_xs = featureData[int(len(featureData) * 0.9):]
            # test_batch_ys = labelData[int(len(labelData) * 0.9):]
            test_batch_xs = testFeatureData
            test_batch_ys = testLabelData
            print(sess.run(accuracy, feed_dict={x: test_batch_xs, y_: test_batch_ys}))

        endTemp = 1;


