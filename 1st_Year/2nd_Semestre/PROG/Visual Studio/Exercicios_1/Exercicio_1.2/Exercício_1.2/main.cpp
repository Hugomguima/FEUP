#include <iostream>
#include <iomanip> 
using namespace std;

int main()
{
	float a;
	float b;
	float c;
	float media;
	float a_media;
	float b_media;
	float c_media;

	cout << "A ? ";
	cin >> a;
	cout << "B ? ";
	cin >> b;
	cout << "C ? ";
	cin >> c;
	
	media = (a + b + c) / 3.0;
	a_media = a - media;
	b_media = b - media;
	c_media = c - media;

	cout << "\nmedia = " << media << endl;
	cout << "A-media = " << a_media << endl;
	cout << "B-media = " << b_media << endl;
	cout << "C-media = " << c_media << endl;

	_getwch();
	return 0;
}