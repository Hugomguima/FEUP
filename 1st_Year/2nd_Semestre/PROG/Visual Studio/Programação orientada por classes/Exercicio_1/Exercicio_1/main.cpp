#include<iostream>
#include<string>
#include<vector>
#include<cmath>
#include"Class.h"

using namespace std;


int main()
{
	Date d1(2020,2,29), d2(2020,2,15) ,d3;
	bool k = d2 < d1;
	cout << "d1 < d2 : " << k << endl;
	cout << "IsValid == " << d1.isValid() << endl;
	cout << "GetYear == " << d1.getYear() << endl;
	cout << "GetMonth == " << d1.getMonth() << endl;
	cout << "Getday == " << d1.getDay() << endl;
	cout << "GetDate == " << d1.getDate() << endl << endl;

	cout << "isEqualTo == " << d1.isEqualTo(d2) << endl;
	cout << "isNotEqualTo == " << d1.isNotEqualTo(d2) << endl;
	cout << "isAfter == " << d1.isAfter(d2) << endl;
	cout << "isBefore == " << d1.isBefore(d2) << endl << endl;

	d3.show();






	_getwch();
	return 0;
}

