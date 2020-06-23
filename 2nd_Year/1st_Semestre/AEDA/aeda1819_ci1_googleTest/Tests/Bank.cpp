/*
 * Bank.cpp
 */

#include "Bank.h"
#include <algorithm>
#include <string>

bool comp(Account* a1,  Account* a2)
{
    if(a1->getBalance() == a2->getBalance()) return (a1->getCodIBAN() < a2->getCodIBAN());
    return(a1->getBalance() < a2->getBalance());
}

Bank::Bank() {}

void Bank::addAccount(Account *a) {
	accounts.push_back(a);
}

void Bank::addBankOfficer(BankOfficer b){
	bankOfficers.push_back(b);
}

vector<BankOfficer> Bank::getBankOfficers() const {
	return bankOfficers;
}

vector<Account *> Bank::getAccounts() const {
	return accounts;
}


// ----------------------------------------------------------------------------------------------

// a alterar
double Bank::getWithdraw(string cod1) const{
    double total = 0.0;
    vector<Account*>::const_iterator it;
    for(it = accounts.begin(); it != accounts.end(); it++ )
    {
        if((*it)->getCodH() == cod1) total+=(*it)->getWithdraw();
    }
	return total;
}


// a alterar
vector<Account *> Bank::removeBankOfficer(string name){
	vector<Account *> res;
    vector<BankOfficer>::const_iterator it;
    for(it = bankOfficers.begin(); it !=bankOfficers.end();it++)
    {

        if( it->getName() == name)
        {
            vector<Account *> contas = it->getAccounts();
            vector<Account *>::const_iterator ita;
            for(ita = contas.begin(); ita!=contas.end();ita++ )
            {
                res.push_back(*ita);
            }
            bankOfficers.erase(it);
            it--;
        }
    }
	return res;
}


// a alterar
const BankOfficer & Bank::addAccountToBankOfficer(Account *ac, string name) {

    vector<BankOfficer>::iterator it;

    for(it = bankOfficers.begin(); it != bankOfficers.end();it++)
    {
        if( it->getName() ==name)
        {
            it->addAccount(ac);
            return *it;
        }
    }
    throw NoBankOfficerException(name);
}


// a alterar
void Bank::sortAccounts() {
    sort(accounts.begin(),accounts.end(),comp);
}

