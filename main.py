from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
for x in contacts_list:
    if len(x) > 7:
        del x[7:]
#pprint(contacts_list)

phone_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)' \
                r'(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)' \
                r'(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
phone_pattern_new = r'+7(\4)\8-\11-\14\15\17\18\20'
contacts_list_new = []

for i in contacts_list:
    i_string = ",".join(i)
    format_i = re.sub(phone_pattern, phone_pattern_new, i_string)
    phone_i = format_i.split(',')
    contacts_list_new.append(phone_i)
#pprint(contacts_list_new)

name_pattern = r'^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)' \
                   r'(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)'
name_pattern_new = r'\1\3\10\4\6\9\7\8'
contacts_list = []
for j in contacts_list_new:
    j_string = ",".join(j)
    format_j = re.sub(name_pattern, name_pattern_new, j_string)
    name_j = format_j.split(',')
    contacts_list.append(name_j)
#pprint(contacts_list)

for i in contacts_list:
    for j in contacts_list:
        if i[0] == j[0] and i[1] == j[1] and i != j:
            if i[2] == '':
                i[2] = j[2]
            if i[3] == '':
                i[3] = j[3]
            if i[4] == '':
                i[4] = j[4]
            if i[5] == '':
                i[5] = j[5]
            if i[6] == '':
                i[6] = j[6]
        contact_list = list()
        for page in contacts_list:
            if page not in contact_list:
                contact_list.append(page)
pprint(contact_list)

with open("phonebook_new.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(contact_list)
