#include <iostream>
#include <string>
#include <vector>
#include <sstream>
#include <fstream>
#include <algorithm>
#include <new>
/*
#include "Board.h"
*/

using namespace std;


void toUpperStr( string &s)
{
	for (int i = 0; i < s.size(); i++)
	{
		s[i] = toupper(s[i]);
	}
}

string transformLine(string s)
{

	for (int i = 0; i < s.size(); i++)
	{
		if (!isalpha(s[i]) && s[i] != ' ')
		{
			s[i] = ' ';
		}
	}
	toUpperStr(s);
	return s;
}

void decomposeLine(string line, vector<string> words)
{
	line = transformLine(line);
	stringstream info(line);
	string temp;

	while (getline(info, temp, ' '))
	{
		if (temp != "") words.push_back(temp);
	}

}

void changeFile(string beginfile, string endfile)
{
	ifstream fin(beginfile);
	ofstream fout(endfile);
	string tempo;
	vector <string> line;

	while (getline(fin, tempo))
	{
		decomposeLine(tempo, line);
		sort(line.begin(), line.end());
		for (size_t i = 0; i < line.size(); i++)
		{
			fout << line[i] << endl;
		}
	}
}

float average(const int grades[], int numStudents)
{
	float result = 0;
	for (int i = 0; i < numStudents; i++)
	{
		result += grades[i];
	}
	return result /= numStudents;
}



int main()
{
	// Exercício 3.e 
	/*
	Board b(10, 20);
	unsigned int identifier;
	char symbol;
	Position position;
	char direction;
	size_t size;

	cout << "identifier :" << endl; cin >> identifier;
	cout << "symbol :" << endl; cin >> symbol;
	cout << "position [line] [col] :" << endl; cin >> position.lin, position.col;
	cout << "direction :" << endl; cin >> direction;
	cout << "size :" << endl; cin >> size;

	Ship sh(identifier, symbol, position, direction, size);

	if (b.putShip(sh) == false)
	{
		throw "Can't put ship!";
	}
	*/

	//Exercicio 3.a2
	/*
	int students_number;
	int *p = new int[students_number];

	readGrades(p, students_number);

	average(p, students_number);

	delete [] p;

	*/




	_getwch();
	return 0;
}