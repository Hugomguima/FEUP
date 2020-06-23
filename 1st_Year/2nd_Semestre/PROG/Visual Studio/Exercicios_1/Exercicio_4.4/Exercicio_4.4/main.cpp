#include<iostream>
#include<string>

using namespace std;

string normalizeName(string name)
{
	int length = name.length();

	cout << name << endl << length << endl;

	while (name[length-1] == ' ' || name[0] == ' ')
	{
		if (name[length-1] == ' ') name.erase(length-1,1);
		if (name[0] == ' ') name.erase(0,1);
		length = name.length();
	}

	cout << length << endl << name << endl;

	for (int i = 0; i < length; i++)
		name[i] = (toupper(name[i]));

	while (name.find("  ") != -1)
	{
		int place = name.find("  ");
		name.erase(place, 1);
	}
	while (name.find(" DE ") != -1)
	{
		int place = name.find(" DE ");
		name.erase(place, 3);
	}
	while (name.find(" DO ") != -1)
	{
		int place = name.find(" DO ");
		name.erase(place, 3);
	}
	while (name.find(" DA ") != -1)
	{
		int place = name.find(" DA ");
		name.erase(place, 3);
	}
	while (name.find(" DOS ") != -1)
	{
		int place = name.find(" DOS ");
		name.erase(place, 4);
	}
	while (name.find(" DAS ") != -1)
	{
		int place = name.find(" DAS ");
		name.erase(place, 4);
	}
	while (name.find(" E ") != -1)
	{
		int place = name.find(" E ");
		name.erase(place, 2);
	}
	cout << length << endl << name << endl;



	return 0;
}




int main()
{
	normalizeName("  hugo miguel da do e da dos das silva   ");


	_getwch();
	return 0;
}