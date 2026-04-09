#Problem: https://www.hackerrank.com/challenges/finding-the-percentage/problem
#Difficulty: Easy

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    student_score_sum = 0
    
    for x in student_marks[query_name]:
        student_score_sum += x
        
    print(f"{(student_score_sum/3):.2f}")