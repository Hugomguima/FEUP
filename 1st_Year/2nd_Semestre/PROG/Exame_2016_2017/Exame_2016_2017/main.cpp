#include <iostream>
#include <string>
#include <vector>
#include <fstream>
#include <sstream>
#include <algorithm>

class Date
{
public:
	Date(int year, int month, int day);
	Date();
	~Date();

private:

};

Date::Date(int year, int month, int day)
{
}

Date::~Date()
{
	int d, m, y;
}

using namespace std;

void simplify(const string &name, string &sName)
{
	stringstream ss(name);
	vector<string> v;
	string temp;

	while (getline(ss, temp, ' '))
	{
		if (temp != "") v.push_back(temp);
	}
	if (v.size() == 1) sName = v[0];
	else sName = v[0] + " " + v[v.size()-1];
}

void aDate(int day, int month, int year)
{
	d = day;
	m = month;
	y = year;
}

/**/
istream & operator>>(istream & f, Date & date)
{
	int year, month, day;
	string temp, date_string;
	vector<int> v;
	
	getline(f, date_string);
	stringstream ss(date_string);
	while (getline(ss, temp, '-'))
	{
		if (stoi(temp) < 0)
		{
			runtime_error message("Invalid Date");
			throw message;
			exit(1);
		}
		v.push_back(stoi(temp));
	}
	if (v.size() != 3)
	{
		runtime_error message("Invalid Date");
		throw message;
		exit(1);
	}
	year = v[0];
	month = v[1];
	day = v[2];
	date = Date(year, month, day);
}

int main()
{

	//Exercício 1.a)
	/*
	ifstream fin("people1.txt");
	if (fin.fail()) return 1;

	ofstream fout("people2.txt");
	string temp, changed;


	while (getline(fin, temp))
	{
		simplify(temp, changed);
		fout << changed << endl;
	}
	*/
	//Exercício 1.c)
	ifstream fin("people1.txt");
	if (fin.fail()) return 1;

	ofstream fout("people2.txt");
	string temp, changed;
	vector<string> v;


	while (getline(fin, temp))
	{
		simplify(temp, changed);
		v.push_back(changed);
	}
	sort(v.begin(), v.end());
	for (size_t i = 0; i < v.size(); i++) fout << v[i];
	
	
	
	
	



	_getwch();
	return 0;
}