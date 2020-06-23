#include <iostream>
using namespace std;

double area(double x1, double y1, double x2, double y2, double x3, double y3)
{
	double ab = sqrt((y1 - y2)*(y1 - y2) + (x1 - x2)*(x1 - x2));
	double ac = sqrt((y1 - y3)*(y1 - y2) + (x1 - x3)*(x1 - x3));
	double cb = sqrt((y3 - y2)*(y3 - y2) + (x3 - x2)*(x3 - x2));

	double s = (ab + ac + cb) / 2;

	return sqrt(s*(s - ab)*(s - ac)*(s - cb));
}
double distance(double x1, double y1, double x2, double y2)
{
	return sqrt((x1 - x2)*(x1 - x2) + (y1 - y2)*(y1 - y2));
}

int main()
{
	cout << area(0, 0, 0, 5, 2, 0) << endl;
	cout << distance(0, 3, 2, 6) << endl;

	_getwch();
	return 0;
}