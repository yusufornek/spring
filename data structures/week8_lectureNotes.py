#List ile Array arasındaki farklar önemli. Listelerde her eleman farklı bir türde olabilir. Arraylerde ise aynı türde olmalıdır.
#Arrayler bellekte daha az yer kaplarlar. 

#Listler dinaimik olarak büyüyebilirler. Arrayler ise sabit boyutludur.
#Örneğin 4 elemanlı bir array oluşturduğumuzda, 5. elemanı ekleyemeyiz. Ancak listlerde ekleyebiliriz.
#Liste bu işlemi şöyle yapar: 1. listeyi kopyalar, 2. yeni elemanı ekler, 3. eski listeyi siler, 4. yeni listeyi eski listeye atar. 2 katına çıkartır.

#Lists are mutable yani değiştirilebilir. Arrayler ise değiştirilemez.
#Lists are flexible yani esnek. Arrayler ise sabit boyutludur.
#Lists are handy to use yani kullanışlıdır. Arrayler ise daha hızlıdır.
########################################################################################################################################################
#Listler ve tupller arasındaki farklar: 
#Listler [] ile tanımlanırken, tuppler () ile tanımlanır.
#Listler değiştirilebilirken, tuppler değiştirilemez. (tuple'lar immutable'dır.)
#Listler daha fazla yer kaplarlar.
#Tuple'lar daha hızlıdır çünkü değiştirilemezler.
#Listlerdeki elemanlar farklı türde olabilirken, tupplerde aynı türde olmalıdır.

