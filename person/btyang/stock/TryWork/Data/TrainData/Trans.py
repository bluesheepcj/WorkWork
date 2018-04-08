import numpy as np;

def TrainData2ndarray(trainData):
    featureData = np.zeros((1, 240));
    label = np.zeros((1, 1));
    for data in trainData:
        featureData = np.append(featureData, [data.data], axis=0);
        label = np.append(label, [data.label], axis=0);
    featureData = np.delete(featureData, 0, 0);
    label = np.delete(label, 0, 0);
    return featureData, label;


def TrainData2ndarray_2(trainData):
    featureData = np.zeros((1, 240));
    label = np.zeros((1, 2));
    for data in trainData:
        featureData = np.append(featureData, [data.data], axis=0);
        label = np.append(label, [[-data.label[0] * 10, data.label[0] * 10]], axis=0);

        # if data.label[0] > 0:
        #     label = np.append(label,[[0,1]],axis=0);
        # else:
        #     label = np.append(label,[[1,0]],axis=0);


        # labelData = np.append(label, [data.label], axis=0);

    featureData = np.delete(featureData, 0, 0);
    label = np.delete(label, 0, 0);
    return featureData, label;