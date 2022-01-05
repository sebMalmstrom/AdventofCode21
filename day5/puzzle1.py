path =  r'./input.in'
input_file = open(path, 'r')
my_list = input_file.read().split('\n')

number = {}

for i in my_list:
    word = i.split(" -> ")
    print(word)