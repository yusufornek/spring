namespace StudentClass
{
    internal class Program
    {
        static void Main(string[] args)
        {

            //int sayi = Convert.ToInt32(Console.ReadLine());
            /*
            string a = "5";
            string b = "3";
            Console.WriteLine(a + b);
            */

            /*
            int x = 10;
            Student ogrenci = new Student("Lisans");
            
            Console.WriteLine(ogrenci.educationType);
            //ogrenci.studentId = -1;

            Console.WriteLine("Student ID: {0}" , ogrenci.studentId);
            // Console.WriteLine($"Student ID: {ogrenci.studentId}");

            // ogrenci.educationType = "Lisans";

            ogrenci.setStudentID(-1);
            Console.WriteLine("Student ID: {0}", ogrenci.studentId);

            ogrenci.setStudentID(18);
            Console.WriteLine("Student ID: {0}", ogrenci.studentId);

            ogrenci.studentName = "Zeki"; // it calls set method of studentName
            Console.WriteLine(ogrenci.studentName); // it calls get method of studentName

            /*ogrenci.studentPhone = "123456";
            Console.WriteLine(ogrenci.studentPhone);*/

            /*
            Student ogrenci2 = new Student(123456);
            Console.WriteLine("Student ID: {0}", ogrenci2.studentId);
            */


            //Algebra algebra = new Algebra();
            Trigonometri trigon = new Trigonometri();
           // trigon.ciktila();
        }
    }
}