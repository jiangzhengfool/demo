# -*- codeing:utf-8 -*-
from  bs4 import BeautifulSoup
path ='https://www.icourse163.org/university/CUFE#/c'
with open(path,'r') as wb_data :
     Soup=BeautifulSoup(wb_data,'lxml')
     print(wb_data);
