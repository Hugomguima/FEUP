#include<iostream>
#include<string>
#include"Class.h"
#include<sstream>
#include<vector>
#include<ctime>

using namespace std;


Date::Date()
{
	struct tm newtime;
	time_t now = time(NULL);
	localtime_s(&newtime, &now);
	month = 1 + newtime.tm_mon;
	year = 1900 + newtime.tm_year;
	day = newtime.tm_mday;

}

Date::Date(unsigned int year, unsigned int month, unsigned int day)
{
	this->year = year;
	this->month = month;
	this->day = day;
}

Date::Date(string yearMonthDay)
{
	stringstream date_ss(yearMonthDay);
	vector<string> v_temp;
	string temp;
	
	while (getline(date_ss, temp, '/'))
		v_temp.push_back(temp);

	year = stoi(v_temp[0]);
	month = stoi(v_temp[1]);
	day = stoi(v_temp[2]);
}

void Date::setYear(unsigned int year)
{
	this->year = year;
}

void Date::setMonth(unsigned int month)
{
	this->month = month;
}

void Date::setDay(unsigned int day)
{
	this->day = day;
}

void Date::setDate(unsigned int year, unsigned int month, unsigned int day)
{
	this->year = year;
	this->month = month;
	this->day = day;
}

unsigned int Date::getYear() const
{
	return year;
}

unsigned int Date::getMonth() const
{
	return month;
}

unsigned int Date::getDay() const
{
	return day;
}

string Date::getDate() const
{
	return to_string(year) + "/" + to_string(month) + "/" + to_string(day);
}

void Date::show() const
{
	cout << getDate();
}

bool Date::isValid()
{
	vector<int> v_month_days = {31,28,31,30,31,30,31,31,30,31,30,31 };
	vector<int> v_leap = { 31,29,31,30,31,30,31,31,30,31,30,31 };

	if (month > 12)
		return false;

	if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0)
	{
		v_month_days.resize(0);
		for (size_t i = 0; i < v_leap.size(); i++)
			v_month_days.push_back(v_leap[i]);
	}
	
	if (day <= v_month_days[month - 1])
		return true;

	return false;
}

bool Date::isEqualTo(const Date &date)
{
	if (date.getYear() == year && date.getMonth() == month && date.getDay() == day)
		return true;
	return false;
}

bool Date::isNotEqualTo(const Date &date)
{
	if (date.getYear() == year && date.getMonth() == month && date.getDay() == day)
		return false;
	return true;
}

bool Date::isAfter(const Date &date)
{
	if (year > date.year) return true;
	if (year == date.year && month > date.month) return true;
	if (year == date.year && month == date.month && day > date.day) return true;
	return false;
}

bool Date::isBefore(const Date &date)
{
	if (year < date.year) return true;
	if (year == date.year && month < date.month) return true;
	if (year == date.year && month == date.month && day < date.day) return true;
	return false;
}

bool operator<(const Date & left, const Date & right)
{
	if (left.year < right.year) return true;
	if (left.year == right.year && left.month < right.month) return true;
	if (left.year == right.year && left.month == right.month && left.day < right.day) return true;
	return false;
}
