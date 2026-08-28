#Problem : https://www.hackerrank.com/challenges/the-minion-game/problem
#Difficulty: Medium

def minion_game(string):
    stuart = 0
    kevin = 0
    vovels = ['A', 'E', 'I', 'O', 'U']
    consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'X', 'Y', 'Z']
    
    for i in range(len(string)):
        if string[i] in vovels:
            kevin += (len(string) - i)
        elif string[i] in consonants:
            stuart += (len(string) - i)
            
            
    if stuart>kevin:
        print(f"Stuart {stuart}")
    elif kevin>stuart:
        print(f"Kevin {kevin}")
    else:
        print(f"Draw")
    

if __name__ == '__main__':
    s = input()
    minion_game(s)