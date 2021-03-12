cr_text = open("my_file.txt", "w", encoding='UTF-8')

while True:
    my_str = input("Vvedite tekst postrochno, esli nechego vvesti nazhmite enter ")
    cr_text.write(my_str)
    cr_text.write('\n')
    if my_str == '':
        break
cr_text.close()