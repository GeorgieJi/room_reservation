import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn import preprocessing
from sklearn.preprocessing import OneHotEncoder
all = pd.read_csv('/home/hyf/Desktop/数据集&数据说明/hotel_info(2769586).csv')
all.drop_duplicates('basicroomid',inplace=True)
all.set_index('basicroomid',inplace=True)
cut_area = all[['basic_minarea','basic_maxarea']]

def transfrom_Arr_DF(arr,col_name = 'col_'):
    if(len(arr.shape)==1):
        df = DataFrame(arr,columns=['col_0'])
    else:
        df = DataFrame(arr,columns=[col_name+str(i) for i in range(arr.shape[1])])
    return df

'''将一维数组转换为OHE码'''
def make_OHE(names):
    data = []
    for name in names:
        data.append([name])
    enc = preprocessing.OneHotEncoder()
    enc.fit(data)
    OHE_data = enc.transform(data).toarray()
    return OHE_data

# train1 = pd.read_csv('/home/hyf/Desktop/数据集&数据说明/competition_train_50%.csv',index_col=['basicroomid_lastord'])
# # train1 = pd.read_csv('/opt/ctrip/competition_test_3.csv',index_col=['basicroomid_lastord'])
# train1 = pd.merge(train1,cut_area,left_index=True,right_index=True,how='left')
# train1['day'] = train1['orderdate']
# train1['rank_lastord_diff'] = train1['rank_lastord'] - train1['rank']
# train1['returnvalue_ratio'] = train1['returnvalue'] / train1['price_deduct']
# train1['price_avg'] = train1['price_deduct'] / train1['basic_minarea_x']
# train1['user_avgpromotion_ratio'] = train1['user_avgpromotion'] / train1['user_avgdealprice']
# train1['user_area_ratio'] = (train1['basic_minarea_y'] + train1['basic_maxarea_y'])/(train1['basic_minarea_x'] + train1['basic_maxarea_x'])
# # train1['price_avg_last'] = train1['price_last_lastord'] / train1['basic_minarea_y']
# # train1['user_ordnum_ratio1'] = train1['user_ordnum_1week'] / train1['user_ordnum_1month']
# # train1['user_avgprice_ratio'] = train1['price_deduct'] / train1['user_avgprice']
# # train1['user_ordnum_1week_ratio'] = train1['user_ordnum_1week'] / train1['user_ordernum']
# # train1['user_ordnum_1month_ratio'] = train1['user_ordnum_1month'] / train1['user_ordernum']
# train1['price_last_lastord_diff'] = train1['price_last_lastord'] - train1['price_deduct']
# # train1['basic_area_x_diff'] = train1['basic_maxarea_x'] - train1['basic_minarea_x']
# # train1['basic_area_y_diff'] = train1['basic_maxarea_y'] - train1['basic_minarea_y']
# # train1['user_avgroomarea_diff'] = train1['user_avgprice'] / train1['user_avgroomarea']
# train1['d1'] = train1['user_avgprice_star'] - train1['user_avgprice']
# train1['basic_minarea_diff'] = train1['basic_minarea_y'] - train1['basic_minarea_x']
# train1['basic_maxarea_diff'] = train1['basic_maxarea_y'] - train1['basic_maxarea_x']
# train1['user_avgprice_diff'] = train1['user_avgprice'] - train1['price_deduct']
# # train1['user_maxprice_diff'] = train1['user_maxprice'] - train1['price_deduct']
# # train1['user_minprice_diff'] = train1['user_minprice'] - train1['price_deduct']
# train1['user_price_diff'] = train1['user_maxprice'] - train1['user_minprice']
# # train1['user_avgprice_max'] = train1['user_maxprice'] - train1['user_avgprice']
# # train1['user_avgprice_min'] = train1['user_minprice'] - train1['user_avgprice']
# # train1['user_avgprice_star_diff'] = train1['user_avgprice_star'] - train1['price_deduct']
# # train1['return_lastord_ratio'] = train1['return_lastord'] / train1['price_last_lastord']
# train1['user_avgprice_1week_diff'] = train1['user_avgprice_1week'] - train1['price_deduct']
# train1['user_price_1week_diff'] = train1['user_maxprice_1week'] - train1['user_minprice_1week']
# train1['user_ordernum2'] = np.log(train1['user_ordernum'])
# train1['user_activation2'] = np.log(train1['user_activation'])
# train1.reset_index(inplace=True)
# train1['roomservice_4'].fillna(6,inplace=True)
# roomservice_3 = transfrom_Arr_DF(make_OHE(train1['roomservice_3']),'roomservice_3_')
# train1 = train1.join(roomservice_3,how='left')
# roomservice_4 = transfrom_Arr_DF(make_OHE(train1['roomservice_4']),'roomservice_4_')
# train1 = train1.join(roomservice_4,how='left')
# roomservice_6 = transfrom_Arr_DF(make_OHE(train1['roomservice_6']),'roomservice_6_')
# train1 = train1.join(roomservice_6,how='left')
# roomservice_8 = transfrom_Arr_DF(make_OHE(train1['roomservice_8']),'roomservice_8_')
# train1 = train1.join(roomservice_8,how='left')
# train1['price_rank'] = train1['price_deduct'].groupby(train1['basicroomid']).rank(method='min')
# # roomtag_2 = train1.groupby(['roomtag_2','orderlabel']).size()
# # roomtag_2 = pd.DataFrame(roomtag_2)
# # roomtag_2.columns = ['count']
# # roomtag_2.reset_index(inplace=True)
# # roomtag_2 = pd.merge(roomtag_2,roomtag_2.groupby(['orderlabel'])[['count']].sum(),left_on='orderlabel',right_index=True)
# # roomtag_2['roomtag_2_ratio'] = roomtag_2['count_x']/roomtag_2['count_y']
# # del roomtag_2['orderlabel']
# # train1 = pd.merge(train1,roomtag_2,left_on=['roomtag_2'],right_on=['roomtag_2'],how='left')
# train1['same_roomservice_2_lastord'] = (train1['roomservice_2'] == train1['roomservice_2_lastord'])
# train1['same_roomservice_3_lastord'] = (train1['roomservice_3'] == train1['roomservice_3_lastord'])
# train1['same_roomservice_4_lastord'] = (train1['roomservice_4'] == train1['roomservice_4_lastord'])
# train1['same_roomservice_5_lastord'] = (train1['roomservice_5'] == train1['roomservice_5_lastord'])
# train1['same_roomservice_6_lastord'] = (train1['roomservice_6'] == train1['roomservice_6_lastord'])
# train1['same_roomservice_8_lastord'] = (train1['roomservice_8'] == train1['roomservice_8_lastord'])
# train1['same_roomtag_2_lastord'] = (train1['roomtag_2'] == train1['roomtag_2_lastord'])
# train1['same_roomtag_3_lastord'] = (train1['roomtag_3'] == train1['roomtag_3_lastord'])
# train1['same_roomtag_4_lastord'] = (train1['roomtag_4'] == train1['roomtag_4_lastord'])
# train1['same_roomtag_5_lastord'] = (train1['roomtag_5'] == train1['roomtag_5_lastord'])
# train1['same_roomtag_6_lastord'] = (train1['roomtag_6'] == train1['roomtag_6_lastord'])
#
# train1['same_star_lastord'] = (train1['star'] == train1['star_lastord'])
#
# # train1.to_csv('/opt/ctrip/competition_test_3_new.csv')
# train1.to_csv('/home/hyf/Desktop/数据集&数据说明/competition_train_50%_new.csv')

