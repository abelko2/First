num_list = [10, 2, 30, 100, 10, 50, 11, 30, 15, 7]
word_list = ['python', 'ruby', 'perl', 'ruby', 'perl', 'python', 'ruby', 'perl']
num_list.reverse()
i1 = int(input('Enter value:\n'))
a = num_list.index(i1)
b = 44444
num_list.insert(a, b)
num_list.reverse()
c = num_list.index(b)
itog = c-1
print('Posledniy raz vstrechaetcya - {}'.format(itog))
i1 = input('Enter text:\n')
word_list.reverse()
a = word_list.index(i1)
b = 'TTTTT'
word_list.insert(a, b)
word_list.reverse()
c = word_list.index(b)
itog = c-1
print('Posledniy raz vstrechaetcya - {}'.format(itog))
