# Напишите программу, удаляющую из текста все слова содержащие "абв".
line = 'asdf asdf gdsfd gret as'
words = line.split(' ')
result = 'asd'
new_words = [ ]
for word in words:
    if result not in word:
        new_words.append(word)
print(new_words)