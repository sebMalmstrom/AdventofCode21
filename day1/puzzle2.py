path =  r'./input.in'
input_file = open(path, 'r')
my_list = list(map(int, input_file.read().split()))
sum1 = 0
sum2 = 0
counter = 0

for w in range(0, len(my_list) - 1):
    
    if sum(my_list[w+1 : w+4]) > sum(my_list[w : w+3]):
        counter += 1

print(counter)