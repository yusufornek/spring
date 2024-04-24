using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace car
{
    internal abstract class TOGG
    {
        public string marka;
        public string model;
        public short yil;
        public string yakit_tipi;
        public string araba_tipi;
        public string vites_türü;
        public short motor_hacmi;
        public bool koltuk_isitma;
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
        public TOGG( string marka, short yil, string araba_tipi)
        {
            /*this .marka = marka;
            this .yil = yil;
            this .araba_tipi = araba_tipi;*/ // Sınıfın üyesi... Program.cs'teki değişkenler artık burada tanımlanan parametre oldu.

           /* marka = marka;
            yil = yil;
            araba_tipi = araba_tipi;*/
            Console.WriteLine($"Marka: {marka} Yıl: {yil} Model {araba_tipi}  ");
        }
        public void display()
        {
            /*Console.WriteLine($"Marka: {marka} Yıl: {yil} Model {araba_tipi}  ");*/
            Console.WriteLine($"Marka: {this.marka} Yıl: {this.yil} Model {this.araba_tipi}  ");
        }
        //This keywordu, Get-Set ve Trim fonksiyonu bu derste işlenmiştir. Trim fonksiyonu, get-set ve abstract sınıfı burada yoktur. Ayrıca çalış!
    }
}
