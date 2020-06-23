/*
 * BankOfficer.cpp
 */
#include "BankOfficer.h"


BankOfficer::BankOfficer(): id(0) {}

void BankOfficer::setName(string nm){
	name = nm;
}

string BankOfficer::getName() const{
	return name;
}

vector<Account *> BankOfficer::getAccounts() const {
	return myAccounts;
}

void BankOfficer::addAccount(Account *a) {
	myAccounts.push_back(a);
}

unsigned int BankOfficer::getID() const{
	return id;
}


// ----------------------------------------------------------------------------------------------

// a alterar
BankOfficer::BankOfficer(string name):name(name) {
    static unsigned int value = 0;
    this->id = ++value;

}

bool BankOfficer::operator>(const BankOfficer &b1) {
    if(myAccounts.size() == b1.myAccounts.size()) return( name > b1.name);
    else return (myAccounts.size() > b1.myAccounts.size());
}



