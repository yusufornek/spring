namespace ConsoleApp1
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Bana bir kenar bilgisini ver");
            double x = Convert.ToDouble(Console.ReadLine());
            Console.WriteLine("Bana diğer kenarın bilgisini ver");
            double y = Convert.ToDouble(Console.ReadLine());
            /*Ebeveyn ebeveyn = new Ebeveyn(x,y);
            Console.WriteLine(ebeveyn.hipotenus());*/

            Cocuk cocuk = new Cocuk(x, y);
            Console.WriteLine(cocuk.hipotenus());
            /*try
            {
                double sonuc = x / y;
                Console.WriteLine(sonuc);
            } catch (DivideByZeroException ex)
            {
                Console.WriteLine("Sayı 0'a bölünemez!");
            }
            finally
            {
                Console.WriteLine("Sonlandırıldı");
            }*/


            //Bir sınıfta method oluşturarak kod tekrarının önüne geçmiş olduk.

        }
        /*public static double hipotenus(double x, double y)
        {
            *//*  Console.WriteLine("Bana bir kenar bilgisini ver");
              x = Convert.ToDouble(Console.ReadLine());
              Console.WriteLine("Bana diğer kenarın bilgisini ver");
              y = Convert.ToDouble(Console.ReadLine());*//*

            double karelerToplami;
            double hipotenus;
            karelerToplami = (x * x) + (y * y);
            hipotenus = Math.Sqrt(karelerToplami);
            return hipotenus;
            
        }*/



        //Data Encapsulation nedir?
        //Method Overloading nedir, derdimiz ne ki bunu kullanıyoruz?
        //Inheritance nedir, neler yapıyoruz? Kalıtım ne işe yarar? 
        //Neden sınıf alıyoruz, yani biz bu sınıfları neden oluşturuyoruz?
        //Abstract class nedir? --Ödev--
        //Interface nedir? --Ödev--
        //Virtual 
        //base keyword
        //sealed 
        //get, set methodları bir kaç istisna içeriyordu, bunlar neler?
        // get, set, value, seti özelleştirdiğin zaman get'i de özelleştiriyorsun
        //Method overriding
        //Constructor Method
        //Instance oluşturma
        //Static, non-static, birbirlerinden çağırma
        //Inheritance
        
    }
}
//Yusuf Örnek
//Yusuf Örnek
//Yusuf Örnek
//Yusuf Örnek
//Yusuf Örnek
//Yusuf Örnek
//Yusuf Örnek

