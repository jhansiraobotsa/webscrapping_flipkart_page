import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
url='https://www.flipkart.com/mobiles/pr?sid=tyy%2C4io&p%5B%5D=facets.availability%255B%255D%3DExclude%2BOut%2Bof%2BStock&param=7564&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIlNob3AgTm93Il0sInZhbHVlVHlwZSI6Ik1VTFRJX1ZBTFVFRCJ9fX19fQ%3D%3D&fm=neo%2Fmerchandising&iid=M_b49965b5-ad80-4493-88b1-7a1828555879_3.Q1PDG4YW86MF&ppt=hp&ppn=homepage&ssid=paxle4idvk0000001669033731730&p%5B%5D=facets.brand%255B%255D%3DGoogle&ctx=eyJjYXJkQ29udGV4dCI6eyJhdHRyaWJ1dGVzIjp7InRpdGxlIjp7Im11bHRpVmFsdWVkQXR0cmlidXRlIjp7ImtleSI6InRpdGxlIiwiaW5mZXJlbmNlVHlwZSI6IlRJVExFIiwidmFsdWVzIjpbIkdPT0dMRSJdLCJ2YWx1ZVR5cGUiOiJNVUxUSV9WQUxVRUQifX19fX0%3D&otracker=clp_metro_expandable_3_5.metroExpandable.METRO_EXPANDABLE_GOOGLE_mobile-phones-store_0TAYGN3KGJ9F_wp2&fm=neo%2Fmerchandising&iid=M_23d8b3c8-365c-498a-a589-b5c65cf58855_5.0TAYGN3KGJ9F&ppt=hp&ppn=homepage&ssid=kyjzc6uo8w0000001684241327646'
r=requests.get(url)
soup=BeautifulSoup(r.text,'lxml')
name=soup.find_all("div",class_="_4rR01T")
rating=soup.find_all("div",class_="_3LWZlK")
ph_model=[]
storage=[]
ratings=''
ph_rating=[]
ph_storage=[]
for i in name:
    ph_model+=[i.text]
    x=re.findall("\d+ GB",i.text)
    storage+=x
for i in rating:
    ratings+=i.text
    ph_rating+=[ratings]
    ratings=''
phstorage=soup.find_all("li",class_="rgWa7D")

#phstorage1=phstorage.find_all(")
storage_ph=[]
for i in phstorage:
    storage_ph+=[i.text]
#print(storage)
#print(ph_model)
#print(ph_rating)
#print(storage_ph)
c=[]
c1=0
d=[]
for i in storage_ph:
    c+=[i]
    c1+=1
    if c1==6:
        d=d+[c]
        c1=0
        c=[]
#print(d)
phone_storage=[]
phone_display=[]
phone_camera=[]
phone_batter=[]
phone_processor=[]
phone_warrenty=[]
for i in range (len(d)):
    for j in range(len(d[i])):
        if j==0:
            phone_storage+=[d[i][j]]
        elif j==1:
            phone_display+=[d[i][j]]
        elif j==2:
            phone_camera+=[d[i][j]]
        elif j==3:
            phone_batter+=[d[i][j]]
        elif j==4:
            phone_processor+=[d[i][j]]
        else:
            phone_warrenty+=[d[i][j]]
#print(phone_storage)
#print(phone_display)
#print(phone_camera)
#print(phone_batter)
#print(phone_processor)
#print(phone_warrenty)
df=pd.DataFrame({"phone_model":ph_model,"phone_display":phone_display,"phone_camera":phone_camera,"phone_battery":phone_batter,"phone_processor":phone_processor,"phone_warrenty":phone_warrenty,"phone_rating":ph_rating})
#print(df)
df.to_csv("flipkart1.csv", mode='a', index=False, header=False)


