
import re
from pprint import pprint
import csv

with open('C:\\Users\\Mario\\Downloads\\phonebook_raw.csv', encoding="utf-8") as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)

  new_contact_list = []
  for contact in contacts_list:
    if contact[1] == '':
      combined = ' '.join(contact[:3])
      divided = combined.split(' ')
      contact[:3] = divided[:3]
      new_contact_list.append(contact)
    elif contact[2] == '':
      combined = ' '.join(contact[:3])
      divided = combined.split(' ')
      contact[:3] = divided[:3]
      new_contact_list.append(contact)
    else:
      new_contact_list.append(contact)



  for sentence in new_contact_list:
    pattern = r'(\+7|8)\s*\(*(\d{1,3})\)*\-*\s*(\d{1,3})\-*(\d{1,2})\-*(\d+)(\s*)\(*((\w+\.)\s(\w+)\)*)*'
    sentence[5] = re.sub(pattern, r'+7\(\2\)\3\-\4\-\5\6\8\9', sentence[5])



print(new_contact_list)
with open("new_phonebook_raw.csv", "w", encoding="utf-8") as f:
  datawriter = csv.writer(f, delimiter=',')
  datawriter.writerows(new_contact_list)









