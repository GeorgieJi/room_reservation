import pandas as pd
import numpy as np
from pandas import DataFrame
from sklearn import preprocessing


all_hotel_info = pd.read_csv('../intput/hotel_info(2769586).csv')
all_hotel_info.drop_duplicates('basicroomid', inplace=True)
all_hotel_info.set_index('basicroomid', inplace=True)
cut_area = all_hotel_info[['basic_minarea', 'basic_maxarea']]


def transfrom_arr_df(arr, col_name='col_'):
    if len(arr.shape) == 1:
        df = DataFrame(arr, columns=['col_0'])
    else:
        df = DataFrame(arr, columns=[col_name+str(i)
                                     for i in range(arr.shape[1])])
    return df


# 将一维数组转换为OHE码
def make_one_hot(names):
    data = []
    for name in names:
        data.append([name])
    enc = preprocessing.OneHotEncoder()
    enc.fit(data)
    one_hot_data = enc.transform(data).toarray()
    return one_hot_data


# del train1
test1 = pd.read_csv('../input/competition_extratime_test.txt', sep='\t',
                    index_col=['basicroomid_lastord'])
test1 = pd.merge(test1, cut_area, left_index=True, right_index=True,
                 how='left')
test1['rank_lastord_diff'] = test1['rank_lastord'] - test1['rank']
test1['returnvalue_ratio'] = test1['returnvalue'] / test1['price_deduct']
test1['price_avg'] = test1['price_deduct'] / test1['basic_minarea_x']
test1['user_avgpromotion_ratio'] = test1['user_avgpromotion'] \
                                   / test1['user_avgdealprice']
test1['user_area_ratio'] = (test1['basic_minarea_y']
                            + test1['basic_maxarea_y']) \
                           / (test1['basic_minarea_x']
                              + test1['basic_maxarea_x'])
test1['price_last_lastord_diff'] = test1['price_last_lastord'] \
                                   - test1['price_deduct']
test1['d1'] = test1['user_avgprice_star'] - test1['user_avgprice']
test1['basic_minarea_diff'] = test1['basic_minarea_y'] \
                              - test1['basic_minarea_x']
test1['basic_maxarea_diff'] = test1['basic_maxarea_y'] \
                              - test1['basic_maxarea_x']
test1['user_avgprice_diff'] = test1['user_avgprice'] - test1['price_deduct']
test1['user_price_diff'] = test1['user_maxprice'] - test1['user_minprice']
test1['user_avgprice_1week_diff'] = test1['user_avgprice_1week'] \
                                    - test1['price_deduct']
test1['user_price_1week_diff'] = test1['user_maxprice_1week'] \
                                 - test1['user_minprice_1week']
test1['user_ordernum2'] = np.log(test1['user_ordernum'])
test1['user_activation2'] = np.log(test1['user_activation'])
test1.reset_index(inplace=True)
test1['roomservice_4'].fillna(6, inplace=True)
roomservice_3 = transfrom_arr_df(make_one_hot(test1['roomservice_3']),
                                 'roomservice_3_')
test1 = test1.join(roomservice_3, how='left')
roomservice_4 = transfrom_arr_df(make_one_hot(test1['roomservice_4']),
                                 'roomservice_4_')
test1 = test1.join(roomservice_4, how='left')
roomservice_6 = transfrom_arr_df(make_one_hot(test1['roomservice_6']),
                                 'roomservice_6_')
test1 = test1.join(roomservice_6, how='left')
roomservice_8 = transfrom_arr_df(make_one_hot(test1['roomservice_8']),
                                 'roomservice_8_')
test1 = test1.join(roomservice_8, how='left')
test1['price_rank'] = test1['price_deduct'].groupby(test1['basicroomid'])\
    .rank(method='min')

test1['same_roomservice_2_lastord'] = (test1['roomservice_2']
                                       == test1['roomservice_2_lastord'])
test1['same_roomservice_3_lastord'] = (test1['roomservice_3']
                                       == test1['roomservice_3_lastord'])
test1['same_roomservice_4_lastord'] = (test1['roomservice_4']
                                       == test1['roomservice_4_lastord'])
test1['same_roomservice_5_lastord'] = (test1['roomservice_5']
                                       == test1['roomservice_5_lastord'])
test1['same_roomservice_6_lastord'] = (test1['roomservice_6']
                                       == test1['roomservice_6_lastord'])
test1['same_roomservice_8_lastord'] = (test1['roomservice_8']
                                       == test1['roomservice_8_lastord'])
test1['same_roomtag_2_lastord'] = (test1['roomtag_2']
                                   == test1['roomtag_2_lastord'])
test1['same_roomtag_3_lastord'] = (test1['roomtag_3']
                                   == test1['roomtag_3_lastord'])
test1['same_roomtag_4_lastord'] = (test1['roomtag_4']
                                   == test1['roomtag_4_lastord'])
test1['same_roomtag_5_lastord'] = (test1['roomtag_5']
                                   == test1['roomtag_5_lastord'])
test1['same_roomtag_6_lastord'] = (test1['roomtag_6']
                                   == test1['roomtag_6_lastord'])
test1['same_star_lastord'] = (test1['star'] == test1['star_lastord'])
test1.to_csv('../output/competition_test_new.csv')
