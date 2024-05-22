using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    abstract class Soyut
    {
        //public abstract string Name() { get; }

        public void study()
        {
            Console.WriteLine("Hay, evrivan! ");
            Console.WriteLine("Öğrenci çalışır! ");

        }
        
        public void sinav()
        {
            Console.WriteLine("Öğrenci sınava girer! ");
        }
        

        //Abstract class içinde abstract method normal şartlar altında oluşturalamaz ama get - set methodu kullanılarak oluşturulabilir.
        //Abstract classlarda kalıtım mümkün, zaten bunun için var ama örneğini oluşturamıyoruz. (new anahtar sözcüğü ile)
    }
}
//Yusuf Example