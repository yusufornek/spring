using System.Runtime.InteropServices;

namespace week5
{
    internal class Program
    {
        public int userId = 5; //Static olsaydı nesne oluşturmadan erişebilirdik.
        public static int elma = 7; //Static olunca nesne oluşturmadan erişebiliriz.
        private string password = "A1B2C3";
        protected long TCKimlik = 12345678912l;





        static void Main(string[] args)
        {
            Program program = new Program();
            Console.WriteLine(program.userId); //Static olsaydı nesne oluşturmadan erişebilirdik.
            Console.WriteLine(program.password);
            Console.WriteLine(program.TCKimlik);
            Console.WriteLine(elma); //Static olunca nesne oluşturmadan erişebiliriz.
            Console.WriteLine("Hello, World!");
            // Enkapsülasyon şu işe yarar: Bir nesnenin içindeki verilere dışarıdan erişimi kısıtlamak.
            // Bu sayede nesnenin iç yapısını koruyarak, dışarıdan erişimi kontrol edebiliriz.
            //Public: her yerden erişilebilir.
            //Private: sadece tanımlandığı sınıf içerisinden erişilebilir.
            //Protected: tanımlandığı sınıf ve bu sınıftan türetilen sınıflardan erişilebilir.
            //Internal: tanımlandığı proje içerisinden erişilebilir.
        }
    }
}
