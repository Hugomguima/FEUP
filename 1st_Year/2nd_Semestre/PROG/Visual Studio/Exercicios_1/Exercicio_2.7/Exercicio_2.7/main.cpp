#include<iostream>
#define _USE_MATH_DEFINES
#include<math.h>
#include <iomanip>
#include<string>
using namespace std;

int main()
{
	int ang;
	char alinea;

	cout << "Escolha a alinea que deseja : ";
	cin >> alinea;

	switch (alinea)
	{
	case 'a':

		cout << setprecision(6) << fixed <<"\n   ang\t\t" << "   sen\t\t" << "   cos\t\t" << "   tan\t" << endl;
		

		for (double i = 0; i <= 90; i += 15)
		{
			double seno, cosseno, tangente;
			seno = sin(i * M_PI / 180);
			cosseno = cos(i * M_PI / 180);
			tangente = tan(i*M_PI / 180);
			

			cout << setprecision(6) << fixed << i << "\t" << seno << "\t" << cosseno << "\t" << tangente << endl;
		}

		break;
	case 'b':
		double intervalo;

		cout << "Introduza o intervalo de resultados : ";
		cin >> intervalo;

		cout << setprecision(6) << fixed << "\n   ang\t\t" << "   sen\t\t" << "   cos\t\t" << "   tan\t" << endl;


		for (double i = 0; i <= 90; i += intervalo)
		{
			double seno, cosseno, tangente;
			seno = sin(i * M_PI / 180);
			cosseno = cos(i * M_PI / 180);
			tangente = tan(i*M_PI / 180);


			cout << setprecision(6) << fixed << i << "\t" << seno << "\t" << cosseno << "\t" << tangente << endl;
		}
		break;
	}


	_getwch();
	return 0;

}