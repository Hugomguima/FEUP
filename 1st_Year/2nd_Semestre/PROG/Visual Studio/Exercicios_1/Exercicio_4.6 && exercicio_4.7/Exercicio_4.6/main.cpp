#include<iostream>
#include<vector>

using namespace std;

void readIntArray(int a[], int nElem)
{
	for (int i = 0; i < nElem; i++)
		cout << i << "\t" << a[i] << endl;
}

int searchValueInIntArray(const int a[], int nElem, int value)
{
	int list[1] = {-1};
	for (int i = 0; i < nElem; i++)
	{
		if (a[i] == value)
		{
			list[0] = i;
			break;
		}
	}


	return list[0];
}
int MultValueInIntArray(const int a[], int nElem, int value, int index[])
{
	int counter = 0;
	for (int i = 0; i < nElem; i++)
	{
		if (a[i] == value)
		{
			index[counter] = value;
			counter++;
		}
	}
	return counter;
}

void readIntVector(const vector<int> &v, int nElem)
{
	for (int i = 0; i < nElem; i++)
		cout << i << "\t" << v[i] << endl;

}int searchValueInIntVector(const vector<int> &v, int value)
{
	int list[1] = { -1 };
	for (size_t i = 0; i < v.size(); i++)
	{
		if (v[i] == value)
		{
			list[0] = i;
			break;
		}
	}


	return list[0];

}

int searchMultValueInIntVector(const vector<int> &v, int value)
{
	int counter = 0;
	for (size_t i = 0; i < v.size(); i++)
	{
		if (v[i] == value)
		{
			counter++;
		}
	}
	return counter;
}

int main()
{
	/*
	int arr[] = { 5,8,4,12 };
	readIntArray(arr, 3);

	int asd[] = { 5,8,4,12 };
	cout << searchValueInIntArray(asd, 2, 4);

	int asd[] = { 5,8,4,4,12,6,4,3,5,7,7,1,1 };
	int cvb[100] = {};
	cout << MultValueInIntArray(asd, 5, 20,cvb);

	vector<int> myvector = { 5,7,8,3 };
	readIntVector(myvector, 4);
	
	vector<int> vec = { 7,6,23,56,38 };

	cout << searchValueInIntVector(vec, 56);


	vector<int> asd = { 5,8,4,4,12,6,4,3,5,7,7,1,1 };
	int cvb[100] = {};
	cout << searchMultValueInIntVector(asd, 7);
	*/

	_getwch();
	return 0;


}