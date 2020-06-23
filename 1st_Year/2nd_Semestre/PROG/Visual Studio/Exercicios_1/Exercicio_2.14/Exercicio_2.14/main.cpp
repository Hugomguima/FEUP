#include<iostream>
#include<iomanip>

using namespace std;

int main()
{
	double num, n, rq, rqn, dif, x;

	cout << "Introduza o numero : ";
	cin >> num;

	rq = 1;
	rqn = (rq + num / rq) / 2;
	dif = num - rqn * rqn;

	cout << setprecision(4) << rq << "\t" << rqn << "\t" << rqn * rqn << "\t" << dif << endl;

	while (dif <= -0.0000001)
	{
		rq = rqn;
		rqn = (rqn + num / rqn) / 2;
		dif = num - rqn * rqn;

		cout << setprecision(5) << rq << "\t" << rqn << "\t" << rqn * rqn << "\t" << dif << endl;

	}
	cout << "\nA raiz quadrada de " << num << " e " << rqn;



	_getwch();
	return 0;
}