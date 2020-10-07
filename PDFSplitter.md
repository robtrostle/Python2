```python
import os
import pandas as pd
import pyodbc
#import ConfigParser
from pandas import Series, DataFrame

outputPath = 'C:\output'
```


```python
excel = pd.read_excel('Loans.xlsx')
excel.head()
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>LOAN_NUMBER</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>4569898</td>
    </tr>
    <tr>
      <th>1</th>
      <td>9895689</td>
    </tr>
    <tr>
      <th>2</th>
      <td>8995998</td>
    </tr>
    <tr>
      <th>3</th>
      <td>5980985</td>
    </tr>
    <tr>
      <th>4</th>
      <td>5678978</td>
    </tr>
  </tbody>
</table>
</div>




```python
loanNumber = excel.LOAN_NUMBER.tolist()
print(loanNumber)
```

    [4569898, 9895689, 8995998, 5980985, 5678978]
    


```python
from PyPDF2 import PdfFileReader, PdfFileWriter
outputPath = 'C:\\output'
def pdf_splitter(path):
    fname = os.path.splitext(os.path.basename(path))[0]
    counter = 0
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))
        output_filename = '{}_Page Number_{}.pdf'.format(fname, loanNumber[page])
        
        with open(os.path.join(outputPath,output_filename), 'wb') as out:
            pdf_writer.write(out)
            
        print('Created: {}'.format(output_filename))
        counter += 1
    print (counter)
if __name__ == '__main__':
    path = 'syllabusCIT244.pdf'
    pdf_splitter(path)
```

    Created: syllabusCIT244_Page Number_4569898.pdf
    Created: syllabusCIT244_Page Number_9895689.pdf
    Created: syllabusCIT244_Page Number_8995998.pdf
    Created: syllabusCIT244_Page Number_5980985.pdf
    Created: syllabusCIT244_Page Number_5678978.pdf
    5
    


```python

```
