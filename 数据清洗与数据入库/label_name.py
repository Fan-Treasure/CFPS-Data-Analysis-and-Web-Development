import csv
import os

for root, dirs, files in os.walk(("F:/数据库数据/CPFS/数据库标签")):
    print(root)
    print(dirs)
    print(files)
for i in range(len(files)):
    total_number = []
    csv_name = root+'/'+files[i]
    save_name = 'F:/数据库数据/CPFS/数据库标签整合/'+files[i]

    print(csv_name,save_name)
    with open(csv_name , 'rt' , encoding='gbk') as f :
        reader = csv.reader(f)
        rows = [row for row in reader]
    for j in range(len(rows)):
        data_split = rows[j][0].split(' ')
        used_label = [data_split[4],data_split[5]]
        total_number.append(used_label)
    with open(save_name , 'w', encoding="gbk", newline='') as file:
        writer = csv.writer(file)
        for l in range(len(total_number)):
            writer.writerow(total_number[l])


