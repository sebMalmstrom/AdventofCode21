path =  r'./input.in'
input_file = open(path, 'r')
my_list = input_file.read().split()
counter = 0
for w in range(1, len(my_list)):
    if int(my_list[w]) > int(my_list[w-1]):
        counter += 1


print(counter)


