#include<iostream>
#include<vector>
#include<string>
#include<algorithm>
#include<string>

using namespace std;

void bubblesort(vector<string> &v)
{
	for (int i = 0; i < v.size() - 1; i++)
	{
		for (size_t j = 0; j < v.size() - 1; j++)
		{
			if (v[j] > v[j + 1])
			{
				swap(v[j], v[j+1]);
			}
				
		}

	}
	for (size_t k = 0; k < v.size(); k++)
		cout << v[k] << endl;

}
void bubblesort_int(vector<int> &v)
{
	for (int i = 0; i < v.size() - 1; i++)
	{
		for (size_t j = 0; j < v.size() - 1; j++)
		{
			if (v[j] > v[j + 1])
			{
				swap(v[j], v[j + 1]);
			}

		}

	}
	for (size_t k = 0; k < v.size(); k++)
		cout << v[k] << endl;

}

int main()
{
	vector<int> v1 = { 7, 4, 6, 9, 3, 12 };
	vector<string> v2 = { "hello","nigga","nigger","jeff" };

	bubblesort_int(v1);
	cout << endl;
	bubblesort(v2);



	_getwch();
	return 0;
}