#if the data needs to be modified, a list should be used. Otherwise, a tuple should be used.
########################################################################################################################################################
#Setler: 
#Setler {} ile tanımlanır.
#Elements of the set are not ordered yani sıralı değildir.
#It does not allow duplicate elements yani tekrar eden elemanlara izin vermez.
#It allows basic mathematical operations like union, intersection, difference, and symmetric difference. Yani birleşim, kesişim, fark ve simetrik fark gibi temel matematiksel işlemlere izin verir.
#MUHTEMEL SINAV SORUSU : For example, a list is given and has duplicate elements. If we want to remove the duplicate elements, we can convert the list to a set. Yani bir listeyi sete çevirerek tekrar eden elemanları silebiliriz.
########################################################################################################################################################
#Dictionary:
#Dictionaryler {} ile tanımlanır.
#Dictionaryler key-value çiftlerinden oluşur. Setlerde sadece elemanlar vardı. Dictionarylerde ise key-value çiftleri vardır.
#Dictionarylerde key'ler unique yani benzersiz olmalıdır. Aynı key'i birden fazla kez kullanamayız.
#Dictionary is mutable yani değiştirilebilir.
#Dictionarylerde key'ler immutable olmalıdır. Yani key'lerin değiştirilemez olması gerekir.
#Dictionarylerde key'ler sıralı değildir. Yani sıralı değildirler.
#Dictionarylerde elemanlar sıralı değildir. Yani sıralı değildirler.
#JSON formatı dictionary formatındadır. JSON dosyası şu demektir: JavaScript Object Notation.
#Set ile dictionary'nin geldiği veri yapısı hash table'dır. Hash table, key-value çiftlerini depolamak için kullanılır.
########################################################################################################################################################
#Hashing:
#Hashing, can be defined as the transformation of a string of characters into a usually shorter fixed-length value or key that represents the original string.
#Yani hashing, karakterlerin bir dizesinin genellikle daha kısa sabit bir uzunlukta bir değere veya anahtara dönüştürülmesi olarak tanımlanabilir.
#Hash tables stores key and value pairs. It uses a hash function to compute an index into an array of buckets or slots, from which the desired value can be found.
#Yani hash tabloları, anahtar ve değer çiftlerini depolar. İstenen değerin bulunabileceği bir dizi kovadan veya yuvadan bir dizine bir dizin hesaplamak için bir hash işlevi kullanır.
#Insert, get, delete supported by hash tables. Yani hash tabloları tarafından desteklenen ekleme, alma ve silme fonksiyon işlemleri vardır.
#Hashing gerçek hayatta çok kullanılır. Örneğin, parolaların hashlenmesi, veri tabanlarında verilerin saklanması, veri sıkıştırma, veri şifreleme gibi alanlarda kullanılır.
#Digital signature process şu şekilde gerçekleşir; Hash algoritm, private key encyption, network transmission, public key decryption.
#MD5 ve SHA-1 hash algoritmaları en çok kullanılan hash algoritmalarıdır. Bu algoritmalar şu yerlerde kullanılır: SSL certificates, VPN, SSH, IPsec, TLS, and HTTPS.
########################################################################################################################################################
#Arrays in Real Life: 
#Real Time Data Processing: Arrays are used to store data in real-time data processing. For example, in the stock market, arrays are used to store the stock prices.
#Image Processing: Arrays are used to store the pixel values of an image. For example, in image processing, arrays are used to store the pixel values of an image.
#Lists in Real Life:
#To-Do List: Lists are used to store the tasks that need to be done. For example, a to-do list is a list of tasks that need to be done.
#Shopping List: Lists are used to store the items that need to be bought. For example, a shopping list is a list of items that need to be bought.
#Tuples in Real Life:
#Coordinates: Tuples are used to store the coordinates of a point. For example, the coordinates of a point are stored in a tuple.
#Data Integrity: Tuples are used to store the data that should not be modified. For example, the data integrity of a database is maintained by storing the data in a tuple.
#Immutable Data: Tuples are used to store the data that should not be changed. For example, the configuration settings of a system are stored in a tuple.
#Sets in Real Life:
#Mathematics: Sets are used to represent the mathematical sets. For example, the set of natural numbers is represented by a set.
#Eliminating Duplicates: Sets are used to eliminate the duplicate elements from a list. For example, a set is used to remove the duplicate elements from a list.
#Membership Testing: Sets are used to test the membership of an element in a set. For example, a set is used to check if an element is present in a set.
#Dictionaries in Real Life:
#Caching: Dictionaries are used to cache the data. For example, a dictionary is used to store the data that is frequently accessed.
#Database Configuration: Dictionaries are used to store the configuration settings of a database. For example, the database configuration settings are stored in a dictionary.
########################################################################################################################################################
########################################################################################################################################################
########################################################################################################################################################
#Linked List:
#Linked listler, birbirine bağlı düğümlerden oluşan bir veri yapısıdır. Her düğüm, veriyi ve bir sonraki düğümün adresini içerir.
#Homojen yani aynı türde olmalıdır.
#Linear collection yani lineer bir koleksiyondur. Peşi sıra gelirler.
#Hiyerarchical collections: Ağaç yapısında kullanılır. Child-parent ilişkisi vardır.
#Graph collections: Graph yapısında kullanılır. Node-edge ilişkisi vardır. Köşe-kenar ilişkisi vardır. Bağlantılar vardır.
#Unoerdered collections: Sırasız koleksiyonlardır. Cannot meaningfully speak of an items's predecessor or successor, yani bir öğenin öncüsü veya halefi hakkında anlamlı bir şekilde konuşamazsınız.
#Features of connections: 
#Collections are typically dynamic yani dinamik olarak büyüyebilirler.
#Random Access and Contiguous Memory: Linked listlerde random access yoktur. Yani bir elemana erişmek için baştan başlamak gerekir. Contiguous memory yoktur. Yani bellekte yan yana değillerdir.
#Yani, the subscript, or index operation, makes it easy for the programmer to store and retrieve data. Yani, alt betim veya dizin işlemi, programcının veri depolamayı ve geri almayı kolaylaştırır.

#Static Memory and Dynamic Memory:
#Arrays in older langugaes such as FORTRAN, COBOL, and C, are static. Yani, eski dillerdeki diziler FORTRAN, COBOL ve C gibi statiktir.
#The length or capacirtof the array is fixed at the time of declaration. Yani, dizinin uzunluğu veya kapasitesi bildirildiği anda sabittir.

#Modern languages such as Python, Java, and C++ support dynamic arrays. Yani, Python, Java ve C++ gibi modern diller dinamik dizileri destekler.
########################################################################################################################################################
#MUHTEMEL SINAV SORUSU: Physical size and logical size: Yani, fiziksel boyut ve mantıksal boyut.
#Physical size is the actual size of the array in memory. Yani, fiziksel boyut, bellekteki dizinin gerçek boyutudur.
#Logical size is the number of elements in the array. Yani, mantıksal boyut, dizideki eleman sayısıdır.