# del train1

test1 = pd.read_csv('/home/hyf/Desktop/数据集&数据说明/competition_extratime_test.txt',sep='\t',index_col=['basicroomid_lastord'])
# for i in range(1,8):
#     i = str(i)
#     print('strat '+i+' make')
#     test1 = pd.read_csv('/opt/ctrip/competition_test_side'+i+'.txt',sep='\t')
#     test1.set_index('basicroomid_lastord',inplace=True)
#
#     print('read data --- complete')
test1 = pd.merge(test1,cut_area,left_index=True,right_index=True,how='left')
test1['rank_lastord_diff'] = test1['rank_lastord'] - test1['rank']
test1['returnvalue_ratio'] = test1['returnvalue'] / test1['price_deduct']
test1['price_avg'] = test1['price_deduct'] / test1['basic_minarea_x']
test1['user_avgpromotion_ratio'] = test1['user_avgpromotion'] / test1['user_avgdealprice']
test1['user_area_ratio'] = (test1['basic_minarea_y'] + test1['basic_maxarea_y'])/(test1['basic_minarea_x'] + test1['basic_maxarea_x'])
# test1['price_avg_last'] = test1['price_last_lastord'] / test1['basic_minarea_y']
# test1['user_ordnum_ratio1'] = test1['user_ordnum_1week'] / test1['user_ordnum_1month']
# test1['user_avgprice_ratio'] = test1['price_deduct'] / test1['user_avgprice']
# test1['user_ordnum_1week_ratio'] = test1['user_ordnum_1week'] / test1['user_ordernum']
# test1['user_ordnum_1month_ratio'] = test1['user_ordnum_1month'] / test1['user_ordernum']
test1['price_last_lastord_diff'] = test1['price_last_lastord'] - test1['price_deduct']
# test1['basic_area_x_diff'] = test1['basic_maxarea_x'] - test1['basic_minarea_x']
# test1['basic_area_y_diff'] = test1['basic_maxarea_y'] - test1['basic_minarea_y']
# test1['user_avgroomarea_diff'] = test1['user_avgprice'] / test1['user_avgroomarea']
test1['d1'] = test1['user_avgprice_star'] - test1['user_avgprice']
test1['basic_minarea_diff'] = test1['basic_minarea_y'] - test1['basic_minarea_x']
test1['basic_maxarea_diff'] = test1['basic_maxarea_y'] - test1['basic_maxarea_x']
test1['user_avgprice_diff'] = test1['user_avgprice'] - test1['price_deduct']
# test1['user_maxprice_diff'] = test1['user_maxprice'] - test1['price_deduct']
# test1['user_minprice_diff'] = test1['user_minprice'] - test1['price_deduct']
test1['user_price_diff'] = test1['user_maxprice'] - test1['user_minprice']
# test1['user_avgprice_max'] = test1['user_maxprice'] - test1['user_avgprice']
# test1['user_avgprice_min'] = test1['user_minprice'] - test1['user_avgprice']
# test1['user_avgprice_star_diff'] = test1['user_avgprice_star'] - test1['price_deduct']
# test1['return_lastord_ratio'] = test1['return_lastord'] / test1['price_last_lastord']
test1['user_avgprice_1week_diff'] = test1['user_avgprice_1week'] - test1['price_deduct']
test1['user_price_1week_diff'] = test1['user_maxprice_1week'] - test1['user_minprice_1week']
test1['user_ordernum2'] = np.log(test1['user_ordernum'])
test1['user_activation2'] = np.log(test1['user_activation'])
test1.reset_index(inplace=True)
test1['roomservice_4'].fillna(6,inplace=True)
roomservice_3 = transfrom_Arr_DF(make_OHE(test1['roomservice_3']),'roomservice_3_')
test1 = test1.join(roomservice_3,how='left')
roomservice_4 = transfrom_Arr_DF(make_OHE(test1['roomservice_4']),'roomservice_4_')
test1 = test1.join(roomservice_4,how='left')
roomservice_6 = transfrom_Arr_DF(make_OHE(test1['roomservice_6']),'roomservice_6_')
test1 = test1.join(roomservice_6,how='left')
roomservice_8 = transfrom_Arr_DF(make_OHE(test1['roomservice_8']),'roomservice_8_')
test1 = test1.join(roomservice_8,how='left')
test1['price_rank'] = test1['price_deduct'].groupby(test1['basicroomid']).rank(method='min')
# test1 = pd.merge(test1,roomtag_2,left_on=['roomtag_2'],right_on=['roomtag_2'],how='left')


