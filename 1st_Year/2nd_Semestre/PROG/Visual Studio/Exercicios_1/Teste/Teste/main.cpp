#include<iostream>
#include<iomanip>
#include<cmath>
#include<cctype>
#include<cstdlib>
#include<ctime>
#include<string>
#include<iomanip>
#include<sstream>
#include<vector>

using namespace std;

int menor_ou_igual_data(string data1, string data2)
{
	//Esta função compara entre duas datas para ver qual é a maior
	int a1, a2, m1, m2, d1, d2;
	int index1, index2;
	int counter1 = 0;
	int counter2 = 0;

	cout << data1 << endl << data2 << endl;


	index1 = data1.find('/');
	a1 = stoi(data1.substr(0, index1));
	data1.erase(0, index1);

	index1 = data1.find('/');
	m1 = stoi(data1.substr(0, index1));
	data1.erase(0, index1);

	index1 = data1.find('/');
	d1 = stoi(data1.substr(0, index1));
	data1.erase(0, index1);

	index2 = data2.find('/');
	a1 = stoi(data2.substr(0, index2));
	data2.erase(0, index2);

	index2 = data2.find('/');
	m2 = stoi(data2.substr(0, index2));
	data2.erase(0, index2);

	index2 = data2.find('/');
	d2 = stoi(data2.substr(0, index2));
	data2.erase(0, index2);

	cout << a1 << endl << m1 << endl << d1 << endl;
	



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
	/*
	string name;
	unsigned int age;
	cout << "Insert your 'name' and 'age': "; cin >> name >> age;
	cout << "Name and age : " << name << " / " << age << endl;
	*/
	
	/*
	string num = "Hello world";

	cout << setw(20) << num;
	*/

	/*
	double num = 12.56789;

	cout << setprecision(4) << num << endl;
	cout << setprecision(9) << num << endl;
	cout << setprecision(4) << fixed << num << endl;
	cout << fixed << setprecision(9) << num << endl;

	*/
	
	cout << menor_ou_igual_data("2019/03/01", "2019/03/10");
	

	_getwch();
	return 0;
}

/*
if (v_clients[j].pacotes_comprados.find(v_packs[i].identificador) != -1);
					{
						valor += stoi(v_clients[j].agregado) * stoi(v_packs[i].preco_pessoa);
						counter++;
					}
*/