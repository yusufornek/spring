# 1. Create a list of your favorite fruits and print the first and last elements.
# Favori meyvelerinizden bir liste oluşturun ve listenin ilk ve son elemanlarını yazdırın.
favorite_fruits = ["elma", "muz", "portakal", "üzüm", "karpuz"]
print("İlk meyve:", favorite_fruits[0])  # Listenin ilk elemanını yazdırır
print("Son meyve:", favorite_fruits[-1])  # Listenin son elemanını yazdırır

# 2. Create an empty list and add five names using the append() method. Print the final list.
# Boş bir liste oluşturun ve append() yöntemini kullanarak beş isim ekleyin. Son listeyi yazdırın.
names = []
names.append("Ali")  # İsimleri ekler
names.append("Ayşe")
names.append("Ahmet")
names.append("Fatma")
names.append("Mehmet")
print("İsimler listesi:", names)  # Son listeyi yazdırır

# 3. Create a list of integers from 1 to 10 and use a loop to print all even numbers in the list.
# 1'den 10'a kadar olan tam sayıları içeren bir liste oluşturun ve listedeki tüm çift sayıları yazdırmak için bir döngü kullanın.
numbers = list(range(1, 11))
print("Çift sayılar:")
for num in numbers:
    if num % 2 == 0:
        print(num)  # Çift sayıları yazdırır

# 4. Create a list of strings and sort it in alphabetical order. Print the sorted list.
# Bir dize listesi oluşturun ve alfabetik sıraya göre sıralayın. Sıralı listeyi yazdırın.
strings = ["elma", "muz", "çilek", "armut", "karpuz"]
sorted_strings = sorted(strings)  # Listeyi alfabetik sıraya göre sıralar
print("Sıralı dizeler:", sorted_strings)  # Sıralı listeyi yazdırır

# 5. Write a Python program to find the sum of all elements in a given list.
# Verilen bir listedeki tüm elemanların toplamını bulan bir Python programı yazın.
numbers = [10, 20, 30, 40, 50]
sum_of_numbers = sum(numbers)  # Listenin tüm elemanlarının toplamını bulur
print("Sayıların toplamı:", sum_of_numbers)  # Toplamı yazdırır

# 6. Create a list of strings and use a loop to print all strings that start with the letter 'A'.
# Bir dize listesi oluşturun ve 'A' harfi ile başlayan tüm dizeleri yazdırmak için bir döngü kullanın.
strings = ["armut", "elma", "avokado", "çilek", "ananas"]
print("'A' ile başlayan dizeler:")
for string in strings:
    if string.startswith("A"):
        print(string)  # 'A' ile başlayan dizeleri yazdırır

# 7. Create a list of integers and use a loop to calculate the product of all numbers in the list that are greater than 5.
# Bir tam sayı listesi oluşturun ve listedeki 5'ten büyük tüm sayıların çarpımını hesaplamak için bir döngü kullanın.
numbers = [2, 3, 6, 8, 10]
product = 1
for num in numbers:
    if num > 5:
        product *= num  # 5'ten büyük sayıların çarpımını hesaplar
print("5'ten büyük sayıların çarpımı:", product)  # Çarpımı yazdırır

# 8. Create a list of strings and use a loop to create a new list of strings where all strings are in uppercase. Print the new list.
# Bir dize listesi oluşturun ve bir döngü kullanarak tüm dizelerin büyük harfli olduğu yeni bir dize listesi oluşturun. Yeni listeyi yazdırın.
strings = ["elma", "muz", "çilek"]
uppercase_strings = [s.upper() for s in strings]  # Tüm dizeleri büyük harfli hale getirir
print("Büyük harfli dizeler:", uppercase_strings)  # Yeni listeyi yazdırır

# 9. Create a list of strings and use a loop to create a new list of strings where all strings are at least 5 characters long. Print the new list.
# Bir dize listesi oluşturun ve bir döngü kullanarak tüm dizelerin en az 5 karakter uzunluğunda olduğu yeni bir dize listesi oluşturun. Yeni listeyi yazdırın.
strings = ["elma", "muz", "çilek", "armut", "kivi"]
long_strings = [s for s in strings if len(s) >= 5]  # En az 5 karakter uzunluğunda olan dizeleri seçer
print("En az 5 karakterli dizeler:", long_strings)  # Yeni listeyi yazdırır

# 10. Write a function that takes a list of integers as input and returns the largest integer in the list. Then call the function with argument [40, 180, 10, 9000, 5456].
# Bir tam sayı listesi alan ve listenin en büyük tam sayısını döndüren bir işlev yazın. Ardından, işlevi [40, 180, 10, 9000, 5456] argümanıyla çağırın.
def find_largest_integer(nums):
    return max(nums)  # En büyük sayıyı bulur

numbers = [40, 180, 10, 9000, 5456]
largest_number = find_largest_integer(numbers)
print("En büyük sayı:", largest_number)  # En büyük sayıyı yazdırır

# 11. Create a class that has five attributes and two methods.
# Beş özelliği ve iki yöntemi olan bir sınıf oluşturun.
class MyClass:
    def __init__(self, attr1, attr2, attr3, attr4, attr5): # Sınıfın özelliklerini tanımlar. Ayrıca __init__ şu demek: "initialize" yani başlatmak, başlangıç yapmak.
        self.attr1 = attr1 # Beş özelliği tanımlar
        self.attr2 = attr2
        self.attr3 = attr3
        self.attr4 = attr4
        self.attr5 = attr5
    
    def method1(self): # Sınıfın birinci yöntemini tanımlar
        pass # Yöntemin içeriğini tanımlar
    
    def method2(self): # Sınıfın ikinci yöntemini tanımlar
        pass # Yöntemin içeriğini tanımlar

# Bonus Question: Write a function that takes a list of strings as input and returns a new list of the same strings but with all vowels removed. Then call the function with argument ["elif", "KARTAL"]. Hint: Use nested for :)
# Bir dize listesi alan ve aynı dizelerin tüm ünlülerini kaldırılmış yeni bir liste döndüren bir işlev yazın. Ardından, işlevi ["elif", "KARTAL"] argümanıyla çağırın. İpucu: İç içe for kullanın :)
def remove_vowels(strings): # Ünlüleri kaldırır
    vowels = "aeiouAEIOU" # Ünlüleri tanımlar
    result = [] # Yeni listeyi tanımlar
    for string in strings: # Dize listesinde döner 
        new_string = ''.join([char for char in string if char not in vowels])  # Ünlüleri kaldırır
        result.append(new_string) # Yeni dizeyi listeye ekler
    return result # Yeni listeyi döndürür

words = ["elif", "KARTAL"]  # Dize listesi
new_words = remove_vowels(words) # Ünlüleri kaldırılmış yeni listeyi oluşturur
print("Ünlüler olmadan kelimeler:", new_words)  # Ünlüleri kaldırılmış kelimeleri yazdırır
