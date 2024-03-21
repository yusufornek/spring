"""s1=int(input("Enter a number:"))
s2=int(input("Enter another number:"))"""

"""theTotal=s1+s2;
theAverage=(s1+s2)/2
"print(theTotal)"
"print(theAverage)"""

def toplama(s1, s2):
    print("Toplam : ", s1+s2)
"toplama(s1, s2)"
"""toplama(7, 15)
toplama(s1=7, s2=8)
my_sum(a=3, b=5)
my_sum(3,5)
my_result=my_sum(3,7)"""
"""def sum_sub(a,b):
    return a+b, a-b 
my_sum, my_sub = sum_sub(3,5)
print(my_sum)
print(my_sub)"""

"""x = 20
def my_fun(x):
    x  = 10
    x += 1
    print(x)
    return(x) # Bu fonksiyon, sırasıyla şunu yapar: x'i 10 yapar, 1 ekler ve x'i yazdırır."""

"""print(x) #Ama x'in değeri değişmez, çünkü x'in değeri fonksiyonun dışında tanımlanmıştır.
my_fun(7) #Ama burada, fonksiyonun içindeki x'in değeri değişir."""

"""my_sum = lambda a, b: a+b
print(my_sum(3,5))"""

"""def find_minimum(numbers): #Bu fonksiyon, bir listenin en küçük elemanını bulur.
    return min(numbers)
print(find_minimum([3,5,7,1,4,9,8,6,2]))

def sum_of_elements(lst): #Bu fonksiyon, bir listenin elemanlarının toplamını hesaplar.
    return sum(lst)
print(sum_of_elements([3,5,7,1,4,9,8,6,2]))
def reverse_string(s): #Bu fonksiyon, bir stringi ters çevirir.
    return s[::-1]
print(reverse_string("hello")) #Bu fonksiyon, "hello" kelimesini "olleh" olarak yazdırır.
def is_palindrome(s):
    return s == s[::-1]
print(is_palindrome("757"))"""

def factorian(n):
    if n == 0:
        return 1
    else:
        return n * factorian(n-1)
print(factorian(5))












"""

def radius_of_circle(r): #Bu fonksiyon, yarıçapı r olan bir dairenin alanını hesaplar.
    return 3.14 * r**2 #3.4 Pi sayısını temsilen kısaltılmış olarak ifade ettim :)
print(radius_of_circle(5))



my_list = [3, 56, 566, 75]
def find_max(x):
    my_max=x[0]
    i = 1
    while i<len(x):
        if x[i]>my_max:
            my_max = x[i]
        i +=1
    return my_max
print(find_max(my_list))"""


    

"""def find_max(lst):
    while len(lst) > 1:
        if lst[0] > lst[1]:
            lst = lst[1:]
        else:

        

print(find_max([5, 7, 45, 1]))"""