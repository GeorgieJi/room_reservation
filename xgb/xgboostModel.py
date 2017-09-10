import pandas as pd
import datetime as dt
from xgboost import XGBClassifier
from sklearn.externals import joblib


def new_feature(set_):
    set_['sort_price'] \
        = set_['price_deduct'].groupby(set_['orderid']).rank(method='min')
    set_['ave_area'] \
        = (set_['basic_minarea_x'].astype('float32')
           + set_['basic_maxarea_x'].astype('float32'))/2
    set_['sort_area'] \
        = set_['ave_area'].groupby(set_['orderid']).rank(method='min')
    set_['sort_rv'] \
        = set_['returnvalue'].groupby(set_['orderid']).rank(method='min')
    return set_


def getscore2(pre_file, true_file):
    true_df = pd.read_csv(true_file, usecols=['orderid', 'roomid',
                                              'orderlabel'])
    temp = true_df[true_df['orderlabel'] == 1]
    true_df = pd.concat([temp.orderid, temp.roomid], axis=1)
    pre_df = pd.read_csv(pre_file)

    temp = pd.merge(true_df, pre_df, how='left', on='orderid')
    true_num = temp[temp.predict_roomid == temp.roomid].shape[0]
    score = (true_num/true_df.shape[0])
    print(true_num, true_df.shape[0], score)
    return score


def train_model(train_set_dir, model_path, use_col):
    print(use_col)
    train_x = pd.read_csv(train_set_dir, usecols=use_col)
    train_x = new_feature(train_x)
    print(train_x.head())
    classifier = XGBClassifier(max_depth=8, learning_rate=0.01,
                               n_estimators=3200, reg_alpha=0.07,
                               reg_lambda=0.5, objective='binary:logistic',
                               scale_pos_weight=36)
    train_y = pd.DataFrame(train_x.orderlabel)
    del train_x['orderlabel']
    print('readed train_set')
    train_x = train_x.iloc[:, 6:].astype(float)
    classifier.fit(train_x, train_y)
    print('train over')
    joblib.dump(classifier, model_path)
    print('model saved')


def predict_model_new(test_path, model_path, use_col_test, result_path, sep_):
    test_set = pd.read_csv(test_path, usecols=use_col_test, sep=sep_)
    test_set = new_feature(test_set)
    model = joblib.load(model_path)
    print(model.get_params())
    print('predicting...')
    res = model.predict_proba(test_set.iloc[:, 6:])
    res = pd.DataFrame(res, columns=['P_0', 'P_1'])
    res = pd.DataFrame(pd.concat([test_set.orderid, test_set.roomid, res.P_1],
                                 axis=1))
    del test_set
    print('Analysis!!!')
    grouped = res.groupby('orderid')
    result_file = []
    for group_name, group in grouped:
        group = group.set_index('roomid')
        roomid = group['P_1'].argmax()
        result_file.append([group_name, roomid])
    pd.DataFrame(result_file, columns=['orderid', 'predict_roomid'])\
        .to_csv(result_path, index=False)


if __name__ == '__main__':
    f = open('../log3.txt', 'r')
    lines = f.readlines()
    t = lines[0]
    t = eval(t)
    str_column_name \
        = 'orderid,uid,orderdate,hotelid,basicroomid,roomid,orderlabel'\
        .split(',')
    for i in t:
        if i[0] != 0:
            str_column_name.append(i[1])
    lis_column_name = [x for x in str_column_name if x not in ['orderlabel']]
    str_model_path = '../models/XGB_F_W_H_8_3200_0.01.model'
    # online test
    str_result_path = '../output/onLine_XGB_8_0.01_3200_two.csv'
    str_test_set_path = '../output/online_competition_train_50%.csv'
    str_split_token = ','
    predict_begin = dt.datetime.now()
    print('Predict:' + str_model_path)
    predict_model_new(str_test_set_path, str_model_path, lis_column_name,
                      str_result_path, str_split_token)
    predict_end = dt.datetime.now()
    print(predict_end-predict_begin)
