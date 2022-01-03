path =  r'./input.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

depth = 0
horiz = 0
aim = 0 

for w in my_list:
    tempList = w.split()
    match tempList[0]:
        case 'forward':
            horiz += int(tempList[1])
            depth += aim*int(tempList[1])
        case 'down':
            aim += int(tempList[1])
        case 'up':
            aim -= int(tempList[1])

print(depth * horiz)

