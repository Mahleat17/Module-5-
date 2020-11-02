#Mahleat Kidanemariam
#11/01/2020

#This program lists numbers divisible by 3, 5, or both.

num_1=1
num_2=50
for i in range(num_1, num_2+1):
   if(i%3==0):
      print("Divisible by 3")
   if (i%5==0):
       print("Divisible by 5")
   if ((i%3==0) and (i%5==0)):
       print ("Divisible by both")
