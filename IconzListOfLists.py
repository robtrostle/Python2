#!/usr/bin/env python
# coding: utf-8

# In[16]:


#answer = input("Please Enter a row size: ")
icon = [[0,1,0],[1,1,1],[0,1,0]]


# In[17]:


# printIcon() iterates over the icon list of lists and converts characters from binary to * and blank space for 0.
def displayIcon():
    for row in icon:
        for item in row:
            if item == 1:
                    print("*", end=" ")
            elif item == 0:
                    print(" ", end=" ")
        print()
# enlargeIcon() simply triples the output of displayIcon
def enlargeIcon():
    for row in iconz:
        for item in row:            
            if item == 1:
                    print("***", end=" ")
            elif item == 0:
                    print("   ", end=" ")
        print()
        
def main():
    displayIcon()
    enlargeIcon()
       
if __name__ == '__main__':
    main()


# In[ ]:




