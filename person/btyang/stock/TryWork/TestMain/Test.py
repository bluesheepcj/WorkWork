import numpy as np

import re

# 将正则表达式编译成Pattern对象
pattern = re.compile(r'(SH[\w\W]+)\.csv')
# pattern = re.compile(r'ˆSH')

# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
match = pattern.match('SHfjdfj984r3.csv')

if match:
    # 使用Match获得分组信息
    print(match.group(1));

### 输出 ###
# hello

mat = np.zeros((1,3));
mat=mat+1;
print(mat[0][0])
a=[1.0,2.0,3.0];
print(mat);
print(a);
featureData=np.append(mat,[a],axis=0);
featureData=np.append(mat,[a],axis=0);
featureData=np.append(featureData,[a],axis=0);
print(featureData)
print(featureData[0:int(len(featureData)*0.7)])
print(len(featureData))