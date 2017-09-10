import pandas as pd


use_ = 'hotelid,basicroomid,roomid,rank,returnvalue,price_deduct,' \
      'basic_minarea,basic_maxarea,roomservice_1,roomservice_2,' \
      'roomservice_3,roomservice_4,roomservice_5,roomservice_6,' \
      'roomservice_7,roomservice_8,roomtag_1,roomtag_2,roomtag_3,roomtag_4,' \
      'roomtag_5,roomtag_6'.split(',')
df = pd.read_csv('../input/competition_train_50%.csv',
                 usecols=use_)
df.drop_duplicates('roomid', inplace=True)
df.to_csv('../output/hotel_info(2769586).csv')
