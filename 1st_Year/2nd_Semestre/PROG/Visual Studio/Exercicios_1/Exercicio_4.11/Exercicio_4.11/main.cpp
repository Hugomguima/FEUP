#include<iostream>
#include<vector>
#include<string>
#include<algorithm>

using namespace std;


void removeDuplicates(vector<int> &v)
{
	sort(v.begin(), v.end());
	v.erase(unique(v.begin(), v.end()), v.end());

	for (size_t i = 0; i < v.size(); i++)
		cout << v[i] << endl;
}

void intersection ( vector<int> &v1, vector<int> &v2)
{

	vector<int> v3 = {};

	sort(v1.begin(), v1.end());
	v1.erase(unique(v1.begin(), v1.end()), v1.end());

	sort(v2.begin(), v2.end());
	v2.erase(unique(v2.begin(), v2.end()), v2.end());

	int counter = 0;

	for (size_t i = 0; i < v1.size(); i++)
	{
		for (size_t j = 0 ; j < v2.size(); j++)
		{
			if (v1[i] == v2[j])
			{
				v3.push_back(v1[i]);
			}
		}

	}

	for (size_t k = 0; k < v3.size(); k++)
		cout << v3[k] << endl;
	cout << endl;
}

void reunion(vector<int> &v1, vector<int> &v2)
{
	vector<int> v3 = {};

	sort(v1.begin(), v1.end());
	v1.erase(unique(v1.begin(), v1.end()), v1.end());

	sort(v2.begin(), v2.end());
	v2.erase(unique(v2.begin(), v2.end()), v2.end());

	for (size_t i = 0; i < v1.size(); i++)
		v3.push_back(v1[i]);
	
	for (size_t j = 0; j < v2.size(); j++)
		v3.push_back(v2[j]);

	
	sort(v3.begin(), v3.end());
	v3.erase(unique(v3.begin(), v3.end()), v3.end());

	for (size_t k = 0; k < v3.size(); k++)
		cout << v3[k] << endl;
	cout << endl;
}

int main()
{
	vector<int> v1 = { 2,2,3,4,5,1,2 };
	vector<int> v2 = { 1,4,2,7 };

	intersection(v1, v2);
	reunion(v1, v2);


	_getwch();
	return 0;
}