def minion_game(string):
    # your code goes here
    vowels = set(string).intersection(['A','E','I','O','U'])  
    scores = [i for i in range(len(string),0,-1)] 
    Kevin = 0
    Stuart = 0
    for s,i in zip(string,scores):
        if s in vowels:
            Kevin += i
        else:
            Stuart += i
    if Kevin>Stuart:
        print('Kevin',Kevin)
    elif Kevin<Stuart:
        print('Stuart',Stuart)
    else:
        print("Draw")
if __name__ == '__main__':
    s = input()
    minion_game(s)