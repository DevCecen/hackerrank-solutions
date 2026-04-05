#Problem : https://www.hackerrank.com/challenges/python-print/problem
#Difficulty : Easy

if __name__ == '__main__':
    n = int(input())
    number_string = ""
    
    for number in range(1,n+1):
        number_string += str(number)
        
    print(number_string)
