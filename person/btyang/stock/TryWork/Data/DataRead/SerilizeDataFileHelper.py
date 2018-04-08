import pickle

def read(path):
    with open(path, 'rb') as f:
        data = pickle.load(f)
        return data;

def save(data,path):
    with open(path, 'wb') as f:
        pickle.dump(data, f)