namespace week8
{
    internal class Program
    {
        static void Main(string[] args)
        {
            Trigonometri trigo = new Trigonometri(); //Zaten kalıtımı belirtmiştik, o yüzden bir daha yazmadık Algebra algebra = new Algebra(); diye
            trigo.ciktila();

            Student ogrenci = new Student("Lisans"); //Parantez içi constructor methodu için
            ogrenci.studentId = 1;

            Console.WriteLine(ogrenci.educationType);
            
            Console.WriteLine("Student ID: {0} ", ogrenci.studentId);
            // Console.WriteLine($"Student ID: {ogrenci.studentId}"); //Başka bir yol

            ogrenci.setStudentID(112);
            Console.WriteLine("Student ID : {0}", ogrenci.studentId);

            ogrenci.studentName = "Yusuf"; // it calls set method of studentName
            Console.WriteLine(ogrenci.studentName);  // it calls get method of studentName

            ogrenci.studentPhone = "123456";
            Console.WriteLine(ogrenci.studentPhone);

            
            

        }
    }
}
