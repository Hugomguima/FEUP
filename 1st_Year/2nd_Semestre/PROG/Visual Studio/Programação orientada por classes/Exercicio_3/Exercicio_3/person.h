#pragma once

#include<string>
#include"Date.h"

using namespace std;

class Person
{
public:
	//Constructors
	Person(string name, string gender, Date date);
	Person(string name, string gender, string date);

	//Set Methods
	void setName(string name);
	void setGender(string gender);
	void setDate(Date date);

	//Get Methods
	string getName();
	string getGender();
	Date getDate();

	//Overload Methods
	friend ostream& operator<<(ostream& out, const Person & person);


private:
	string name;
	string gender;
	Date date;

};
