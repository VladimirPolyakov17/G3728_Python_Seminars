# Задача 27: Пользователь вводит текст(строка). Словом считается последовательность непробельных символов идущих подряд, 
# слова разделены одним или большим числом пробелов. Определите, сколько различных слов содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells that she sells are sea shells 
# I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells
# Output: 13
import string # Коллекция
my_text = ''' She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure.So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells '''
print(my_text)

punct = list (string.punctuation) + ['\n', '\t' ] # '\n' - перевод на новую строку, '\t' - табуляция.

for char in punct:
    my_text = my_text.replace(char, ' ')

my_text = my_text.lower(). split()

dict_count = {}
for key in my_text:
    dict_count[key] = dict_count.get(key, 0) + 1
print(*dict_count.items(), sep='\n')

# print(my_text)

print(len(set(dict_count)))
