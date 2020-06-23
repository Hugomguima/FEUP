#include<iostream>
#include<cstring>

using namespace std;

bool isHydroxide(char compound[])
{
	int length = strlen(compound);

	if (compound[length - 1] == 'H' && compound[length-2] == 'O')
		return true;
	else
		return false;
}

int main()
{
	char word[] = "KOH";
	cout << isHydroxide(word) << endl;


	_getwch();
	return 0;
}