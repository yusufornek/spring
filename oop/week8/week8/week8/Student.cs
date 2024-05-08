using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace week8
{
    public class Student
    {
        public int studentId;
        public string studentDepartment;
        public string studentName {  get; set; } //Her bir değişken için 2'şer tane get ve set methodu tanımlamak yerine bunu kullanabiliriz.
        public string educationType { get; set; }
        public Student(string educationType) //Constructor methodu örneği
        {
            this.educationType = educationType;
        }

        public Student(int studentId)
        {
            this.studentId = studentId;
        }

        public string studentPhone
        {
            get {  return studentPhone; }
            set
            {
                if(this.ToString().Length ==11)
                    this.studentPhone = value;
            }
        }
        public void setStudentID(int studentId)
        {
            if(studentId > 0)
            {
                this.studentId = studentId;
            }
        }
        public void setStudentDepartment(string studentDepartment)
        {
            if(studentDepartment != null)
            {
                this.studentDepartment = studentDepartment;
            }
        }
        public int getStudentId(int studentId) 
        {  
            return this.studentId; 
        }
    }
}
