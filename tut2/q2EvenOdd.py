"""
# ----------------------
# Created : 30-09-2021 14:37
# Licencing : (C) 2021 Dalimol Abraham, LYIT
#             Available under GNU public licence
# Description: 
# Author : Dalimol Abraham
# ----------------------
"""

if  __name__ == '__main__':
     limit = int(input("Enter the limit: "))
     oddNum  = 0
     evenNum = 0
     for x in range(limit):
         if (x % 2) == 0:
              evenNum += 1
         else:
            oddNum += 1
     print("Count of even number" + str(evenNum))
     print("Count of odd number" + str(oddNum))
