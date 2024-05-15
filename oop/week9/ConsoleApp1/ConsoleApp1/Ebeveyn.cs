using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    public class Ebeveyn //Sealed olan class bir nevi mühürlenit, korumaya alınır. O sınıfı türetemezsin.
    {
        public double x;
        public double y;

   
        public Ebeveyn(double x, double y) //Normalde bu methodun adı hipotenüstü ama constructor yapısını göstermek için Ebeveyn adını verdik.
        {
            /*  Console.WriteLine("Bana bir kenar bilgisini ver");
              x = Convert.ToDouble(Console.ReadLine());
              Console.WriteLine("Bana diğer kenarın bilgisini ver");
              y = Convert.ToDouble(Console.ReadLine());*/
            this.x = x;
            this.y = y;

            //Kurucu methodlar geriye değer döndürmez, void dışında!
        }
        public virtual double kare()
        {
            /*double karelerToplami;
            double hipotenus;
            karelerToplami = (this.x * this.x) + (this.y * this.y);
            hipotenus = Math.Sqrt(karelerToplami);
            return hipotenus;*/
            return this.x * this.x;
        }
      
    }

}
