#snake,water,gun
import random
def gamewin(comp,you):
    if comp ==you:
        return None
    elif comp == ' s':

         if you== 'w':
                return False
    if you==  'g':
       return True


    elif comp == 'w':
      if you== 'g':
        return False
    if you== 's':
       return True  
 
    elif comp ==  'g':
            if you== 's':
                return False
    if you==  'w':
       return True 

print("comp turn: Snake(s) water(w) or gun(g)?")

randNo=random.randint(1,3)
if randNo == 1:
    comp= 's'  
if randNo == 2:
    comp= 'w'

if randNo == 3:
    comp=  'g'


you=input("player1 turn : snake(s) water(w) or gun(g)?\n")
a=gamewin(comp,you)


print(f"computer choose{comp}")
print(f"you choose{you}")

if a==None:
    print("game is tie.")
elif a:
    print("you win.")
else :
    print("you loose.")
