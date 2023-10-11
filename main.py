#Type in your code here
import random

choice=( posssibilities 'rock','paper','scissors')

def choice_winner(marsh,computer):
    if(marsh =="rock" and computer=="paper"):
        print("lost bet!:")
        return "computer"
    elif(marsh=="rock"and computer == "scissors" ): 
        print("congrats! You win bet:") 
        return "marsh"
    elif (marsh=="scissors" and computer =="paper"): 
        print("congrats! You win bet:")
        return "marsh"
    elif (marsh=="scissors" and computer =="rock"):
        print("lost bet!:")
        return "computer"
    elif (marsh=="paper"and computer =="rock"):
         print("congrats! You win bet:")
         return "marsh"
    elif(marsh=="paper" and computer=="scissors"):
         print("lost bet!:")
         return "computer"

    else:
         print("its a draw,retry!")    
         return "Tie"
y
    if (marsh== "rock" or marsh=="paper" or marsh=="scissors"):
        break
    else:
         print(" invalid input. Try again.")  

  computer =random.choice(possibilities)
  print("Your hand:",marsh)
  print("computer hand:", computer)
  result=checkforWinner(marsh,computer)
  if(result=="marsh"):
       marshScore+=1
   elif(result=="computer")
       computerScore+=1
   else:
       drawScore+=1
    print("Your score",marshScore,"computer".computerScore,"Draw",tieScore)

print("Game over! Thank you for playing:")



         
            

        


