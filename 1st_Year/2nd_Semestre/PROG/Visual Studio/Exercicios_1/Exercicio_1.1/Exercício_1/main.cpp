#include <iostream>
using namespace std;


int main()
{
	char c;
	cout << "Enter a character : ";
	cin >> c;
	cout << "ASCII value of " << c << " is : " << hex << int(c);
	_getwch();
	return 0;
	
}