num_f = open("f_with_num.txt", "w")
num_f.write(input("Vvedite chisla razdelyy probelami "))
num_f.close()

num_f = open("f_with_num.txt", "r")
content = num_f.read()
num_f.close()

l_num = content.split(' ')
s = 0
for x in l_num:
    s += int(x)
print("Summa chisel v faile ", s)