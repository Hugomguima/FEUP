#ifndef STUDENT_H
#define STUDENT_H
#include<string>

using namespace std;

class Student
{
public:
	Student();
	Student(const string &code, const string &name);
	void setGrades(double shortExam, double project, double exam);
	string GetCode() const;
	string GetName() const;
	int GetFinalGrade() const;

	bool isApproved();
	static int weightShortExam, weightProject, weightExam;

private:
	string code;
	string name;
	double shortExam, project, exam;
	int finalGrade;

};


#endif
