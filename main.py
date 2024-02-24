import re
from pprint import pprint
# читаем адресную книгу в формате CSV в список contacts_list
import csv
import os

file_path = os.path.join(os.getcwd(), 'telephon_book\phonebook_raw.csv')
with open(file_path, encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
####pprint(contacts_list)

# TODO 1: выполните пункты 1-3 ДЗ
# ваш код

pattern = "(\+7|8)+\s*(\()?(\d{3})[-\s]?(\))?\s*(\d{3})[-\s]?(\d{2})[-\s]?(\d{2})+\s*((\()?(доб.)+[ \s]+(\d+)(\))?)?"
substitution = r"+7(\3)\5-\6-\7 \10 \11"

contacts_list_new = []
set_fio = set()
len_source = len(contacts_list)
contacts_list_new.append(contacts_list[0])

for i in range(1, len_source):
    id_name = " ".join(" ".join((contacts_list[i][:3])).split()[:2])
    if id_name not in set_fio:
        set_fio.add(id_name)
        i_new = len(set_fio)
        contacts_list_new.append(['', '', '', '', '', '', ''])
        fio_string = " ".join(contacts_list[i][:3]).strip()
        fio = fio_string.split(" ")
        contacts_list_new[i_new][0] = fio[0]
        contacts_list_new[i_new][1] = fio[1]
        if len(fio) > 2:
            contacts_list_new[i_new][2] = fio[2]
        contacts_list_new[i_new][3] = contacts_list[i][3]
        contacts_list_new[i_new][4] = contacts_list[i][4]
        contacts_list_new[i_new][5] = (re.sub(pattern, substitution, contacts_list[i][5])).strip()
        contacts_list_new[i_new][6] = contacts_list[i][6]

        if i < len_source:
            for next_index in range(i + 1, len_source):
                fio_next = " ".join((" ".join(contacts_list[next_index][:3])).split()[:2])
                if fio_next == id_name:
                    if contacts_list_new[i_new][3] == '':
                        contacts_list_new[i_new][3] = contacts_list[next_index][3]
                    if contacts_list_new[i_new][4] == '':
                        contacts_list_new[i_new][4] = contacts_list[next_index][4]
                    if contacts_list_new[i_new][5] == '':
                        contacts_list_new[i_new][5] = (re.sub(pattern, substitution, contacts_list[next_index][5])).strip()
                    if contacts_list_new[i_new][6] == '':
                        contacts_list_new[i_new][6] = contacts_list[next_index][6]

# TODO 2: сохраните получившиеся данные в другой файл
# код для записи файла в формате CSV
with open("telephon_book.phonebook.csv", "w", encoding="utf-8") as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(contacts_list_new)
