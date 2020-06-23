#include<iostream>

using namespace std;

int main()
{
	int num, counter;

	cout << "Introduza o numero : ";
	cin >> num;
	
	int n = num;

	for (int i = 2; i <= num; i++) 
	{
		counter = 0;

		for (int j = 1; i >= j; j++)
			if (i % j == 0)
				counter++;
		if (counter == 2)
		{
			while (n % i == 0)
			{
				cout << i << endl;
				n = n / i;
			}
		}
	}
			






	_getwch();
	return 0;
}