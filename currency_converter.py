currency=["KSH", "USD","EURO","POUND" ]
#write a python that convertes the specified amount
#write a function that has twoparameters(currency,amount,rates)
def currency_converter(KSH):
    if KSH==100:
      for KSH in range(0,100):

          if(KSH%100) ==100:
              print(KSH,"USD")
              break
          else:
              print(KSH," USD")   
    else:
         print(KSH,"convert to USD")  

currency_converter(101) 




