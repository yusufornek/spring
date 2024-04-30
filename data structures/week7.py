

my_set : set()
my_set = {1, 2, 3, 4, 5}
print(my_set)
print(type(my_set))

my_second_set = set()
my_second_set = {1, 2, 3, 4, 5}
my_second_set.add(6)
fruits = {"apple", "banana", "cherry"}

add = lambda x,y: x+y #Bu fonksiyon x ve y yi toplar ve sonucu ekler.
print(add(2,3)) 

for x in my_set:
    print(x)

for i in my_second_set:
    print(i)

my_member = 6
if my_member in my_set:
    Print(my_member, "is in the set")
else:
    print(my_member, "is not in the set")

print(my_set.add(5))

print(my_set.remove(5))
print(my_set)
print(my_set.pop())
print(my_set) # Pop fonksiyonu setin ilk elemanını siler.  Sınav sorusu olabilir.

bir_tane_liste = [1, 2, 3, 4, 5]
print(type(bir_tane_liste))
bir_tane_liste = set(bir_tane_liste)
print(bir_tane_liste)
print(type(bir_tane_liste))
print(bir_tane_liste) # Listeyi sete çevirir ve yapısını değiştirir. Yeni yapısı set olur. Set ile liste arasındaki farklar nelerdir? Sınav sorusu olabilir.
numbers ={10, 201, 30, 404, 50, 60, 707, 80, 909, 100}
evens = {num for num in numbers if num % 2 == 0}
print(evens) # Set yapısı kullanarak numbers setindeki çift sayıları bulur ve evens setine ekler kanka.

odds = {num for num in numbers if num % 2 != 0}
print(odds)

divisible_three = {num for num in numbers if num % 3 == 0}
print(divisible_three)

numbers ={10, 201, 30, 404, 50, 60, 707, 804, 909, 104}
ending_4 = {num for num in numbers if num % 10 == 4}
print(ending_4) 
numbers ={10, 201, 30, 404, 50, 60, 707, 804, 909, 104}
ending_4 = {num for num in numbers if str(num).endswith("4")}
print(ending_4)



set1 = {10, 20, 30}
set2 = {20, 30, 40}

for num1 in set1:
    for num2 in set2:
        if num1 == num2:
            print(num1)
my_intersection = set1.intersection(set2)
print(my_intersection) # İki setin kesişimini bulur ve my_intersection setine ekler.


a = set("apple")
print(a) # Set yapısı kullanarak apple kelimesini a setine ekler ve a setini yazdırır.
b = set("banana")
print(b) # Set yapısı kullanarak banana kelimesini b setine ekler ve b setini yazdırır.

a &= b # İki setin kesişimini bulur ve a setine ekler.
a = set("apple")
b = set("banana")
a|= b # İki seti birleştirir ve a setine ekler.
the_union = a.union(b) # İki seti birleştirir ve the_union setine ekler.

a-=b # İki setin farkını bulur ve a setine ekler.
b -= a # İki setin farkını bulur ve b setine ekler.

the_diff1 = a.difference(b) # İki setin farkını bulur ve the_diff1 setine ekler.
the_diff2 = b.difference(a) # İki setin farkını bulur ve the_diff2 setine ekler.

#Lambda fonksiyonu

add = lambda x,y: x+y
print(add(2,3)) # Bu fonksiyon x ve y yi toplar ve sonucu ekler.

#Sorting a list of tuples based on the second element of the tuples
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')] # İki elemanlı tuple listesi oluşturur.
pairs.sort(key=lambda pair: pair[1]) # Bu fonksiyon listeyi sıralar ve sıralama kriteri olarak lambda fonksiyonunu kullanır.
print(pairs) # Bu fonksiyon listeyi sıralar ve sıralama kriteri olarak lambda fonksiyonunu kullanır.

#Filtering a list of numbers to get even numbers

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] # Liste oluşturur.
even_numbers = list(filter(lambda x: x % 2 == 0, numbers)) # Bu fonksiyon listeyi filtreler ve filtreleme kriteri olarak lambda fonksiyonunu kullanır.
print(even_numbers) # Bu fonksiyon listeyi filtreler ve filtreleme kriteri olarak lambda fonksiyonunu kullanır.

names = ["Elif", "Irem", "Emanuel"] # Liste oluşturur.
def my_greet(name): # Fonksiyon oluşturur. 
    return f"Hello, {name}" # Bu fonksiyon name değişkenini alır ve Hello, name şeklinde bir çıktı verir.

formatted = map(my_greet, names) # Bu fonksiyon listeyi map fonksiyonu ile dönüştürür ve my_greet fonksiyonunu kullanır.

for message in formatted: # Bu döngü formatted listesini döner ve her bir elemanı message değişkenine atar.
    print(message) # Bu fonksiyon message değişkenini yazdırır. 
