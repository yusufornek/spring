using System.ComponentModel.DataAnnotations;
using System.Security.Cryptography;

namespace variableResulation
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Type a number : ");
            int sayi = Convert.ToInt32(Console.ReadLine());
            kareAl(sayi);
        }
        public static void kareAl(int sayi)
        {
            int sonuc;
            sonuc = sayi * sayi;
            goruntule(sonuc);
        }
        public static void goruntule(int number)
        {

            Console.WriteLine(number);
        }
        
        
        
    }
}
