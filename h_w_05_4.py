my_text = open("translation.txt", "r")
content = my_text.readlines()
# print(content)
my_text.close()

new_f = open("new_f.txt", "w", encoding='UTF-8')

for el in content:
    el = el.split(' - ')
    if  el[0] == 'One':
        el[0] = 'Один'
    elif el[0] == 'Two':
        el[0] = 'Два'
    elif el[0] == 'Three':
        el[0] = 'Три'
    else: el[0] = 'Четыре'
    el = ' - '.join(el)
    new_f.write(el)
new_f.close()
