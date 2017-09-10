import random as rd


if __name__ == '__main__':
    file = open('../input/competition_test_new.csv')
    out_3 = open('../input/online_competition_test_50%.csv', 'w')
    out_t3 = open('../input/online_competition_train_50%.csv', 'w')
    line_num = 0
    current_orderid = ''
    deal_list = []
    header = file.readline().split(',')
    out_3.write(','.join(header))
    out_t3.write(','.join(header))

    for line in file:
        line_num += 1
        print(line_num)
        li = line.split('\t')
        if current_orderid == li[0] or line_num == 1:
            deal_list.append(','.join(li))
        else:
            rdnum = rd.randint(1, 10)
            # 10%
            if rdnum > 9:
                for item in deal_list:
                    print()
            else:
                for item in deal_list:
                    print()
                    # 30%
            if rdnum > 7:
                for item in deal_list:
                    print()
            else:
                for item in deal_list:
                    print()
            # 50%
            if rdnum > 5:
                for item in deal_list:
                    out_3.write(item)
            else:
                for item in deal_list:
                    out_t3.write(item)
            deal_list.clear()
            deal_list.append(','.join(li))
            current_orderid = li[0]
    rdnum = rd.randint(1, 10)
    # 10%
    if rdnum > 9:
        for item in deal_list:
            print()
    else:
        for item in deal_list:
            print()
            # 30%
    if rdnum > 7:
        for item in deal_list:
            print()
    else:
        for item in deal_list:
            print()
    # 50%
    if rdnum > 5:
        for item in deal_list:
            out_3.write(item)
    else:
        for item in deal_list:
            out_t3.write(item)
    out_3.close()
    out_t3.close()
