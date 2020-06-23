#include<iostream>
#include<string>
#include<sstream>

using namespace std;


double executeOperation(string op)
{
	stringstream num(op);
	char operation;
	int digit;
	double x = 0;
	num >> x;

	
	if (op.find('+') != -1)
	{
		digit = op.find('+');
		op.erase(0, digit + 1);
		stringstream num_2(op);
		double y = 0;
		num_2 >> y;
		return x + y;
	}
	if (op.find('-') != -1)
	{
		digit = op.find('-');
		op.erase(0, digit + 1);
		stringstream num_2(op);
		double y = 0;
		num_2 >> y;
		return x - y;
	}
	if (op.find('*') != -1)
	{
		digit = op.find('*');
		op.erase(0, digit + 1);
		stringstream num_2(op);
		double y = 0;
		num_2 >> y;
		return x * y;
	}
	if (op.find('/') != -1)
	{
		digit = op.find('/');
		op.erase(0, digit + 1);
		stringstream num_2(op);
		double y = 0;
		num_2 >> y;
		return x / y;
	}
	

	return 0;
	
}

int main()
{

	cout << executeOperation("12.3 + 5");



	_getwch();
	return 0;
}