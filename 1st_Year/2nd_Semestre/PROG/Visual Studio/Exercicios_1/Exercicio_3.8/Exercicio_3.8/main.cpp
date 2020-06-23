#include<iostream>

using namespace std;

int mdc(int m, int n)
{
	if (m % n == 0)
		return n;

	return mdc(n, m % n);
}



int main()
{
	int n1, n2;

	cout << "Introduza os 2 numeros : " << endl;
	cin >> n1 >> n2;

	cout << endl << mdc(n1, n2);

	_getwch();
	return 0;

}