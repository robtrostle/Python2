![](https://i.ytimg.com/vi/CiDRFapPor4/hqdefault.jpg)

### key for NASA photos: RcDlBrpTe5hIcYRzarcCeyiUhNWcooWMrpqhAL0e    


```python
%matplotlib inline
import requests,json
import pandas as pd
from IPython.display import Image
#use requests to issue a request to a remote host. Choose the appropriate http method by calling the corresponding 
#function on the module. 
resp = requests.get('https://api.nasa.gov/planetary/apod?api_key=RcDlBrpTe5hIcYRzarcCeyiUhNWcooWMrpqhAL0e')
#Get status code
print(resp,'\n')
#get headers
if(int(resp.status_code)==200):
    payload = json.loads(resp.text)#loads is load string
    for key in payload:
        print(key)
```

    <Response [200]> 
    
    copyright
    date
    explanation
    hdurl
    media_type
    service_version
    title
    url
    


```python
#Assign image url within json dict to image, assign explantion to variable caption to view below after displaying image. 
image = payload['url']
caption = payload['explanation']
title = payload['title']
```


```python
Image(image)
```




![jpeg](output_4_0.jpg)




```python
print("Title: "+title,'\n')
print(caption)
```

    Title: The Colorful Clouds of Rho Ophiuchi 
    
    The many spectacular colors of the Rho Ophiuchi (oh'-fee-yu-kee) clouds highlight the many processes that occur there.  The blue regions shine primarily by reflected light.  Blue light from the  Rho Ophiuchi star system and nearby stars reflects more efficiently off this portion of the nebula than red light.  The Earth's daytime sky appears blue for the same reason.  The red and yellow regions shine primarily because of emission from the nebula's atomic and molecular gas.  Light from nearby blue stars - more energetic than the bright star  Antares - knocks electrons away from the gas, which then shines when the electrons recombine with the gas.  The dark brown regions are caused by dust grains - born in young stellar atmospheres - which effectively block light emitted behind them.  The Rho Ophiuchi star clouds, well in front of the globular cluster M4 visible here on the upper right, are even more colorful than humans can see - the clouds emits light in every wavelength band from the radio to the gamma-ray.   Astrophysicists: Browse 2,200+ codes in the Astrophysics Source Code Library
    


```python

```
