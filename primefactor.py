def prime_factor(n):
    if n>1:
        for i in range(2,n):
            if(n%i) ==0:
                print(n,"is not a prime factor")
                break


        else:
          print(n,"is a prime factor")
    else:
         print(n,"is not a prime number")
prime_factor(7)
prime_factor(20)        

                
