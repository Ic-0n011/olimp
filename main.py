import csv
from operator import itemgetter
from os import system
data = []


def user_input() -> list:
    """Даём пользователю выбрать файлы"""
    files_name = []
    text = ['  Программа собирает информацию из таблиц(ы) и сортирует ее по следующим критериям:',
        '       1) по возрасту: от 20 до 59 лет',
        '       2) по росту: от 150 до 190 см',
        '       3) по весу: от 50 до 90',
        '       4) по зрению: 1.0',
        '       5) по знанию английского: true',
        '  Данная программа поддерживает только csv формат, с другими форматами программа может работать не коректно',
        'файл сохраниться в ту же дерикторию где сейчас находится данная программа, и будет называться > result.csv <',
        '',
        'Напишите имя файла без расширения и нажмите  > Enter < , если файлов несколько то повторите, иначе > Enter < без ввода:',]
    while True:
        system('cls')
        for st in text:
            print(st)
        if files_name:
            print(f'Выбранные файлы: {" ".join(str(i) for i in files_name)}')
        file_name = input()
        if file_name:
            files_name.append(file_name+'.csv')
        else:
            break
    return files_name


def reasor_file(file) -> None:
    """Открывает файл и отсеивает информацию, которую после сохраняет в > data <"""
    normal_head = ['id', 'name', 'surname', 'height', 'weight', 'education', 'age']
    try:
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
    except FileNotFoundError:
        print("Такой файл не найден, убедитесь что имя файла верное и повторите попытку.")
        print(f'Файлы которые вы вписали - {" ".join(str(i) for i in files_name)}')


files_name = user_input()
if files_name:
    """ищет и открывает файлы которые указал пользователь"""
    for file_name in files_name:
        reasor_file(file_name)

    """сортировка данных по имени"""
    data = sorted(data, key=itemgetter(1, 2))

    """Разделяет data для дальнейшей сортировки по возрасту"""
    priority_age = []
    remaining = []
    for row in data:
        if 27 <= int(row[6]) <= 37:
            priority_age.append(row)
        else:
            remaining.append(row)
    data = priority_age + remaining

    """создание новых порядковых номеров для кандидатов"""
    for index, candidate in enumerate(data, start=1):
        candidate[0] = index

    """сохранение полученного результата в файл result.csv"""
    with open('result.csv', mode='w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter='#')
        writer.writerows(data)
else:
    print('Пользователь ничего не указал')