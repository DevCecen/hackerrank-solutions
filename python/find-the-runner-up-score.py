#Problem: https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list/problem
#Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    reverse_arr = sorted(arr,reverse=True)
    
    for indeks,number in enumerate(reverse_arr):
        if reverse_arr[indeks] != reverse_arr[indeks + 1]:
            print(reverse_arr[indeks + 1])
            break
    
