def RemoveChar(someWords , oneChar):
    result = "";
    for char in someWords :
        if char != oneChar:
            result += char

    return result



def FindPrimeNumbers (fNum , sNum) :
    for n in range(fNum, sNum):
        if n == 1:
            continue
        check = True
        for m in range(2 , n-1):
            if n%m == 0 :
                check = False
                break
    
        if check :
            print (str(n) + " Is a prime number")


def FindCharCount(someWords , oneChar):
    result = 0;
    for char in someWords :
        if char == oneChar:
            result += 1

    return result




#print(RemoveChar("ayad muayad" , 'a'))

#FindPrimeNumbers (1 , 10)

#print(FindCharCount("ayad muayad" , 'n'))