f = input('Enter free space : ')
u = input('Enter used space : ')
o = input('Enter delete file size : ')
n = input('Enter new file size : ')

total = f+u
used = u - o
used = used + n
free = total - used

print('Space Available: ',free)