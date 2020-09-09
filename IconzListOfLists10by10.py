#!/usr/bin/env python
# coding: utf-8

# In[35]:


# userString = [[]]
# userString = list(input("Please enter 100 1s and/or zeros to display a 10 by 10 sized icon. Ones will be displayed as * and Zeros will be displayed as empty spaces: "))

# lst = [ ] 
# n = int(input("Enter number of elements : "))  
# for i in range(0, n): 
#     ele = [input(), int(input())] 
#     lst.append(ele) 
      
# print(lst)


# In[36]:


icon = [[0,0,0,0,0,0,0,0,0,0],
        [1,0,0,0,0,0,0,0,0,1],
        [1,1,0,0,0,0,0,0,1,1],
        [0,1,1,0,0,0,0,1,1,0],
        [0,0,1,1,0,0,1,1,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [0,0,0,0,1,1,0,0,0,0],
        [0,0,0,1,1,1,1,0,0,0],
        [1,1,1,1,0,0,1,1,1,1],
        [1,1,1,0,0,0,0,1,1,1]]


# In[37]:


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
    for row in icon:
        for item in row:            
            if item == 1:
                    print("***", end=" ")
            elif item == 0:
                    print("   ", end=" ")
        print()
def displayUserIcon(userString):
    for row in userString:
        for item in row:
            if item == '1':
                    print("*", end=" ")
            elif item == '0':
                    print(" ", end=" ")
                    
        print()
def main():
    displayIcon()
    enlargeIcon()
    displayUserIcon(userString)
       
if __name__ == '__main__':
    main()


# In[ ]:




