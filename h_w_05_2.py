my_text = open("text2.txt", "r", encoding='UTF-8')
content = my_text.readlines()
print(content)
my_text.close()
print("Kolichestvo strok - ", len(content))
# words = 1
# for el in content:
#         for x in el:
#             if x == ' ' or x == '\n':
#                 words += 1
# print("Kolichestvo slov - ", words)
words_cont = []
for el in content:
    words_cont.append(el.split())
n_of_words = 0
for el in words_cont:
    n_of_words += len(el)
print("Kolichestvo slov - ", n_of_words)
