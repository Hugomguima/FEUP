#include <iostream>;
using namespace std;

int main()
{
	int h1, m1, s1, h2, m2, s2, h3, m3, s3, rs, rm, rh, d;

	cout << "Tempo 1 (horas minutos segundos) ? ";
	cin >> h1 >> m1 >> s1;
	cout << "Tempo 2 (horas minutos segundos) ? ";
	cin >> h2 >> m2 >> s2;

	s3 = (s1 + s2) % 60;
	rs = (s1 + s2) / 60;


	m3 = (m1 + m2 + rs) % 60;
	rm = (m1 + m2 + rs) / 60;

	h3 = (h1 + h2 + rm) % 24;
	rh = (h1 + h2 + rm) / 24;

	d = rh % 24;


	cout << "Soma dos tempos : " << d << " dia, " << h3 << " horas, " << m3 << " minutos e " << s3 << " segundos";


	
	return 0;
}
