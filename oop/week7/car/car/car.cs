using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace car
{
    internal class car
    {
        string marka;
        string model;
        short yil;
        string yakit_tipi;
        string araba_tipi;
        string vites_türü;
        short motor_hacmi;
        bool koltuk_isitma;
        public void run()
        {
            Console.WriteLine("Araba çalışıyor.");
        }
        public void @break()
        {
            Console.WriteLine("Araba fren yapıyor.");
        }
        public void stop()
        {
            Console.WriteLine("Araba duruyor.");
        }
    }
}
