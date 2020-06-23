#include<iostream>
#include<string>

#include"Date.h"
#include"person.h"


using namespace std;

int main()
{
	Date d1(2000, 7, 17);
	Person p1("john","male","2000/7/17");

	cout << d1 << endl;
	cout << p1;

	_getwch();
	return 0;
}