# -*- coding: utf-8 -*-
"""
Created on Sun Aug 19 23:30:08 2018

@author: serha
"""
# %%
var1='10236'
# %%

# %% double

# int double

int_deneme=60

# %%

# %% built in function
#double=float= ondalikli sayi

float_deneme=-30.8
ondalikli_sayi=-65.98
sayi_1=-50
sayi_2=50.5

str_2='1653'
#%%

# %% user defined function
 #fonksiyon parametresi = input
 
 var1=30
 var2=67

def benim_function(a,b):
	
	"""
	parametre:
	return:
	"""
	output = ((a+b)*32)/((a-b)*2)
	return output
sonuc
 = benim_function2(var1,var2)

def benim_function2(x,y):
	output =  ((x+y)*32)/((x-y)*2)
	return output
sonuc2 = benim_function2(var1,var2)

def deneme1():
	print("hello world")
	
	
#%% default and flexible functions
	
	# default function cemberin cevre uzunlugu = 2*pi*r

def cember_cevresi(r,pi=3.14):
	"""
	cemberin cevresi hesapla
	input(parametre): r,pi
	output = cemberin cevresi

	#pi değişkeni default function olarak tanımlandı ve function 
	yazarken giriş parametresine pi tekrar yazmaya gerek yok#
	"""
	output = 2*3.148*r
	return output

  #flexible function
  
def hesapla(boy,kilo,*args):
	print(args)
	print(len(args))
	"""
	boy ve kiloya göre vücüt indeksi çıkarılacak
	input(parameter): boy, kilo
	output: vücut indeksi
	"""
	output = kilo/((boy/10)*(boy/10))*args[0]
	return output
#%% Quiz

# int variable yaş
# string name isim
	
# function print(len(),type(),float())
# *args soyisim
# default ayakkabı nuarası

yas = 35
isim = ali	

def kisi_parametre(yas,isim,ayakkabi_no=42,*args):
	"""input(parameters)=yas,isim, ayakkabı_no,soyisim
	"""
	print(type(yas))
	
#%%
	
	def my_function(country="turkey"):
		print("i am from " + country)
		
		my_function("sweden")
		my_function("america")
		my_function()
	
	def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")

#%%

def my_function(isim,il="karabuk"):
	print( "ad:" + isim ,"sehir:" + il)
	
my_function("",)
my_function("mehmet","istanbul")
my_function("diyarbakir")

#%%

def my_function(x):
  return 5*x

print(my_function(3))
print(my_function(4))
print(my_function(5))
	
	
sonuc2 = lambda x: x*x
print(sonuc2(3)) 	
	
	
def sonuc(x):
	
	output= x*x
	return output
print(sonuc(3))
	
def my_function(n):
	lambda a:a*(n+1)

double_func = my_function(4)
single_func = my_function(5)

print(double_func(2))
print(single_func(7))
#%%	  
  
  def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11)) 
print(mytripler(11))

def myfunc(n):
  return lambda a : a * n

mytripler = myfunc(3)

print(mytripler(11))  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  