#Problem: https://www.hackerrank.com/challenges/python-lists/problem
#Difficulty: Easy

if __name__ == '__main__':
    N = int(input())
    my_list = []
    for _ in range(N):
        input_value,*a = input().split()
        if input_value == "insert":
            b,c = map(int,a)
            my_list.insert(b,c)
        elif input_value == "print":
            print(my_list)
        elif input_value == "remove":
            b = int(a[0])
            my_list.remove(b)
        elif input_value == "append":
            b = int(a[0])
            my_list.append(b)
        elif input_value == "sort":
            my_list.sort()
        elif input_value == "pop":
            my_list.pop()
        elif input_value == "reverse":
            my_list.reverse()