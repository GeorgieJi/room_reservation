import random as rd
if __name__ == '__main__':
    file = open('/home/hyf/Desktop/数据集&数据说明/competition_test_new.csv')
    # out_1 = open('/home/hyf/Desktop/数据集&数据说明/online_competition_test_10%.csv', 'w')
    # out_t1 = open('/home/hyf/Desktop/数据集&数据说明/online_competition_train_90%.csv', 'w')
    # out_2 = open('/home/hyf/Desktop/数据集&数据说明/online_competition_test_30%.csv', 'w')
    # out_t2 = open('/home/hyf/Desktop/数据集&数据说明/online_competition_train_70%.csv', 'w')
    out_3 = open('/home/hyf/Desktop/数据集&数据说明/online_competition_test_50%.csv', 'w')
    out_t3 = open('/home/hyf/Desktop/数据集&数据说明/online_competition_train_50%.csv', 'w')
    line_num = 0
    current_orderid = ''
    deal_list = []

    header = file.readline().split(',')
    # offline_1.write(','.join(header))
    # out_1.write(','.join(header))
    # out_2.write(','.join(header))
    out_3.write(','.join(header))
    # out_t1.write(','.join(header))
    # out_t2.write(','.join(header))
    out_t3.write(','.join(header))

    for line in file:
        line_num+=1
        print(line_num)
        li = line.split('\t')
        if current_orderid == li[0] or line_num ==1:
            deal_list.append(','.join(li))
        else:
            rdnum = rd.randint(1, 10)
            # # 10%
            if rdnum > 9:
                for item in deal_list:
                    print()
                    # out_1.write(item)
            else:
                for item in deal_list:
                    print()
                    # out_t1.write(item)
                    # 30%
            if rdnum > 7:
                for item in deal_list:
                    print()
                    # out_2.write(item)
            else:
                for item in deal_list:
                    print()
                    # out_t2.write(item)
            # 50%
            if rdnum > 5:
                for item in deal_list:
                    out_3.write(item)
            else:
                for item in deal_list:
                    out_t3.write(item)
            deal_list = []
            deal_list.append(','.join(li))
            current_orderid = li[0]
    rdnum = rd.randint(1, 10)
    # 10%
    if rdnum > 9:
        for item in deal_list:
            print()
            # out_1.write(item)
    else:
        for item in deal_list:
            print()
            # out_t1.write(item)
            # 30%
    if rdnum > 7:
        for item in deal_list:
            print()
            # out_2.write(item)
    else:
        for item in deal_list:
            print()
            # out_t2.write(item)
    # 50%
    if rdnum > 5:
        for item in deal_list:
            out_3.write(item)
    else:
        for item in deal_list:
            out_t3.write(item)
    # out_1.close()
    # out_2.close()
    out_3.close()
    # out_t1.close()
    # out_t2.close()
    out_t3.close()


