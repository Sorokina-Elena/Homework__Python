def read_csv(filename):
    phone_book=[]
    fields=['Фамилия', 'Имя', 'Телефон', 'Описание']
    with open(filename,'r',encoding='utf-8') as phb:
        for line in phb:
            record = dict(zip(fields, line.split(',')))
            phone_book.append(record)
        return phone_book
    

def write_txt(filename, phone_book):
    with open(filename,'w',encoding='utf-8') as phout:
        for i in range(len(phone_book)):
            s=''
            for v in phone_book[i].values():
                s+=v+','
        phout.write(f'{s[:-1]}\n')   


def find_by_lastname(phone_book, Last_name):
    filtered = list(filter(lambda x: x['Фамилия'] == Last_name, phone_book))
    return list(map(lambda x: x['Телефон'] + ' ' + x['Фамилия'] + ' ' + x['Имя'], filtered))


def change_number(phone_book, Last_name, new_number):
    for i in range(len(phone_book)):
        if Last_name == phone_book[i]['Фамилия']:
            key, value = 'Телефон', new_number
            phone_book[i].update({key: value})
    return phone_book


def delete_by_lastname(phone_book, Last_name):
    return list(filter(lambda x: x['Фамилия'] != Last_name, phone_book))


def find_by_number(phone_book, number):
    filtered = list(filter(lambda x: x['Телефон'] == number, phone_book))
    return list(map(lambda x: x['Фамилия'] + ' ' + x['Имя'], filtered))


def add_user(phone_book):
    new_data = {}
    Lastname = input('Фамилия: ')
    key, value = 'Фамлия', Lastname
    new_data.update({key: value})

    firsname = input('Имя: ')
    key, value = 'Имя', firsname
    new_data.update({key: value})

    phone = input('Телефон: ')
    key, value = 'Телефон', phone
    new_data.update({key: value})

    description = input('Описание: ')
    key, value = 'Описание', description
    new_data.update({key: value})
    phone_book.append(new_data)
    return phone_book


def show_menu():
    print('1. Распечатать справочник'
    '2. Найти телефон по фамилии'
    '3. Изменить номер телефона'
    '4. Удалить запись'
    '5. Найти абонента по номеру телефона'
    '6. Добавить абонента в справочник'
    '7. Закончить работу', sep = '\n')
    choice=int(input())
    return choice


def work_with_phonebook():
    choice=show_menu()
    phone_book=read_csv('phonebook.csv')
    while (choice!=7):
        if choice==1:
            print(phone_book)
        elif choice==2:
            last_name=input('lastname ')
            print(find_by_lastname(phone_book,last_name))
        elif choice==3:
            last_name=input('lastname ')
            new_number=input('new number ')
            print(change_number(phone_book,last_name,new_number))
        elif choice==4:
            lastname=input('lastname ')
            print(delete_by_lastname(phone_book,lastname))
        elif choice==5:
            number=input('number ')
            print(find_by_number(phone_book,number))
        elif choice==6:
            user_data=input('new data ')
            add_user(phone_book,user_data)
            write_txt('phonebook.txt',phone_book)
        choice=show_menu()

work_with_phonebook()
