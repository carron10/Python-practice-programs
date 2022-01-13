import pandas as pd

df=pd.read_excel(r'C:\Users\Muleya\Desktop\PYTHON PROJECTS\fashion.xlsx')
catetory=df['CARTEGORY']
price=df['PRICE']
years=df['YEARS']
description=df['DESCRIPTION']
name=df['PRODUCT _NAME']
image=df['IMAGE']
size=df['SIZE']
i=0;
print("INSERT INTO  products(category,product_name,size,years,picture,price,description) values")
while i<(len(df)):
    
    name[i]=name[i].replace("'","\'\'")
    size[i]=size[i].replace("'","''")
    years[i]=years[i].replace("'","''")
    image[i]=image[i].replace("'","''")
    price[i]=price[i].replace("'","''")
    description[i]=description[i].replace("'","''")
    name[i]=name[i].strip()
    size[i]=size[i].strip()
    years[i]=years[i].strip()
    image[i]=image[i].strip()
    price[i]=price[i].strip()
    description[i]=description[i].strip()
    a=',(\'men\',\''+name[i]+"\',\'"+size[i]+"\',\'"+years[i]+"\',\'men/"+image[i]+"\',\'"+price[i]+"\',\'"+description[i]+"\')"
    
    print(a)
    i+=1
print(";")
