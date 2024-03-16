# -*- coding: utf-8 -*-
"""
@title: Basic Concepts of Python Programming
@author: Assoc. Prof. Elif Kartal
@date: March 14, 2024
"""
# Exercises 1
# Defining variables
x = 35
y = 10
z = "50"
isinstance(x, object) # x bir object midir?
isinstance(x, int) # x bir integer mıdır?
isinstance(y, object) # y bir object midir?
isinstance(y, str)   # y bir string midir?
isinstance(z, object) # z bir object midir?
isinstance(z, int) # z bir integer mıdır?
# Exercises 2
x
id(x)
y
id(y)
y += 1
id(y)
z
id(z)
z += " is enough"
z
id(z)
# New example
fav_song = "The world is not enough"
fav_song[4] 
id(fav_song)
#fav_song[4] = "w" # can not writable because of string type is immutable . So we can not change the value of the string.
# List Type
m_list = list(fav_song)
m_list
id(m_list)
m_list[4]
m_list[4] = "w"
m_list
id(m_list)
m_list.append("h")
m_list
id(m_list)
#Memory Management, Lists, and Loops
#Data Structures & Management
#Assoc. Prof. Elif KARTAL
# Exercises 3
a = 1
id(a)
b = a
id(b)
b is a
b += 1
b is a
x = 1500
id(x)
y = 1500
id(y)
x is y
# A simple class example in Python
class Pets:
 def __init__(self, n, g, a):
    self.nickname = n
    self.gender = g
    self.age = a

my_pet1 = Pets("Safyuz", "Male", 11)
print(my_pet1.nickname)
print(my_pet1.gender)
print(my_pet1.age)
# Another class example
class Pets:
 def __init__(self, n, g, a):
    self.nickname = n
    self.gender = g
    self.age = a

 def show_info(self):
    return f"Nickname: {self.nickname}, Gender: {self.gender}, Age: {self.age}."
my_pet2 = Pets("Misik", "Male", 13)
my_pet2.show_info()
isinstance(my_pet2, Pets)
#Memory Management, Lists, and Loops
#Data Structures & Management
#Assoc. Prof. Elif KARTAL
"""
Assignment:
Create a Person class has three attributes: name, age, and gender.
The introduce() method should be a function that takes no arguments (other
than self, which refers to the instance of the class) and returns a string
introducing the person with their name, age, and gender.
"""
# Exercises 4
a = 300
id(a)
b = 300
id(b)
a is b
a = -50
b = -50
a is b
c = "Garbage"
id(c)
d = "Garbage"
id(d)
c is d
e = "Garbage!"
f = "Garbage!"
id(e)
id(f)
e is f
#Memory Management, Lists, and Loops
#Data Structures & Management
#Assoc. Prof. Elif KARTAL
# Back to the lists in Python
my_stdnts = ["beratcan", "berkay", "eyyüp", "furkan",
 "güz", "irem", "kaan", "yusuf"]
