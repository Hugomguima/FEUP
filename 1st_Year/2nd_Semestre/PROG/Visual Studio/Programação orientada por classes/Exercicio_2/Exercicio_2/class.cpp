#include<iostream>
#include<string>;
#include"class.h"
#include<cmath>

using namespace std;


Student::Student()
{
}

Student::Student(const string &code,const string & name)
{
	this->code = code;
	this->name = name;
}

void Student::setGrades(double shortExam, double project, double exam)
{
	this->shortExam = shortExam;
	this->project= project;
	this->exam = exam;
	weightShortExam = 20;
	weightProject = 30;
	weightExam = 50;

	finalGrade = round((shortExam * weightShortExam + project * weightProject + exam * weightExam) / 100);
}

string Student::GetCode() const
{
	return code;
}

string Student::GetName() const
{
	return name;
}

int Student::GetFinalGrade() const
{
	return finalGrade;
}

bool Student::isApproved()
{
	if (finalGrade >= 10) return true;
	return false;
}
