#include <iostream>
#include <string>
#include <map>
#include <fstream>
#include <vector>
#include <iomanip>

using namespace std;

class Coin
{
public:
	Coin(int a, char b);
};

class Purse
{
public:
	Purse();
	void insertCoin(Coin c);
	void insertCoins(vector<Coin> v);
	void  showCoins() const;
	double getTotalAmount() const;
	Coin removeCoin(Coin c);
	vector<Coin> removeAmount(double m);
	vector<Coin> exchangeCoin(Coin c);

private:
	vector<Coin> v_coins;
	int number;
	double ammount;

};






















class Card {
	friend ostream& operator<<(ostream& os, const Card& card);
public:

	Card();
	Card(char suit, unsigned int rank, unsigned int points, bool isFaceUp);
	char getSuit() const; // retorna o naipe
	unsigned int getRank() const; // retorna o valor
	unsigned int getPoints() const; // retorna a pontuação da carta
private:
	char suit; // o naipe da carta: 'C' - copas, 'E' - espadas, 'O' - ouros, 'P' - paus
	unsigned int rank; // o valor da carta: 1 - ás, 2 - duque, ..., 11 - valete, 12 - dama, 13 - rei
	unsigned int points; // a pontuação da carta: ás - 11, duque - 2, ..., valete/dama/rei - 10
	bool isFaceUp; // true = face virada para cima
};
class Hand {
public:
	Hand();
	void addCard(Card c); // acrescenta uma carta à mão
	Card getCard(); // retira uma carta da mão
	void show() const; // mostra as cartas da mão, no estado em que cada uma estiver
	unsigned int getPointsTotal() const; // obtém a pontuação total das cartas da mão
private:
	vector<Card> cards; // o conteúdo da mão
};

string cardRankToSymbol(unsigned int rank)
{
	string arr[] = {"A","2","3","4","5","6","7","8","9","10","J","Q","K"};
	
	if (1 <= rank && rank <= 13) return arr[rank-1];
	return "Invalid card!";
}
string cardRankToSymbol2(unsigned int rank)
{
	map<int, string> m;
	if (rank < 1 || rank > 13) return "Invalid card!";

	m.insert(pair<int, string>(1, "A"));
	m.insert(pair<int, string>(2, "2"));

	return m[rank];
}
template <class T>
T absolute(T number)
{
	if (number < 0) return -number;
	return number;
}

bool match(const string pat, const string dic)
{
	if (pat.size() != dic.size()) return false;
	for (int i = 0; i < pat.size(); i++) if (pat[i] != '.' && tolower(pat[i]) != dic[i]) return false;
	return true;
}



int main()
{
	
	Purse p1, p2;
	Coin e10(10, 'C'), e20(20, 'C'), e50(50, 'C'), e1(1, 'E'), e2(2, 'E');
	vector<Coin> v = { e10,e10,e10,e10,e10,e20,e20,e20,e20,e20,e50,e1 };

	p1.insertCoin(e2);
	p2.insertCoin(e2);

	p1.insertCoins(v);
	p2.insertCoins(v);


	p2.insertCoins(p1.exchangeCoin(e2));

	p2.showCoins();


	_getwch();
	return 0;
}

Card::Card(char suit, unsigned int rank, unsigned int points, bool isFaceUp)
{
	this->suit = suit;
	this->rank = rank;
	this->points = points;
	this->isFaceUp = isFaceUp;
}

ostream & operator<<(ostream & os, const Card & card)
{
	
	if (card.isFaceUp)
	{
		os << setw(4) << cardRankToSymbol(card.rank) + "." + to_string(card.points);
		return os;
	}
	os << setw(4) << "XXXX";
	return os;
	// TODO: insert return statement here
}

unsigned int Hand::getPointsTotal() const
{
	unsigned int result = 0;
	unsigned ace = 0;
	for (size_t i = 0; cards.size(); i++)
	{
		result += cards[i].getPoints();
		if (cards[i].getRank() == 1) ace += 1;
	}
	if (result < 21) return result;
	return result - 10 * ace;
}
