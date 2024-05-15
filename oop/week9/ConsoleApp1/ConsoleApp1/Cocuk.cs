using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class Cocuk : Ebeveyn 
    {
        public Cocuk(double x, double y) : base(x, y)
        {

        }
        public double kare()
        {
            double kare = base.kare(); //Ebeveyn class'ın hipotenüsünü base ile çağırır ve onu da kullanarak işlem yapar!
            return this.x * kare; //Buradaki kare, ebeveyn sınıfından gelen kare.
        }
        public int sayi {  get; set; }
        public int sayi2 {
            get
            {
                return this.sayi2;
            }
            set
            {
                value = value++;
            }
        
        }
        
    }
}
