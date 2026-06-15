
'''
# *  
# * *  
# * * *  
# * * * *  
# * * * * *  
# * * * * * *  
# * * * * * * *  
# * * * * * *  
# * * * * *  
# * * * *  
# * * *  
# * *  
# *  

n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<m:
        print('* '*(i+1),end=' ')
    else:
        print('* '*(n-i),end=' ')
    print()
    


#       * 
#      ** 
#     *** 
#    **** 
#   ***** 
#  ****** 
# ******* 
#******** 
# ******* 
#  ****** 
#   *****
#    **** 
#     *** 
#      ** 
#       * 

n = int(input("Enter the size: "))
m = n//2

for i in range(n):
    if i<=m:
        print(' '*(m-i),end=' ')
        print('*'*(i+1),end=' ')
    else:
        print(' '*(i-m),end=' ')
        print('*'*(n-i),end=' ')
    print()





#    *  
#   * *  
#  * * *  
# * * * *  
#  * * *  
#   * *  
#    *  
# 7
    
n = int(input("Enter the size: "))
m = n//2
for i in range(n):
    if i<=m:
        print(' '*(m-i)+'* '*(i+1),end=' ')
    else:
        print(' '*(i-m)+'* '*(n-i),end=' ')
    print()



#  * * * * *
#  *       *
#  *       *
#  *       *
#  * * * * *

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or i == n-1 or j == 0 or j == n-1:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()

#    j
#  i * * * * *

#    *       *

#    * * * * *

#    *       *

#    *       *


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j==n-1  or i == n//2:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()

#    j
#  i * * * * *

#    *       *

#    * * * * *

#    *       *

#    * * * * *



n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or j==n-1  or i == n//2 or i==n-1:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()

#    j
#  i * * * * *

#    *       

#    * 

#    *       

#    * * * * *


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i ==n-1:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()




#    j
#  i * * * * *

#    *       *

#    *       *

#    *       *

#    * * * * *



n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i ==n-1 or j==n-1:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()



#    j
#  i * * * * *

#    *       

#    * * * * *

#    *       

#    * * * * *

n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0 or i ==n-1 or i==n//2:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()



#    j
#  i * * * * *

#    *       

#    * * * * *

#    *       

#    *


n = int(input("Enter the size: "))
for i in range(n):
    for j in range(n):
        if i == 0 or j == 0  or i==n//2:
            print("*", end = " ")
        else:
            print(" ", end=" ")
    print()'''

'''


  0 1 2 3 4
0 * * * * *      
1 *       
2 *   * * *    
3 *   *   *

4 * * *   *


'''





