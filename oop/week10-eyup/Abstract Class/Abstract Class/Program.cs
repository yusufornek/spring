using System.Security.Cryptography.X509Certificates;

namespace Abstract_Class
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //Ogrenci soyut = new Ogrenci();
            //abstract sınıfların yeni bir örneğini oluşturamayız.
                
           Lisans lisans1 = new Lisans();
            lisans1.study("Lisans");


            Master master = new Master();
            master.study("Master");

            ogrenci2nincocugu ogrenci2Nincocugu2 = new ogrenci2nincocugu();
            ogrenci2Nincocugu2.study();
            
        }
    }
}
