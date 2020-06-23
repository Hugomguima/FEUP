#include<iostream>
#include<cmath>

using namespace std;

int main()
{
	int num;
	char alinea;


	cout << "Escola a alinea que deseja : ";
	cin >> alinea;


	switch (alinea)
	{
	case 'a':
		cout << "Introduza o numero : ";
		cin >> num;

		if (num % 10 == num / 100)
			cout << num << " e uma capicua!!";
		else
			cout << num << " nao e uma capicua!!";
		break;

	case 'b':
		int a, n;
		int checker = 0;
		int last, first;

		cout << "Introduza o numero : ";
		cin >> n;

		a = n;

		last = n % 10;
		first = n / pow(10,(int)log10(n));


		while(first == last && (int)log10(a) > 0 )
		{
			last = a % 10;
			first = a / pow(10,(int)log10(a));

			if (first == last)
			{	
				checker = 1;
				a = a / 10;
				a = a - last * pow(10, (int)log10(a));

			}
			else
			{
				checker = 0;
				break;
			}
		}
		
		if (checker == 1)
			cout << n << " e uma capicua!!";
		else
			cout << n << " nao e uma capicua!!";

		break;
	}
	




	_getwch();
	return 0;
}
