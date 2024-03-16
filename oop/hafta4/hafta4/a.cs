using System.Runtime.CompilerServices;

namespace hafta4
{
    internal class a
    {
        public static void a_static()
        {
            b.numberb = 100; // Static method içerisinde static olmayan bir değişkeni kullanmak istediğimizde, o değişkenin bulunduğu sınıfın bir nesnesini oluşturup, o nesne üzerinden o değişkene ulaşabiliriz.
            
            Console.WriteLine("a_static");
            //Static method her yerden çağrılabilir.
            b.b_static();//B_static methodu adından da anlaşılabileceği gibi static bir methodtur. Her yerden çağrılabilir. Doğrudan sinif.method() seklinde çağrılabilir.
            a a_sinifi = new a();
            a_sinifi.a_nonstatic();//A_nonstatic methodu ise static olmadığı için doğrudan sinif.method() şeklinde çağrılamaz. Önce sinifin bir nesnesi oluşturulmalıdır. Oluşturulan nesne üzerinden çağrılabilir. 

            b bsinifi = new b();
            bsinifi.b_nonstatic();//B_nonstatic methodu ise static olmadığı için doğrudan sinif.method() şeklinde çağrılamaz. Önce sinifin bir nesnesi oluşturulmalıdır. Oluşturulan nesne üzerinden çağrılabilir.
            
        }
        public void a_nonstatic()
        {
            // Bsinifi.bstatic Static methodu nesne üzerinden çağıramayız. Çünkü static methodlar sadece bir kere oluşturulur ve her nesne oluşturulduğunda tekrar oluşturulmaz.
            b.b_static(); //Static method her yerden çağrılabilir.
            Console.WriteLine("a_nonstatic");
            b bsinifi2 = new b();
            bsinifi2.b_nonstatic();//B_nonstatic methodu ise static olmadığı için doğrudan sinif.method() şeklinde çağrılamaz. Önce sinifin bir nesnesi oluşturulmalıdır. Oluşturulan nesne üzerinden çağrılabilir.
            //static method daha az memory kullanır. Çünkü static methodlar sadece bir kere oluşturulur ve her nesne oluşturulduğunda tekrar oluşturulmaz.
            this.a_nonstatic();//A_nonstatic methodu ise static olmadığı için doğrudan sinif.method() şeklinde çağrılamaz. This anahtar kelimesi ile çağrılabilir. Çünkü this anahtar kelimesi ile o anki nesneyi temsil eder.
        }
        public void a2_nonstatic()
        {
            Console.WriteLine("a2_nonstatic");
            a_nonstatic();
            this.a_nonstatic(); 

        }
    }
}
