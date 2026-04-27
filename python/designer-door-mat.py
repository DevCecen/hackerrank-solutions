#Problem : https://www.hackerrank.com/challenges/designer-door-mat/problem
#Difficulty: Easy

# Enter your code here. Read input from STDIN. Print output to STDOUT

def yazdir_ve_ekle(liste,eleman):
    print(eleman,sep="")
    liste.append(eleman)

my_list = []
N, M = map(int,input().split())
A = (M - 3) // 2
B = (M - 7) // 2

counter = 1
for i in range(1,N+1):
    yazdir_ve_ekle(my_list,("-"*(A)+".|."*(counter)+"-"*(A)))
    counter += 2
    A = A - 3
    if i == ((N-1)//2):
        print("-"*(B),"WELCOME","-"*(B),sep="")
        my_list.reverse()
        break
    
for i in my_list:
    print(i)