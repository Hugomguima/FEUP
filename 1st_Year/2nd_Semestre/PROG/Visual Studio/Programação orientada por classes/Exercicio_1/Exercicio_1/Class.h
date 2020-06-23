#ifndef DATE_H
#define DATE_H
#include<string>

using namespace std;

class Date
{
	friend bool operator <(const Date&left, const Date&right);
public:
	Date();
	Date(unsigned int year, unsigned int month, unsigned int day);
	Date(string yearMonthDay);
	void setYear(unsigned int year);
	void setMonth(unsigned int month);
	void setDay(unsigned int day);
	void setDate(unsigned int year, unsigned int month, unsigned int day);
	unsigned int getYear() const;
	unsigned int getMonth() const;
	unsigned int getDay() const;
	string getDate() const;
	void show() const;
	bool isValid();
	bool isEqualTo(const Date &date);
	bool isNotEqualTo(const Date &date);
	bool isAfter(const Date &date);
	bool isBefore(const Date &date);


private:
	unsigned int year;
	unsigned int month;
	unsigned int day;

};

#endif
