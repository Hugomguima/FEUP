#include<iostream>

using namespace std;

void decompose(string compound)
{
	int length = compound.length();

	for (int i = 0; i < length; i++)
		if (isdigit(compound[i])) continue;
		else cout << compound[i];

		

}

int main()
{
	decompose("C6H12O6");

	_getwch();
	return 0;
}