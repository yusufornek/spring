using System;
using System.Collections.Generic;
using System.Linq;
using System.Security.Cryptography.X509Certificates;
using System.Text;
using System.Threading.Tasks;

namespace Abstract_Class
{
   public  abstract class Ogrenci
    {

        public int sayi;
        public void example(int _sayi)
        {
            Console.WriteLine("Abstract Examples");
            sayi = _sayi;

        }

        
        public virtual void study(string _ogrenciTipi)
        {
            
            Console.WriteLine($" {_ogrenciTipi} Ogrencisi olarak calisir.");
          
        }
        public Ogrenci()
        {
            

        }
        public void sinav()
        {
            Console.WriteLine("Öğrenci sınava girer.");
        }





    }
}
