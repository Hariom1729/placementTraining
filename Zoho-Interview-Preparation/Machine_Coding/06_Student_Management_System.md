# Machine Coding: Student Management System

## 1. Requirements

Design a Student Management System:
1. **Add Students:** Register students with details.
2. **Add Courses:** Create courses with credit values.
3. **Enrollments:** Enroll students into courses.
4. **Grading:** Assign grades to a student for a course.
5. **GPA Calculation:** Calculate the overall GPA for a student.

## 2. Entities
- `Student`: ID, Name, Enrollments.
- `Course`: ID, Name, Credits.
- `Enrollment`: Course, Grade.

## 3. C++ Implementation

```cpp
#include <iostream>
#include <vector>
#include <string>
#include <unordered_map>

using namespace std;

class Course {
public:
    string id;
    string name;
    int credits;
    Course() {}
    Course(string i, string n, int c) : id(i), name(n), credits(c) {}
};

class Enrollment {
public:
    string courseId;
    double grade; // 0.0 to 4.0
    bool isGraded;

    Enrollment(string c) : courseId(c), grade(0.0), isGraded(false) {}
};

class Student {
public:
    string id;
    string name;
    unordered_map<string, Enrollment> enrollments; // courseId -> Enrollment

    Student() {}
    Student(string i, string n) : id(i), name(n) {}

    void enroll(string courseId) {
        if(enrollments.find(courseId) == enrollments.end()) {
            enrollments[courseId] = Enrollment(courseId);
        }
    }

    void assignGrade(string courseId, double grade) {
        if(enrollments.find(courseId) != enrollments.end()) {
            enrollments[courseId].grade = grade;
            enrollments[courseId].isGraded = true;
        }
    }
};

class StudentManagementSystem {
private:
    unordered_map<string, Student> students;
    unordered_map<string, Course> courses;

public:
    void addStudent(string id, string name) {
        students[id] = Student(id, name);
    }

    void addCourse(string id, string name, int credits) {
        courses[id] = Course(id, name, credits);
    }

    void enrollStudent(string sId, string cId) {
        if(students.find(sId) != students.end() && courses.find(cId) != courses.end()) {
            students[sId].enroll(cId);
            cout << "Enrolled " << students[sId].name << " into " << courses[cId].name << "\n";
        }
    }

    void assignGrade(string sId, string cId, double grade) {
        if(students.find(sId) != students.end()) {
            students[sId].assignGrade(cId, grade);
        }
    }

    void calculateGPA(string sId) {
        if(students.find(sId) == students.end()) return;
        
        Student& s = students[sId];
        double totalPoints = 0;
        int totalCredits = 0;

        for(auto& pair : s.enrollments) {
            Enrollment& e = pair.second;
            if(e.isGraded) {
                int credits = courses[e.courseId].credits;
                totalCredits += credits;
                totalPoints += (e.grade * credits);
            }
        }

        if(totalCredits == 0) cout << s.name << " has no graded courses yet.\n";
        else cout << s.name << " GPA: " << (totalPoints / totalCredits) << "\n";
    }
};

int main() {
    StudentManagementSystem sms;
    sms.addCourse("CS101", "Intro to CS", 3);
    sms.addCourse("MTH101", "Calculus I", 4);

    sms.addStudent("S1", "John Doe");

    sms.enrollStudent("S1", "CS101");
    sms.enrollStudent("S1", "MTH101");

    sms.assignGrade("S1", "CS101", 3.5); // A-
    sms.assignGrade("S1", "MTH101", 4.0); // A

    sms.calculateGPA("S1"); // (3.5*3 + 4.0*4) / 7 = 3.78

    return 0;
}
```

## 4. Interview Discussion
- **Many-to-Many Relationships:** A student has many courses, a course has many students. Handling this cleanly is a standard SQL / OOP design question.
