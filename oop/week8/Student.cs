using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace StudentClass
{
     public class Student
    {
        public int studentId;
        public string studentDepartment;
        public string studentName { get; set; }

        public string educationType { get; set; }
        public string studentPhone
        {
            get { return studentPhone; }

            set
            {
                if (value.ToString().Length == 11)
                    this.studentPhone = value;
                else
                    this.studentPhone = "0";
            }
        }

        public Student(string educationType)
        {
            this.educationType = educationType;
        }

        public Student(int studentId)
        {
            this.studentId = studentId;
        }

        public void setStudentID(int studentId)
        {
            if (studentId > 0)
                this.studentId = studentId;
        }

        public void setStudentDepartment(string studentDepartment)
        {
            this.studentDepartment = studentDepartment;
        }

        public int getStudentId(int studentId)
        {

            return this.studentId;
        }
    }
}
