
import s
a = input('Введіть слово')
word = a
with s.open('E:/learn/1.txt', encoding='utf-8') as file:
    for line in file:
        if word in line:
            print(line, end='')
        else:
            print('В тексті нема введеного слова')