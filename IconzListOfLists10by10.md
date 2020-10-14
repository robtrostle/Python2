```python
import contextlib
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
```


```python
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
#generateTxtFile will ask user to name their txt file and then generate a txt file in local directory based on name. 
def generateTxtFile():
    iconName = input("This app will create a text file of the chosen icon.\n"
                     "Please pick a name: ") or 'icon.txt'
    with open(iconName + '.txt', 'w') as f:
        with contextlib.redirect_stdout(f):
            displayIcon()
        print(iconName + ".txt has been generated.")

def main():
    displayIcon()
    enlargeIcon()
    generateTxtFile()
           
if __name__ == '__main__':
    main()
```

                        
    *                 * 
    * *             * * 
      * *         * *   
        * *     * *     
          * * * *       
            * *         
          * * * *       
    * * * *     * * * * 
    * * *         * * * 
                                            
    ***                                 *** 
    *** ***                         *** *** 
        *** ***                 *** ***     
            *** ***         *** ***         
                *** *** *** ***             
                    *** ***                 
                *** *** *** ***             
    *** *** *** ***         *** *** *** *** 
    *** *** ***                 *** *** *** 
    This app will create a text file of the chosen icon.
    Please pick a name: hockeySticks
    hockeySticks.txt has been generated.
    


```python

```
