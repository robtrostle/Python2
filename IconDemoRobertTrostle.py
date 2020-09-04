#!/usr/bin/env python
# coding: utf-8

# In[1]:


iconDict = {"line 1" :[0,1,0],
            "line 2" :[1,1,1],
            "line 3" :[0,1,0]}
            

# printIcon() iterates over the IconDict dictionary and converts characters from binary to * and blank space for 0. 

def printIcon():
    for key in iconDict:
        binaryList = iconDict[key]

        for v in binaryList:
            if v == 1:
                print("*", end=" ")
            elif v == 0:
                print(" ", end=" ")
        print(" ")
    
def main():
    printIcon()
    
    
if __name__ == '__main__':
    main()
    

