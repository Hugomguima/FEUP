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

int main()
{

	vector<int> vec = { 1,2,2,2,5,6,7,8,12,12,14,15,15,15,15,20};


	removeDuplicates(vec);

	_getwch();
	return 0;
}