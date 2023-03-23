fileRead_0 = open('employee.txt', encoding='utf-8')
read_0 = fileRead_0.readlines()
# print(read_0)

try:
    str_emp_0 = "".join(read_0[0])
    str_emp_1 = "".join(read_0[1])
    str_emp_2 = "".join(read_0[2])

    print("Сотрудник: ", str_emp_0)
    print("Сотрудник: ", str_emp_1)
    print("Сотрудник: ", str_emp_2)


    full_str = ''.join(read_0)

except:
    pass

finally:
    while True:
        os = input("Продолжим? 'да/нет'")
        if os == 'нет':
            break
        else:
            print("Здравствуйте о каком из сотрудников Вам нужна информация?")
            print("Введите Фамилию или инициал имени")
            poisk = input("Ввод ")

            if poisk == 'Иванов' or poisk == 'С':
                print(str_emp_0)
                while True:
                    dellete = input("Желаете удалить данные о сотруднике? да/нет ")
                    if dellete == 'да':
                        str_emp_0 = str_emp_0
                        full_str = full_str.replace(str_emp_0, '')
                        with open('employee.txt', 'w', encoding='utf-8') as fl:
                            fl.write(full_str)
                        break
                    else:
                        pass
                    dop = input("Желаете что-то изменить в данных сотрудника? да/нет ")
                    if dop == "да":
                        print("Изменить ФИО-1; Номер телефона-2; Возраст-3; Должность-4, Оклад в месяц-5")
                        iz_info = int(input("Что хотите изменить? "))
                        iz_info_2 = input("Введите новые данные ")
                        if iz_info == 1:
                            str_emp_9 = str_emp_0.replace('Иванов С.А.', iz_info_2)
                        if iz_info == 2:
                            str_emp_0 = str_emp_0.replace('81113334455', iz_info_2)
                        if iz_info == 3:
                            str_emp_0 = str_emp_0.replace('49', iz_info_2)
                        if iz_info == 4:
                            str_emp_0 = str_emp_0.replace('Главный бухгалтер', iz_info_2)
                        if iz_info == 5:
                            str_emp_0 = str_emp_0.replace('60000', iz_info_2)

                        file_write_vop = input("Хотите сохранить обновленные данные о сотркднике? да/нет ")
                        if file_write_vop == "да":
                            with open("text_11.txt", 'a', encoding='utf-8') as f:
                                f.write(str_emp_0)

                        print("Новые данные ", str_emp_0)

                    else:
                        break




            if poisk == 'Александров' or poisk == 'В':
                print(str_emp_1)
                while True:
                    dellete = input("Желаете удалить данные о сотруднике? да/нет ")
                    if dellete == 'да':
                        full_str = full_str.replace(str_emp_1, '')
                        with open('employee.txt', 'w', encoding='utf-8') as fl:
                            fl.write(full_str)
                        break
                    else:
                        pass
                    dop = input("Желаете что-то изменить в данных сотрудника? да/нет ")
                    if dop == "да":
                        print("Изменить ФИО-1; Номер телефона-2; Возраст-3; Должность-4, Оклад в месяц-5")
                        iz_info = int(input("Что хотите изменить? "))
                        iz_info_2 = input("Введите новые данные ")
                        if iz_info == 1:
                            str_emp_1 = str_emp_1.replace('Александров В.П.', iz_info_2)
                        if iz_info == 2:
                            str_emp_1 = str_emp_1.replace('83284523850', iz_info_2)
                        if iz_info == 3:
                            str_emp_1 = str_emp_1.replace('26', iz_info_2)
                        if iz_info == 4:
                            str_emp_1 = str_emp_1.replace('Инженер', iz_info_2)
                        if iz_info == 5:
                            str_emp_1 = str_emp_1.replace('55000', iz_info_2)

                        file_write_vop = input("Хотите сохранить обновленные данные о сотркднике? да/нет ")
                        if file_write_vop == "да":
                            with open("text_11.txt", 'a', encoding='utf-8') as f:
                                f.write(str_emp_1)

                        print("Новые данные ", str_emp_1)

                    else:
                        break

                
            if poisk == 'Стрельцова' or poisk == 'И':
                print(str_emp_2)
                while True:
                    dellete = input("Желаете удалить данные о сотруднике? да/нет ")
                    if dellete == 'да':
                        full_str = full_str.replace(str_emp_2, '')
                        with open('employee.txt', 'w', encoding='utf-8') as fl:
                            fl.write(full_str)
                        break
                    else:
                        pass
                    dop = input("Желаете что-то изменить в данных сотрудника? да/нет ")
                    if dop == "да":
                        print("Изменить ФИО-1; Номер телефона-2; Возраст-3; Должность-4, Оклад в месяц-5")
                        iz_info = int(input("Что хотите изменить? "))
                        iz_info_2 = input("Введите новые данные ")
                        if iz_info == 1:
                            str_emp_2 = str_emp_2.replace('Стрельцова И.Д.', iz_info_2)
                        if iz_info == 2:
                            str_emp_2 = str_emp_2.replace('89034762548', iz_info_2)
                        if iz_info == 3:
                            str_emp_2 = str_emp_2.replace('20', iz_info_2)
                        if iz_info == 4:
                            str_emp_2 = str_emp_2.replace('Секретарь', iz_info_2)
                        if iz_info == 5:
                            str_emp_2 = str_emp_2.replace('40000', iz_info_2)

                        file_write_vop = input("Хотите сохранить обновленные данные о сотркднике? да/нет ")
                        if file_write_vop == "да":
                            with open("text_11.txt", 'a', encoding='utf-8') as f:
                                f.write(str_emp_2)

                        print("Новые данные ", str_emp_2)

                    else:
                        break
