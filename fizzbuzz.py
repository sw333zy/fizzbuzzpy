#numbers for x in the range of 1 - 100 and iterating by 1
for x in range(1,100,1):
    #if x is a multiple 5 meaning it can be modulo by 5 and have a remander of 0 then
    #it is is a multiple of that number so x%3==0 and x%5==0 
    if x%5==0 & x%3==0:
        print ('Fizzbuzz')
        #else if its only by 5 print buzz
    elif x%5==0:
        print('Buzz')
        #or if its only 3 print fizz
    elif x%3==0:
        print('Fizz')
    else:
        print(x)
