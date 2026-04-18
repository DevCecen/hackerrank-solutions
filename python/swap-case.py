# Problem: https://www.hackerrank.com/challenges/swap-case/problem
# Difficulty: Easy

def swap_case(s):
    my_list = []
    for char in s:
        if char.islower():
            my_list.append(char.upper())
        elif char.isupper():
            my_list.append(char.lower())
        else:
            my_list.append(char)
    return "".join(my_list)
    
    
if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)