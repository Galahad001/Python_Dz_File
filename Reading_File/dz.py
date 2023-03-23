''' 1 Дано два текстовых файла. Выяснить, совпадают ли
их строки. Если нет, то вывести несовпадающую строку
из каждого файла.
'''
def dz_1():
    fileRead_0 = open('Reading_File/text_1.txt', encoding="utf-8")
    fileRead_1 = open('Reading_File/text_2.txt', encoding="utf-8")

    read_0 = fileRead_0.read()
    read_1 = fileRead_1.read()

    # print(read_0)
    # print(read_1)

    if  read_0 == read_1:
        print("Значения совпадают")
    else:
        print(f"Значения не совпадают: \n{read_0}\n{read_1}")

    fileRead_0.close()
    fileRead_1.close()

print("=" * 15, '1', "=" * 15)

'''Дан текстовый файл. Необходимо создать новый файл
и записать в него следующую статистику по исходному
файлу:
-Количество символов;
-Количество строк;
-Количество гласных букв;
-Количество согласных букв;
-Количество цифр.'''

def dz_2():
    fileRead_2 = open("Reading_File/text_7.txt", encoding="utf-8")
    read_2 = fileRead_2.readlines()

    read_2_1 = "".join(read_2)
    print(read_2_1)

    info_0 = f"Количество элементов: {len(read_2_1)}\n"
    info_1 = f"Количество гласных букв: {sum(read_2_1.count(x) for x in ('ауоыиэяюёе'))}\n"
    info_2 = f"Количество согласных букв: {sum(read_2_1.count(x) for x in ('бвгджзйклмнпрстфхцчшщ'))}\n"
    info_3 = f"Количество цифр: {sum(read_2_1.count(x) for x in ('1234567890'))}\n"
    info_4 = f"Количество строк: {len(read_2)}\n"

    with open('Reading_File/text_10.txt', 'w', encoding='utf-8') as fileWrite_2:
        fileWrite_2.write(info_0)
        fileWrite_2.write(info_1)
        fileWrite_2.write(info_2)
        fileWrite_2.write(info_3)
        fileWrite_2.write(info_4)

    print(f"\n{info_0}{info_1}{info_2}{info_3}{info_4}")
    print("Смотреть фаил 'text_10.txt'")

    fileRead_2.close()

print("=" * 15, '2', "=" * 15)

''' 3 Дан текстовый файл. Удалить из него последнюю
строку. Результат записать в другой файл.'''

def dz_3():
    fileRead_3 = open('Reading_File/text_5.txt', encoding="utf-8")

    read_3 = fileRead_3.readlines()

    del read_3[-1]

    res = ""

    for i in read_3:
        res += i

    fileWrite_3 = open("Reading_File/text_6.txt", 'w')
    fileWrite_3.write(res)

    fileRead_3.close()
    fileWrite_3.close()
    print("Смотреть фаил 'text_6.txt'")


print("=" * 15, '3', "=" * 15)

''' 4 Дан текстовый файл. Найти длину самой длинной
строки.'''

def dz_4():
    fileRead_4 = open("Reading_File/text_7.txt", encoding='utf-8')

    read_4 = fileRead_4.readlines()

    max_len = len(read_4[1])

    for i in read_4:
        spis = i.replace('\n', '')
        if len(i) > max_len:
            file_max_len = open("Reading_File/text_8.txt", 'w', encoding='utf-8')
            file_max_len.write(i)
            max_len = len(i)
            ind = read_4.index(i)
            print(spis)
        else:
            print(spis)

    print(f"\nСамая большая строка под индексом {ind}, в ней {max_len} элементов.")
    print("Смотреть фаил 'text_8.txt'")

    file_max_len.close()
    fileRead_4.close()

print("=" * 15, '4', "=" * 15)

''' 5 Дан текстовый файл. Посчитать сколько раз в нем
встречается заданное пользователем слово.'''

def dz_5():
    fileRead_5 = open("Reading_File/text_7.txt", encoding="utf-8")

    read_5 = fileRead_5.read()
    print(read_5)

    sUser = input("Введите искомое слово ")

    listIn = read_5.split(" ")

    count = 0

    for i in listIn:
        count  += i.count(sUser)

    print("\nИскомое слово встречается", count, "раз/а")

    fileRead_5.close()

print("=" * 15, '5', "=" * 15)

''' 6 Дан текстовый файл. Найти и заменить в нем задан-
ное слово. Что искать и на что заменять определяется
пользователем.'''

def dz_6():
    fileRead_6 = open("Reading_File/text_9.txt", encoding="utf-8")

    read_6 = fileRead_6.read()

    print(read_6)

    sUserN = input("Введите искомое слово ")
    sUserZ = input("Введите слово которым хотите заменить ")

    read_6 = read_6.replace(sUserN, sUserZ)

    print(read_6)

    fileRead_6.close()




# sum(text.count(x) for x in ('.!?'))
# print(sum(p.count(x) for x in ('1234567890')))
# print(sum(p.count(x) for x in (':;.,- ')))
# print(sum(p.count(x) for x in ('!')))