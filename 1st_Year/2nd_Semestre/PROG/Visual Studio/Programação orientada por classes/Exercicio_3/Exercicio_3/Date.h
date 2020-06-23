#pragma once

#include<string>

using namespace std;

class Date
{
public:
	Date();
	Date(unsigned int year, unsigned int month, unsigned int day);
	Date(string yearMonthDay);

	//Set Methods
	void setYear(unsigned int year);
	void setMonth(unsigned int month);
	void setDay(unsigned int day);
	void setDate(unsigned int year, unsigned int month, unsigned int day);

	//Get Methods
	unsigned int getYear() const;
	unsigned int getMonth() const;
	unsigned int getDay() const;
	string getDate() const;

	//Show method
	void show() const;

	//Comparison Methods
	bool isValid();
	bool isEqualTo(const Date &date);
	bool isNotEqualTo(const Date &date);
	bool isAfter(const Date &date);
	bool isBefore(const Date &date);
	
	//ostream
	friend ostream& operator<<(ostream& out, const Date & date);

private:
	unsigned int year;
	unsigned int month;
	unsigned int day;

};
