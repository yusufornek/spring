namespace week6
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine(Math.Round(arithmetic.kare(5.6),2)); //İki basamağa yuvarladık Math.Round fonksiyonu ile birlikte.
            Console.WriteLine(Math.Floor(arithmetic.kare(5.6))); //Aşağı yuvarlama
            Console.WriteLine(Math.Ceiling(arithmetic.kare(5.6))); //Yukarı yuvarlama
            Console.WriteLine(arithmetic.kare(5));
            Console.WriteLine(arithmetic.varsayilandegermethodu(8)); //Parametre girersem gönderdiğim parametre çalışır.
            Console.WriteLine(arithmetic.varsayilandegermethodu()); //Parametre girmezsem varsayılan parametre değeri çalışır.
        }   
         /*IEE1254 FORMATINA BAK!*/
    }
}
