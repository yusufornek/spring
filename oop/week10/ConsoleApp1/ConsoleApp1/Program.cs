using System.Net.Http.Headers;

namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
           /* Console.WriteLine("Hello, World!");*/
            //Soyut soyut = new Soyut(); Abstract class'larda örnek oluşturulamaz, mesela new komutu kullanılamaz!
            Lisans lisans = new Lisans(); //Lisans sınıfı Soyut sınıfından kalıtım aldığı için study diye bir metodu olmamasına rağmen soyut sınıfındaki metodu çalıştırır.
            lisans.study();

            ogrenci2nincocugu ogrenci2cocuk = new ogrenci2nincocugu();
            ogrenci2cocuk.study();
        }
    }
}

//Yusuf Example