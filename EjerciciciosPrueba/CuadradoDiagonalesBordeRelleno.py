"""
*******
* *   *
*  *  *
*   * *
*  *  *
* *   *
*******
"""

a = int(input("altura: "))
if a %2 == 0:
    exit()

for i in range(a):
    if i == 0 or i == a-1:
        print(a*"*")
    elif i < a//2:
        print("*" + " "*i + "*" + " "*(a -3-i) + "*")
    else:
        print("*" + " " * (a-1-i) + "*" + " "*(i-2) + "*")
        
str()