lst = ['hello', 15, 28, 'cat', 2.5, True, 'meme', [3, 4, 5], (-1, 14, False)]
cnt = 0

for i in lst:
    if type(i) is str:
        cnt += 1

print(f'Amount of strings: {cnt}') 
