# -*- coding: utf-8 -*-
"""
Created on Tue Sep 11 18:24:19 2018

@author: serha
"""

# %%

# list

liste = [1,2,3,4]
type(liste)

liste_str = ["ocak","subat","mart"]
type(liste_str)

value = liste[1]
print(value)

last_value = liste[-1]
print(last_value)

liste_divide = liste[1:3]
print(liste_divide)

liste.append(7)

# %%

liste_2 = [2,6,8,5]

   liste_2.clear()
   
   liste_3 = [1,2,3]
   x = liste_3.copy()
   print(x)
   
   
   # %%
   
   # dictionary
   
   dictionary = {"osman":45,"rahmi":24,"memo":23}
   
   
def deneme():
	dictionary = {"osman":45,"rahmi":24,"memo":23}
	return dictionary

dic = deneme()

# %%

# Quizzz if-else

# metod yazılıcak
 #input integer yıllar
 # output yuzyıl
	# 1640. yıl == 17.yuzyıl
	# 109.  yıl == 2. yuzyıl
	# 2000. yıl == 20.yuzyıl
	
	# 001 – 100 Birinci yüzyıl

	# 101 – 200 İkinci yüzyıl

	# 1601 – 1700 Onyedinci yüzyıl

	# 1701 – 1800 Onsekizinci yüzyıl

	# 1901 – 2000 Yirminci yüzyıl 
	
		# input = year >> 1 <= year	<= 2005

def year2century(year):
	str_year = str(year)
	if(len(str_year)<3): # 89 3 79
		return 1
	elif(len(str_year) == 3):
		if(str_year[1:3]=="00"):
			return int(str_year[0]) #100 200 300 
		else:
			return int(str_year[0])+1
	else:
		if(str_year[1:4]=="00"):
			return int(str_year[:2])
		else:
			return int(str_year[:2])+1
	
	# %%
    
	# for loop & while loop
  
  
for each in range(1,15):
	print(each)        
	
for each in "ankara istanbul":
	print(each)



for each in "ankara istanbul".split():
	print(each)

liste = [1,2,3,4,5,6,7,8,9]

count = 0

for each in liste:
	count = count + each
	
print(count)


  # while loop
  
 i = 0
while(i<4):
	i = i + 1
	print(i) 
	
	
each = 0
uzunluk = len(liste)
count = 0

while(each<uzunluk):
	count = count + liste[each]
	each = each + 1
	print(count)
	
deger = 0
for jon in range(1,10):
	deger = deger + jon
	
print(deger)
# %%

		  # Quizz 
		  
		        
 # verilen listedeki en küçük sayıyı bulmak
 
liste = [1,2,3,6,5,98,755,-5,65,-96,0]

en_buyuk = 0
count = 0
for each in liste:
	if(count<len(liste)):
		if(each>liste[count]):
			en_buyuk=each
		else:
			continue
	count = count + 1
		
print(en_buyuk)

 
en_kucuk = 10000

for each in liste:
	if(each<en_kucuk):
		en_kucuk=each
	else:
		continue

print(en_kucuk)
# %%

  # örnekler
  # kullanıcı tarafından girilen iki sayıyı toplama:
  num1 = int(input("birinci sayıyı giriniz :"))
num2 = int(input("ikinci sayıyı giriniz :"))
 
 
# iki sayının toplamı
sum = int(num1) + int(num2)
 
# sonucu yazdırma
print('{0} + {1} = {2}'.format(num1, num2, sum))

	
		 # kullanıcı tarafından girilen iki sayının ortalamasını alma:
	 
num1 = int(input("Birinci sayiyi giriniz :"))
num2 = int(input(" İkinci sayiyi giriniz :"))

sum = ((int(num1) + int(num2))/2)

print('{0}+{1} = {2}'.format(num1, num2, sum))

	   
   
		# aralarında virgül ile girilen sayıları toplayama:
		
numaralar = input("sayıları aralarında virgül koyarak giriniz:")
print("Girdiğiniz sayılar: {0}".format(numaralar))
		
 numaralar_2=numaralar.split(",")
# print("Girdiğiniz sayılar: {0}".format(numaralar_2))		 

toplam = 0

for each in numaralar_2:
	toplam = toplam + int(each)
	
	
print("GİRDİĞİNİZ SAYILARIN ORTALMASI:{0:.2f} ".format(toplam / len(numaralar_2)))
   
   
   
   
   
   
   
   
   
   
   
   
   
   