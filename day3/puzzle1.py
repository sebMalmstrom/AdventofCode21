path =  r'./input.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')
counter = [0] * 12

for w in my_list:
    for i in range(0,12):
        counter[i] += int(w[i])

gam = [0] * 12
eps = [0] * 12
for w in range(0,12):
    if counter[w] > len(my_list)/2:
        gam[w] = 1
        eps[w] = 0
    else:
        gam[w] = 0
        eps[w] = 1

print(int(''.join(map(str, gam)),2 ) * int(''.join(map(str, eps)),2 ))