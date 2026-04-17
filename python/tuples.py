#Problem: https://www.hackerrank.com/challenges/python-tuples/problem
#Difficulty: Easy

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    
    tuple_list = tuple(integer_list)
    print(hash(tuple_list))