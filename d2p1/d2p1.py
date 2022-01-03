path =  r'./input.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

depth = 0
horiz = 0

for w in my_list:
    tempList = w.split()
    match tempList[0]:
        case 'forward':
            horiz += int(tempList[1])
        case 'down':
            depth += int(tempList[1])
        case 'up':
            depth -= int(tempList[1])

print(depth * horiz)

