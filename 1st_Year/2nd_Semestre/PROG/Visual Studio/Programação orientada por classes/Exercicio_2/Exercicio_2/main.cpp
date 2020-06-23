#include<iostream>
#include"class.h"


using namespace std;

int main()
{
	Student s1;

	cout << "GetCode == " << s1.GetCode() << endl;
	cout << "GetName == " << s1.GetName() << endl;
	cout << "GetFinalGrade == " << s1.GetFinalGrade() << endl;
	cout << "IsApproved == " << s1.isApproved() << endl;



	_getwch();
	return 0;
}