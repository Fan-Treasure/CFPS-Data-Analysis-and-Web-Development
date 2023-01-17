import csv
import os


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        pass

    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass

    return False

num =2012
whole_path = 'F:/数据库数据/CPFS/CPFS数据/CPFS' + str(num) + '/数据'
for root, dirs, files in os.walk((whole_path)):
    print(root)
for m in range(len(files)):
    csv_name = whole_path + '/' + files[m]
    save_path = whole_path + '已清洗/' + files[m]
    with open(csv_name, "rt", encoding="gbk") as vsvfile:
        reader = csv.reader(vsvfile)
        rows = [row for row in reader]
    for i in range(len(rows)):
        for j in range(len(rows[0])):
            if (rows[i][j] == '不适用') | (rows[i][j] == '缺失') | (rows[i][j] == '不知道') | (rows[i][j] == '拒绝回答'):
                signal = 0
                for tm in range(len(rows)):
                    if (rows[tm][j] != '不适用') | (rows[tm][j] != '缺失') | (rows[tm][j] != '不知道'):
                        if (is_number(rows[tm][j])):
                            signal = 1
                if (signal == 1):
                    rows[i][j] = -1
                    print('(', i, j, ')has been changed')

    with open(save_path, 'w', encoding="gbk", newline='') as file:
        writer = csv.writer(file)
        for l in range(len(rows)):
            writer.writerow(rows[l])