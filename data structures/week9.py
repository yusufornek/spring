#Linked - List nedir? 
#Linked listler, birbirine bağlı düğümlerden oluşan bir veri yapısıdır. Her düğüm, veriyi ve bir sonraki düğümün adresini içerir.
#KSS : Singly and doubly linked listler vardır. Singly linked listlerde her düğüm bir sonraki düğümün adresini içerir. Doubly linked listlerde ise her düğüm bir sonraki ve bir önceki düğümün adresini içerir.
# Singly and doubly linked listler ile ilgili görsel soru gelebilir. Grafik verilip hangi linked list olduğu sorulabilir vs.
#Noncontigous memory: Bellekte yan yana değillerdir.
#Noncontigous nodes: Düğümler bellekte yan yana değillerdir.
#Bu düğümlerdeki adres şu demektir: Her düğüm, veriyi ve bir sonraki düğümün adresini içerir.
#MSS : The structure of a linked list önemli, çıkabilir.
#Pointer : Bellekte bir düğümün adresini tutar.
#Performans Karşılaştırması : Lists vs Linked Lists
#Lists: Eleman ekleme ve çıkarma işlemleri zaman alır.
#Linked Lists: Eleman ekleme ve çıkarma işlemleri hızlıdır.
#Lists: Elemanları bellekte yan yana tutar.
#Linked Lists: Elemanları bellekte yan yana tutmaz.
#Time Complexity: Lists vs Linked Lists
#Lists: Eleman ekleme ve çıkarma işlemleri O(n) karmaşıklığına sahiptir.
#Linked Lists: Eleman ekleme ve çıkarma işlemleri O(1) karmaşıklığına sahiptir.

# liste = [1,2,3,4,5]
# print(liste)
# liste.append(6)

# print(liste)
# liste.insert(0,1)
# print(liste)

# m_list = [1,2,3,4,5]

# for i in m_list:
#     print(i)


# my_list = [5, 200, 862, 19, 86, 22, 14, 103, 818, 25, 49, 500, 15]


# def findmyItem(x, val):
#     for i in range(0, len(x)):
#         if x[i] == val:
#             return i
#             break
#         else:
#             continue
#     return -1
# print(findmyItem(my_list, 103))
# print(findmyItem(my_list, 5)) #Best Case çünkü eleman burada ve ilk sırada.
# print(findmyItem(my_list, 687654)) #Worst Case çünkü eleman burada yok ya da son sırada da olabilir.

# #Bu fonksiyona göre best case ve worst case durumları nedir?
# #Best case: Aranan elemanın listede ilk sırada olması durumunda O(1) karmaşıklığına sahiptir.
# #Worst case: Aranan elemanın listede olmaması durumunda O(n) karmaşıklığına sahiptir. 


my_list = [5, 200, 862, 19, 86, 22, 14, 103, 818, 25, 49, 500, 15]

print(max(my_list))

def enbuyukEleman(x):
    elma = 0
    buyukolan = x[0]
    for i in range(1, len(x)):
        if x[i] > buyukolan:
            buyukolan = x[i]
            elma = elma + 1
        else:
            elma = elma + 1
            continue
    return elma
    return buyukolan
print(enbuyukEleman(my_list))


#o(n^2) Simple Multiplication Table
n = 10
for i in range(1, n+1):
    for j in range(1, n+1):
        print(1, "x", j, "=", i*j)


#o(2^n) Fibonacci Series

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
for i in range(1, 11):
    print(fibonacci(i))

my_tupple = ("asd", "adglkmdgFSDKsfg")
my_list = list(my_tupple)
for i in range (len(my_tupple)):
    upper = my_list[i].upper()
    print(upper)


