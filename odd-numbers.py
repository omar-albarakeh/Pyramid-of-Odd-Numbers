
#to print pattern numbers
#def odd_numbers(num):
#   for i in range(1 , num*2 ,2):
#      print(i,end=" ")

def p_odd_numbers(x):
    for i in range(x):
        for j in range(1, 2*i + 2,2):
            print(j, end=" ") 
        print()

x = int(input("ur nb"))
p_odd_numbers(x)
#odd_numbers(x)
