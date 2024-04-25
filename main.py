import csv
normal_head = ['id', 'name', 'surname', 'height', 'weight', 'education', 'age']
data = []
data.append(normal_head)

with open('Архив/rus.csv') as file:
    reader = csv.reader(file, delimiter='#')
    heading = next(reader)
    head = dict()
    num = 0
    for i in heading:
        head[i] = num
        num += 1
    print(head)
    for row in reader:
        age = row[head[normal_head[6]]]
        if 26 < int(age) < 38:
            data.append(
                [row[head[normal_head[0]]],
                 row[head[normal_head[1]]],
                 row[head[normal_head[2]]],
                 row[head[normal_head[3]]],
                 row[head[normal_head[4]]],
                 row[head[normal_head[5]]],
                 age]
                 )


def sort_col(i):
    return i[1]


data.sort(key=sort_col)
for row in data:
    print(*row)

with open('result.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='#')
    writer.writerows(data)