type(my_stdnts) # Listedeki elemanların tipi
len(my_stdnts) # Listedeki eleman sayısı
my_stdnts[0] # Listenin ilk elemanı
my_stdnts[2] # Listenin 3. elemanı
my_stdnts[-2] # Listenin sondan 2. elemanı
my_stdnts[-3] # Listenin sondan 3. elemanı
my_stdnts[0:4] # Listenin 0. indeksinden 4. indeksine kadar olan elemanlar
my_stdnts[4:] # Listenin 4. indeksinden sona kadar olan elemanlar
my_stdnts[-3:] # Listenin sondan 3. indeksinden sona kadar olan elemanlar Yani şu elemanı yazdır: "irem", "kaan", "yusuf"
my_stdnts[::5] # Listenin 5. indeksine kadar olan elemanlar 
my_stdnts[0:len(my_stdnts):5] # Bu kod da yukarıdaki kodla aynı işi yapar.
my_stdnts[::-1] # Listenin ters çevrilmiş hali
log_list = [True, False, False, True] # Boolean tipinde bir liste
mixed_list = ["A", "white rabbit", True, 1, 1.5] # Karışık tipde bir liste
mixed_list 
mixed_list[1] = "black rabbit" # Listenin 1. indeksindeki elemanı değiştir
mixed_list 
# Using a list() constructor: 
count_to_5 = list(("eins", "zwei", "drei", "vier", "fünf")) # Bu kod ile count_to_5 adında bir liste oluşturduk.
ml = [1,2,3,4,5,6,7,8,9,10] # ml adında bir liste oluşturduk. 
# adding an element to the end of the list.
id(ml) # ml'nin bellekteki adresini al
ml.append(11) # ml'nin sonuna 11 ekle
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,3,4,5,6,7,8,9,10,11 yazdır.
# adding an element at a specific index in the list
ml.insert(2, 20) # ml'nin 2. indeksine 20 ekle
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,20,3,4,5,6,7,8,9,10,11 yazdır.
ml.insert(10, 20) # ml'nin 10. indeksine 20 ekle
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,20,3,4,5,6,7,8,9,10,20,11 yazdır.
# removing the first occurrence of an element from the list.
ml.remove(20) # ml'den 20'yi çıkar
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,3,4,5,6,7,8,9,10,20,11 yazdır.
# removing and returning the last element in the list
last_item = ml.pop() # ml'nin son elemanını çıkar ve last_item adında bir değişkene ata
print(last_item) # last_item'ı ekrana yazdır. Yani ekranda 11 yazdır.
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,3,4,5,6,7,8,9,10,20 yazdır.
# returning the index of the first occurrence of an element in the list
ind = ml.index(20) # ml'nin içindeki 20'nin indeksini bul ve ind adında bir değişkene ata
print(ind)  # ind'yi ekrana yazdır. Yani ekranda 9 yazdır.
#Memory Management, Lists, and Loops
#Data Structures & Management
#Assoc. Prof. Elif KARTAL
# sorting the elements in the list in ascending order
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,3,4,5,6,7,8,9,10,20 yazdır.
ml.sort() # ml'yi küçükten büyüğe sırala
print(ml) # ml'yi ekrana yazdır. Yani ekranda 1,2,3,4,5,6,7,8,9,10,20 yazdır.
# reversing the order of the elements in the list.
ml.reverse() # ml'nin elemanlarını ters çevir
print(ml)
# creating an empty list
my_list = []
my_list.append("A") # my_list'in sonuna "A" ekle
my_list.append("B") # my_list'in sonuna "B" ekle
my_list.append("C") # my_list'in sonuna "C" ekle
# Use a loop to print all odd numbers in the list.
for i in ml: # ml'deki her bir eleman için
 if i % 2 == 1: # eğer i'nin 2'ye bölümünden kalan 1 ise. Yani i tek sayı ise
    print(i) # i'yi ekrana yazdır
# Write a Python program to find the sum of all elements in a given list.


my_list = [10, 20, 30, 40, 50]
total = 0 # toplam değişkenine 0 ata
for i in my_list: # my_list'teki her bir eleman için
 total += i # toplam değişkenine i'yi ekle. Yani sonuç olarak toplam değişkeni my_list'teki tüm elemanların toplamı olacak.
print("Sum of all elements in the list:", total)



# Have a new solution?
# ...
sum(my_list) # my_list'teki tüm elemanların toplamını bulur.
# Write a Python program to find the largest and smallest number in a given list.
my_list = [100, 20, 3000, 140, 50] # my_list adında bir liste oluştur
# set initial values for min and max
min_num = my_list[0] # min_num'a my_list'in ilk elemanını ata
max_num = my_list[0] # max_num'a my_list'in ilk elemanını ata
# iterate through the list with a for loop
for i in my_list: # my_list'teki her bir eleman için
 if i < min_num: # eğer i min_num'dan küçükse   
    min_num = i # min_num'a i'yi ata
 elif i > max_num: # eğer i max_num'dan büyükse
    max_num = i # max_num'a i'yi ata
# print the results
print("The largest number is:", max_num)
print("The smallest number is:", min_num)



# Have a new solution?
# ...
min(my_list) # my_list'teki en küçük elemanı bulur.
max(my_list) # my_list'teki en büyük elemanı bulur.
#Memory Management, Lists, and Loops
#Data Structures & Management
#Assoc. Prof. Elif KARTAL
# Create a list of integers and remove all even numbers from the list. Print
#the modified list.
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10] # numbers adında bir liste oluştur
numbers = [num for num in numbers if num % 2 != 0] # numbers'ın içindeki her bir eleman için eğer elemanın 2'ye bölümünden kalan 0 değilse elemanı numbers'a ata
print(numbers) # numbers'ı ekrana yazdır


