#include<iostream>
#include<fstream>
#include<string>
#include<vector>

using namespace std;

int main()
{
	vector<string> names = {};
	string filename,name;

	cout << "Write the filename : ";
	cin >> filename;
	
	ifstream fin(filename);

	
	while (getline(fin, name))
	{
		names.push_back(name);
	}

	for (int i = 0; i < names.size() - 1; i++)
	{
		for (size_t j = 0; j < names.size() - 1; j++)
		{
			if (names[j] > names[j + 1])
			{
				swap(names[j], names[j + 1]);
			}

		}

	}
	fin.close();

	ofstream fout("names_sorted.txt");
	
	for (size_t k = 0; k < names.size(); k++)
	{
		fout << names[k] << endl;
	}
	fout.close();





	_getwch();
	return 0;
}