my_text = open("vedomost_po_zp.txt", "r", encoding='UTF-8')
content = my_text.readlines()
# print(content)
my_text.close()
all_zp = 0
for el in content:
    zp = int(el.split('-')[1])
    if zp < 20000:
        print(el, end='')
    all_zp += zp
print("\nSrednyy zp - ", all_zp/len(content))