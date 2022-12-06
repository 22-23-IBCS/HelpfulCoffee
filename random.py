import random

def main():
    L = [32,14,4,90,50,55,22,78,12,3]
    
    while True:
        x = random.randint(0,len(L)-1)
        y = random.randint(0,len(L)-1)
        L[x], L[y]  = L[y], L[x]
        isSorted = True
        
        for i in range(len(L)-1):
            if L[i] > L[i+1]:
                isSorted = False
                break
            
        if isSorted:
            break

    print(L)

if __name__ == "__main__":
    main()

