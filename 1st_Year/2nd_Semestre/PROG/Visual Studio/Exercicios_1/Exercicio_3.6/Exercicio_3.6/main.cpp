#include<iostream>
#include<string>

using namespace std;

bool bissexto(int ano)
{
	if (ano % 4 == 0 && ano % 100 != 0)
		return true;
	else if (ano % 4 == 0 && ano % 400 == 0)
		return true;
	else
		return false;
}

int dias(int mes,int ano)
{
	switch (mes)
	{
		case(1):
			return 31;
			break;
		case(2):
		{
			if (bissexto(ano))
				return 29;
			else
				return 28;
			break;
		}
		case(3):
			return 31;
			break;
		case(4):
			return 30;
			break;
		case(5):
			return 31;
			break;
		case(6):
			return 30;
			break;
		case(7):
			return 31;
			break;
		case(8):
			return 31;
			break;
		case(9):
			return 30;
			break;
		case(10):
			return 31;
			break;
		case(11):
			return 30;
			break;
		case(12):
			return 31;
			break;
	}
}

int dia_semana(int ano, int m,int d)
{
	int c;
	int s = (ano / 100);
	int a = ano % 100;

	switch (m)
	{
	case(1):
		if (bissexto(ano))
			c = 6;
		else
			c = 0;
		break;

	case(2):
		if (bissexto(ano))
			c = 2;
		else
			c = 3;
		break;
	case(3):
		if (bissexto(ano))
			c = 3;
		else
			c = 3;
		break;
	case(4):
		if (bissexto(ano))
			c = 6;
		else
			c = 6;
		break;
	case(5):
		if (bissexto(ano))
			c = 1;
		else
			c = 1;
		break;
	case(6):
		if (bissexto(ano))
			c = 4;
		else
			c = 4;
		break;
	case(7):
		if (bissexto(ano))
			c = 6;
		else
			c = 6;
		break;
	case(8):
		if (bissexto(ano))
			c = 2;
		else
			c = 2;
		break;
	case(9):
		if (bissexto(ano))
			c = 5;
		else
			c = 5;
		break;
	case(10):
		if (bissexto(ano))
			c = 0;
		else
			c = 0;
		break;
	case(11):
		if (bissexto(ano))
			c = 3;
		else
			c = 3;
		break;
	case(12):
		if (bissexto(ano))
			c = 5;
		else
			c = 5;
		break;
	}

	return ((5 * a / 4) + c + d - 2 * (s % 4) + 6) % 7;
}

void calendario(int ano,int m)
{
	string mes;
	switch (m)
	{
	case(1):
		mes = "Janeiro";
		break;
	case(2):
		mes = "Fevereiro";
		break;
	case(3):
		mes = "Marco";
		break;
	case(4):
		mes = "Abril";
		break;
	case(5):
		mes = "Maio";
		break;
	case(6):
		mes = "Junho";
		break;
	case(7):
		mes = "Julho";
		break;
	case(8):
		mes = "Agosto";
		break;
	case(9):
		mes = "Setembro";
		break;
	case(10):
		mes = "Outrubro";
		break;
	case(11):
		mes = "Novembro";
		break;
	case(12):
		mes = "Dezembro";
		break;
	}
	
	int primeiro = dia_semana(ano, m, 1);

	cout << mes << "/" << ano << endl;
	cout << "Dom\t" << "Seg\t" << "Ter\t" << "Qua\t" << "Qui\t" << "Sex\t" << "Sab\n";

	for (int j = 0; j < primeiro; j++)
		cout << "\t";

	for (int i = 1; i <= dias(m, ano); i++)
	{
		cout << i << "\t";
		if (dia_semana(ano, m, i) == 6)
			cout << endl;

	}
	cout << endl;
}



int main()
{
	int ano;
	cout << "Introduza o ano : ";
	cin >> ano;

	for (int i = 1; i <= 12; i++)
		calendario(ano, i);
	
	
	_getwch();
	return 0;
}