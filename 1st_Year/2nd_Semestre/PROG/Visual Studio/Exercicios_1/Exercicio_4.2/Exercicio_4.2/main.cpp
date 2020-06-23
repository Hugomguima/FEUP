#include<iostream>
#include<string>

using namespace std;

bool sequenceSearch(string s, int nc, char c)
{
	int length =  s.length();
	int counter = 0;

	for (int i = 0; i < length; i++)
	{
		if (s[i] == c)
			counter++;
		else counter = 0;

		if (counter = nc)
			break;

	}

	if (counter == nc) return true;
	else return false;


}

int main()
{
	string st = "abcddde";
	cout << sequenceSearch(st, 2, 'd');



	_getwch();
	return 0;
}