test1['same_roomservice_2_lastord'] = (test1['roomservice_2'] == test1['roomservice_2_lastord'])
test1['same_roomservice_3_lastord'] = (test1['roomservice_3'] == test1['roomservice_3_lastord'])
test1['same_roomservice_4_lastord'] = (test1['roomservice_4'] == test1['roomservice_4_lastord'])
test1['same_roomservice_5_lastord'] = (test1['roomservice_5'] == test1['roomservice_5_lastord'])
test1['same_roomservice_6_lastord'] = (test1['roomservice_6'] == test1['roomservice_6_lastord'])
test1['same_roomservice_8_lastord'] = (test1['roomservice_8'] == test1['roomservice_8_lastord'])
test1['same_roomtag_2_lastord'] = (test1['roomtag_2'] == test1['roomtag_2_lastord'])
test1['same_roomtag_3_lastord'] = (test1['roomtag_3'] == test1['roomtag_3_lastord'])
test1['same_roomtag_4_lastord'] = (test1['roomtag_4'] == test1['roomtag_4_lastord'])
test1['same_roomtag_5_lastord'] = (test1['roomtag_5'] == test1['roomtag_5_lastord'])
test1['same_roomtag_6_lastord'] = (test1['roomtag_6'] == test1['roomtag_6_lastord'])

test1['same_star_lastord'] = (test1['star'] == test1['star_lastord'])

test1.to_csv('/home/hyf/Desktop/数据集&数据说明/competition_test_new.csv')

    # test1.to_csv('/opt/ctrip/competition_test_side'+i+'_new.csv',index=False)



