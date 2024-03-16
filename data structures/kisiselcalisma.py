var = ["elma", "armut", "muz"] # Var, bir liste olup, içerisinde 3 adet string bulunduruyor.
print(var) # Var'ı ekrana yazdır.

List = [['Geeks', 'For'], ['Geeks']] # List, bir liste olup, içerisinde 2 adet liste bulunduruyor.
print(List[0][1]) # List'in 0. indeksindeki listenin 1. indeksindeki elemanı ekrana yazdır.
print(List[1][0]) # List'in 1. indeksindeki listenin 0. indeksindeki elemanı ekrana yazdır.

liste = ["Merhaba", "Dünya", 1, 2, 3, 4] # Liste, bir liste olup, içerisinde 4 adet string ve 2 adet integer bulunduruyor.
print(liste[-1]) # Liste'nin son elemanını ekrana yazdır.
print(liste[-5]) # Liste'nin sondan 5. elemanını ekrana yazdır. Yani ekrana "Dünya" yazdırılacak.   
print(len(liste)) # Liste'nin uzunluğunu ekrana yazdır. Yani listenin içerisinde kaç adet eleman bulunduğunu ekrana yazdır.

#string = input("Bir string giriniz : ") # Kullanıcıdan bir string al.
#lst = string.split() # Alınan string'i boşluklara göre ayır ve lst adında bir liste oluştur.
#print("The list is : " , lst) # lst'yi ekrana yazdır.

Liste2 = []
print("Initial blank List: ")
print(Liste2)
Liste2.append(1) # Liste2'ye 1 ekle. Append metodu, listenin sonuna eleman eklemek için kullanılır.
Liste2.append(2) # Liste2'ye 2 ekle. Append metodu, listenin sonuna eleman eklemek için kullanılır.
Liste2.append(4) # Liste2'ye 4 ekle. Append metodu, listenin sonuna eleman eklemek için kullanılır.
print("\nList after Addition of Three elements: ")
print(Liste2) # Liste2'yi ekrana yazdır. Yani 1, 2 ve 4'ü ekrana yazdır.
for i in range(1, 4): # 1'den 4'e kadar olan sayıları i'ye ata.
    Liste2.append(i) # Liste2'ye i'yi ekle. Append metodu, listenin sonuna eleman eklemek için kullanılır.
print("\nList after Addition of elements from 1-3: ") # 1-3 arasındaki elemanları ekledikten sonra Liste2'yi ekrana yazdır.
print(Liste2) # Liste2'yi ekrana yazdır.