if __name__ == '__main__':
    records=[]
    scores=[]
    for _ in range(int(input())):
        name = input()
        score = float(input())
        
        records.append([name, score])
        scores.append(score)
    
    second_lowest_score = sorted(set(scores))[1]
    names = [record[0] for record in records if second_lowest_score in record]
    names.sort()
    print(*names, sep='\n')