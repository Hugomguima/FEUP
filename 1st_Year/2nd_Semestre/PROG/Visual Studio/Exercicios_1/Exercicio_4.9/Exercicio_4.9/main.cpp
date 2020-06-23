#include<iostream>
#include<vector>
#include<string>

using namespace std;

int binarySearch(const vector <int> &v, int value)
{
	double middle;
	int bottom = 0;
	int top = v.size()-1;
	int found = false;

	while (v[bottom] <= v[top] && found == false)
	{
		middle = (top + bottom) / 2;
		if (v[middle] == value) found = true;
		else if (v[middle] < value) bottom = middle + 1;
		else top = middle - 1;

	}
	return middle;

}

int main()
{
	vector<int> v = { 4,7,12,35,67,98 };
	cout << binarySearch(v,67);

	_getwch();
	return 0;
}