/*
 * Account.h
 */

#ifndef SRC_ACCOUNT_H_
#define SRC_ACCOUNT_H_

#include <string>
#include<iostream>
#include<vector>
using namespace std;



class Account {
protected:
	string holder;
	string codeHolder;
	string codeIBAN;
	double balance;
public:
	Account(string hold, string codeH, string codeA, double bal);
	virtual ~Account();
	string getCodH() const;
	string getCodIBAN() const;
	double getBalance() const;
    virtual double getWithdraw()const = 0;
	//...

};


class CheckingAccount: public Account {
	double limit; //lower limit for free checking
public:
	CheckingAccount (string hold, string codeH, string codeA, double bal, double lim);
	double getCharge()const;
    double getWithdraw()const;
	//...

};


class SavingsAccount: public Account {
protected:
	double rate;
public:
	SavingsAccount(string hold, string codeH, string codeA, double bal, double pct); //pct = percentage interest rate
	double getCharge() const;
    virtual double getWithdraw()const;
	//...

};


class TimeAccount: public SavingsAccount {
	double funds_avail;
public:
	TimeAccount(string hold, string codeH, string codeA, double bal, double pct);
	double getWithdraw()const;
	//...

};

template <class T>
unsigned int numberDifferent(const vector<T> & v1)
{
    typename vector<T>::const_iterator it;
    vector<T> vec;
    bool encontrou;

    for(it = v1.begin(); it != v1.end();it++)
    {
        encontrou = false;
        for(size_t i = 0; i< vec.size(); i++)
            if(vec[i] == *it)
            {
                encontrou = true;
                break;
            }
        if(!encontrou) vec.push_back(*it);
    }
    return vec.size();
}

#endif /* SRC_ACCOUNT_H_ */
