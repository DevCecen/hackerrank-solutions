#Problem: https://www.hackerrank.com/challenges/nested-list/problem
#Difficulty: Easy

if __name__ == '__main__':
    student_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        student_list.append([name, score])
        student_list.sort(key=lambda x: x[1])
    student_list2 = []
    
    en_dusuk_not = student_list[0][1]
    while en_dusuk_not == student_list[0][1]:
        student_list.pop(0)
    
    for x in student_list:
        for y in student_list:
            if x[1] == y[1]:
                student_list2.append(y[0])
        break;
        
    sorted_studentlist2 = sorted(student_list2)
    for x in sorted_studentlist2:
        print(x)
        
        
                
                
    
