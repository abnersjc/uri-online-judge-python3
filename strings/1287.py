while True:
    try:
        n = str(input())
        numeros_string = ''
        stop_0 = False
        
        for dig in n:
            if dig.isdigit():
                if dig == '0' and stop_0 == True:
                    numeros_string += dig
                if dig != '0':
                    stop_0 = True
                    numeros_string += dig

            if dig == 'O' or dig == 'o':
                stop_0 = True
                numeros_string += '0'
            if dig == 'l':
                numeros_string += '1'
    
        if numeros_string.isdigit():
            if int(numeros_string) > 2147483647:
                print('error')

            if int(numeros_string) >= 0 and int(numeros_string) <= 2147483647:
                if (sum(int(i) for i in numeros_string)) == 0:
                    numeros_string = 0
                else:
                    print(int(numeros_string))
                    #if (sum(int(h) for h in numeros_string)) / len(numeros_string) == 1:
                    #    print(1)
                    #else:  
                    #    print(int(numeros_string))
                        
                    
        
        if n.isnumeric():
            if (sum(int(i) for i in n)) == 0:
                numeros_string = 0
                

        if numeros_string == 0:
            print(int(numeros_string))
            

        if n.isalpha() and numeros_string == '' and len(numeros_string) == 0:
            print('error')
        if n == '':
            print('error')

   
    except EOFError:
            break
    











'''
def isnumber(value):
    try:
        float(value)
    except ValueError:
        return False
    return True
print(isnumber(n))
'''