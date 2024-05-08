using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace week8
{
    internal class Algebra
    {
        

        public int sayi {            //Get ve set methodu olan bir değişken ve negatif değer alursa 5 değerini döndürür.
           
            get { return sayi; }
            set 
            { 
            if (value < 0)
                this.sayi = 5;
            
            } 
        }
        public Algebra()
        {
            Console.WriteLine("Zeki Hocam");
        }
        
    }

}
