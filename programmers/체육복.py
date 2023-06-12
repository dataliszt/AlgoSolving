
def solution(n, lost, reserve):
    student = {}
    student[0] = None
    
    for i in range(1,n+1):
        student[i] = 1
    student[n+1] = None
    
    for j in lost:
        student[j] -= 1
        
    for x in reserve:
        if x in lost:
            student[x] += 1
        else:
            student[x] =2
            
    for k in range(1,n+1):
        if student.get(k) == 0:
            if student.get(k-1) == 2:
                student[k] += 1
                student[k-1] -= 1
            elif student.get(k+1) == 2:
                student[k] += 1
                student[k+1] -= 1
            else:pass
            
    return n - list(student.values()).count(0)