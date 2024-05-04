import csv
from operator import itemgetter
normal_head = ['id', 'name', 'surname', 'height', 'weight', 'education', 'age']
data = []
files = ['ita.csv', 'us.csv', 'ger.csv', 'rus.csv']


def reasor_file(file):
    """Read and Sort the file"""
    with open(file) as file:
        reader = csv.reader(file, delimiter='#')
        heading = next(reader)
        head = dict()
        num = 0
        for i in heading:
            head[i] = num
            num += 1
        for row in reader:
            id = row[head[normal_head[0]]]
            name = row[head[normal_head[1]]]
            surname = row[head[normal_head[2]]]
            height = row[head[normal_head[3]]]
            weight = row[head[normal_head[4]]]
            education = row[head[normal_head[5]]]
            age = row[head[normal_head[6]]]
            english_language = row[head['english_language']]
            eyesight = row[head['eyesight']]

            if (20 <= int(age) <= 59) and (150 <= int(height) <= 190):
                if (50 <= int(weight) <= 90) and (float(eyesight) == 1.0):
                    if education == 'Master' or education == 'PhD':
                        if english_language == 'true':
                            data.append(
                                [id,
                                 name,
                                 surname,
                                 height,
                                 weight,
                                 education,
                                 age]
                                 )


for file in files:
    reasor_file(file)
data = sorted(data, key=itemgetter(1, 2))
priority_age = []
remaining = []
for row in data:
    if 27 <= int(row[6]) <= 37:
        priority_age.append(row)
    else:
        remaining.append(row)


for row in data:
    print(*row)
    
with open('result.csv', mode='w', encoding='utf-8') as file:
    writer = csv.writer(file, delimiter='#')
    writer.writerows(data)
