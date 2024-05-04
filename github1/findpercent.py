if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    if query_name in student_marks:
        student_scores = student_marks[query_name]
        
        score_length = len(student_scores)
        
        total_score = sum(student_scores)
        
        average_score = total_score / score_length
        
        print(f"{average_score:.2f}")