path =  r'./input.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')
originallist = my_list.copy()
counter = [0] * len(my_list[0])
maxlangd = len(my_list[0])

def mostExisting(index, len, list):
    counter2 = 0
    for w in list:
        counter2 += int(w[index])
        
    if counter2 >= len/2:
        return 1
    else:
        return 0

def leastExisting(index, len, list):
    counter2 = 0
    for w in list:
        counter2 += int(w[index])
        
    if counter2 >= len/2:
        return 0
    else:
        return 1

for i in range(0, maxlangd):
    onelist = []
    zerolist = []
    for w in my_list:
        if int(w[i]) == 1:
            onelist.append(w)
        else:
            zerolist.append(w)


    langd = len(my_list)
    print(mostExisting(i, langd, my_list))
    if mostExisting(i, langd, my_list) == 1:
        my_list = onelist.copy()
    else:
        my_list = zerolist.copy()

    onelist.clear()
    zerolist.clear()

oxy = my_list[0]

my_list = originallist.copy()

for i in range(0, maxlangd):
    onelist = []
    zerolist = []
    for w in my_list:
        if int(w[i]) == 1:
            onelist.append(w)
        else:
            zerolist.append(w)


    langd = len(my_list)
    print(leastExisting(i, langd, my_list))
    if leastExisting(i, langd, my_list) == 1:
        my_list = onelist.copy()
    else:
        my_list = zerolist.copy()
    if len(my_list) == 1:
        break

    onelist.clear()
    zerolist.clear()

co = my_list[0]

print(int(oxy, 2) * int(co, 2))



    