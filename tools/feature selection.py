import pandas as pd
from sklearn.ensemble import RandomForestClassifier
train = pd.read_csv('/home/hyf/Desktop/数据集&数据说明/competition_test_10%_new.csv')
train = train[:100000]
use_col = train.columns
n_use = ['Unnamed: 0','index','roomid','roomid_lastord','hotelid_lastord','orderid_lastord', 'orderdate_lastord','orderid', 'uid', 'orderdate', 'hotelid', 'basicroomid']
# use_col_X = [x for x in use_col if x not in n_use]
use_col_X = [x for x in use_col if x not in n_use]
print(use_col_X)
X = train[use_col_X]
X.fillna(-1,inplace=True)
Y = train['orderlabel']
names = use_col_X
rf = RandomForestClassifier(n_jobs=-1,random_state=14)
rf.fit(X, Y)
print ("Features sorted by their score:")
a =sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names),
          reverse=True)
file=open('/home/hyf/Desktop/数据集&数据说明/log3.txt','w')
file.write(str(a));
file.close()
# a.to_csv('/home/nil/ctrip_room/subset_noclean/log.csv')
print (sorted(zip(map(lambda x: round(x, 4), rf.feature_importances_), names),
              reverse=True))