

namespace hafta4
{
    internal class b
    {
        public static int numberb = 10;
        public int numberb2 = 20;
        public static int numberBstatic = 10;
        public static void b_static()
        {
            double numberBstatic = 3.14;
            Console.WriteLine(numberBstatic); // Bu durumda static method içerisinde static olmayan bir değişkeni kullanmak istediğimizde, o değişkenin bulunduğu sınıfın bir nesnesini oluşturup, o nesne üzerinden o değişkene ulaşabiliriz.
            Console.WriteLine("b_static");
            Console.WriteLine(numberb);
            b yeni = new b();
            yeni.numberb2 = 30; // Bu da bir başka yöntem olabilir. Static method içerisinde static olmayan bir değişkeni kullanmak istediğimizde, o değişkenin bulunduğu sınıfın bir nesnesini oluşturup, o nesne üzerinden o değişkene ulaşabiliriz.
        }
        public void b_nonstatic()
        {
            b yeni = new b();
            Console.WriteLine("b_nonstatic");
            Console.WriteLine(numberb2);
            Console.WriteLine(numberBstatic);
            Console.WriteLine(b.numberBstatic);
            // Console.WriteLine(yeni.numberBstatic); // Hata aldık çünkü numberBstatic static bir değişken. Static değişkenler sınıfın bir nesnesi oluşturulmadan çağrılabilir.
            
        }
         
    }
}
