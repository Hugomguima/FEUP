#include<iostream>
#include"person.h"
#include<string>

using namespace std;


Person::Person(string name, string gender, Date date)
{
	this->name = name;
	this->gender = gender;
	this->date = date;
}
Person::Person(string name, string gender, string yearMonthDay)
{
	this->name = name;
	this->gender = gender;
	this->date = Date(yearMonthDay);
}

void Person::setName(string name)
{
	this->name = name;
}

void Person::setGender(string gender)
{
	this->gender = gender;
}

void Person::setDate(Date date)
{
	this->date = date;
}

string Person::getName()
{
	return name;
}

string Person::getGender()
{
	return gender;
}

Date Person::getDate()
{
	return date;
}

ostream & operator<<(ostream & out, const Person & person)
{
	out << person.name << "'s " << "information:" << endl << endl;
	out << "name: " << person.name << endl << "gender: " << person.gender << endl << "date: " << person.date;
	return out;
}
