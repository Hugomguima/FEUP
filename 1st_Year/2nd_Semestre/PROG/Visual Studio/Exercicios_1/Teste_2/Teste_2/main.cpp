#include<iostream>
#include<string>

using namespace std;

int menor_ou_igual_data(string data1, string data2)
{
	//Esta função compara entre duas datas para ver qual é a maior
	int a1, a2, m1, m2, d1, d2;
	int index1, index2;


	index1 = data1.find('/');
	a1 = stoi(data1.substr(0, index1));
	data1.erase(0, index1 + 1);


	index1 = data1.find('/');
	m1 = stoi(data1.substr(0, index1));
	data1.erase(0, index1 + 1);

	d1 = stoi(data1);

	index2 = data2.find('/');
	a2 = stoi(data2.substr(0, index2));
	data2.erase(0, index2 + 1);

	index2 = data2.find('/');
	m2 = stoi(data2.substr(0, index2));
	data2.erase(0, index2 + 1);

	d2 = stoi(data2);





	//return 1 significa data1 menor que data2
	//return 0 significa data1 maior que data2

	if (a1 < a2) return 1;       //Comparar anos
	else if (a2 < a1) return 0;
	else if (m1 < m2) return 1;  //Comparar meses
	else if (m2 < m1) return 0;
	else if (d1 < d2) return 1;  //Comparar dias
	else if (d2 < d1) return 0;
	else if (d2 == d1) return 1;
	else return 0;

}


int main()
{
	cout << menor_ou_igual_data("2019/03/10", "2019/03/1");




	_getwch();
	return 0;
}