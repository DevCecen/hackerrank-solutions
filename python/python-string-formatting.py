#Problem: https://www.hackerrank.com/challenges/python-string-formatting/problem
#Difficulty: Easy

def print_formatted(number):
    max_len = len(bin(number)[2:])
    my_list = []
    for x in range(1,number+1):
        my_list.append([x,oct(x)[2:],(hex(x)[2:]).upper(),bin(x)[2:]])
    
    result = ""
    for x in my_list:
        for y in x:
            result += " "*((max_len)-len(str(y))) + str(y) + " "
        result += "\n"
    
    return print(result)

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)