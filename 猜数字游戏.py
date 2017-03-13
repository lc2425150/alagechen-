from random import randint
num = randint(0,100)
print 'Guess what I think?'
answer = input()
while answer != 10:


   if  answer < num:
     print"too small?"
     answer = input()

   if  answer > num:
     print"too big?"
     answer = input()

   if answer == num:
     print'bingo'
     bingo = True
     break