# Exercises 3
a = 1 # a'ya 1 ata
id(a) # a'nın bellekteki adresini al
b = a # b'ye a'yı ata
id(b) # b'nin bellekteki adresini al
b is a # Bu kod ile b ve a'nın bellekteki adreslerini karşılaştırıyoruz. Eğer b ve a'nın bellekteki adresleri aynı ise True, değilse False döner. 
b += 1 # b'ye 1 ekle
b is a # Bu kod ile b ve a'nın bellekteki adreslerini karşılaştırıyoruz. Eğer b ve a'nın bellekteki adresleri aynı ise True, değilse False döner.
x = 1500 # x'e 1500 ata
id(x) # x'in bellekteki adresini al
y = 1500 # y'ye 1500 ata
id(y) # y'nin bellekteki adresini al
x is y # Bu kod ile x ve y'nin bellekteki adreslerini karşılaştırıyoruz. Eğer x ve y'nin bellekteki adresleri aynı ise True, değilse False döner.


# A simple class example in Python
class Pets: # Pets adında bir sınıf oluştur
 def __init__(self, n, g, a): #Bu kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a
   self.nickname = n # Bu satırdaki kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a
   self.gender = g # Bu satırdaki kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a
   self.age = a # Bu satırdaki kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a

my_pet1 = Pets("Safyuz", "Male", 11) # my_pet1 adında bir nesne oluştur
print(my_pet1.nickname) # my_pet1'in nickname özelliğini ekrana yazdır
print(my_pet1.gender) # my_pet1'in cinsiyet özelliğini ekrana yazdır
print(my_pet1.age) # my_pet1'in age özelliğini ekrana yazdır
# Another class example
class Pets: # Pets adında bir sınıf oluştur
 def __init__(self, n, g, a): #Bu kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a
   self.nickname = n # Bu satırdaki kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a
   self.gender = g # Bu satırdaki kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a
   self.age = a # Bu satırdaki kod ile sınıfın özelliklerini belirliyoruz. Bu sınıfın özellikleri : n, g, a

 def show_info(self):
   return f"Nickname: {self.nickname}, Gender: {self.gender}, Age:  {self.age}." # Bu kod ile sınıfın özelliklerini ekrana yazdırıyoruz.
my_pet2 = Pets("Misik", "Male", 13) # my_pet2 adında bir nesne oluştur
my_pet2.show_info() # my_pet2'nin show_info özelliğini ekrana yazdır
isinstance(my_pet2, Pets) # my_pet2 bir Pets nesnesi midir?
#Memory Management, Lists, and Loops
#Data Structures & Management
#Assoc. Prof. Elif KARTAL
"""
Assignment:
Create a Person class has three attributes: name, age, and gender.
The introduce() method should be a function that takes no arguments (other
than self, which refers to the instance of the class) and returns a string
introducing the person with their name, age, and gender.
"""
# Exercises 4
a = 300 # a'ya 300 ata
id(a) # a'nın bellekteki adresini al 
b = 300 # b'ye 300 ata
id(b) # b'nin bellekteki adresini al
a is b # Bu kod ile a ve b'nin bellekteki adreslerini karşılaştırıyoruz. Eğer a ve b'nin bellekteki adresleri aynı ise True, değilse False döner.
a = -50 # a'ya -50 ata
b = -50 # b'ye -50 ata
a is b # Bu kod ile a ve b'nin bellekteki adreslerini karşılaştırıyoruz. Eğer a ve b'nin bellekteki adresleri aynı ise True, değilse False döner.
c = "Garbage" # c'ye "Garbage" ata
id(c)  # c'nin bellekteki adresini al
d = "Garbage" # d'ye "Garbage" ata
id(d) # d'nin bellekteki adresini al
c is d # Bu kod ile c ve d'nin bellekteki adreslerini karşılaştırıyoruz. Eğer c ve d'nin bellekteki adresleri aynı ise True, değilse False döner.
e = "Garbage!" # e'ye "Garbage!" ata
f = "Garbage!" # f'ye "Garbage!" ata
id(e) # e'nin bellekteki adresini al
id(f) # f'nin bellekteki adresini al
e is f # Bu kod ile e ve f'nin bellekteki adreslerini karşılaştırıyoruz. Eğer e ve f'nin bellekteki adresleri aynı ise True, değilse False döner.