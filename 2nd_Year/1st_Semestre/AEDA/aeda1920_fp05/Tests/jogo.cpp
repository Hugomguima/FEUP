/*
 * jogo.cpp
 */

#include "jogo.h"
#include <cstdlib>
#include <ctime>
#include <iostream>
using namespace std;



unsigned int Jogo::numPalavras(string frase)
{
  if ( frase.length() == 0 ) return 0;

  unsigned n=1;
  size_t pos = frase.find(' ');
  while (pos != string::npos) {
    frase = frase.substr(pos+1);
    pos = frase.find(' ');
    n++;
  }
  return n;
}

// a implementar
Jogo::Jogo(){}

// a implementar
Jogo::Jogo(list<Crianca>& lc2):criancas(lc2){}

// a implementar
void Jogo::insereCrianca(const Crianca &c1)
{
    criancas.push_back(c1);
}

// a implementar
list<Crianca> Jogo::getCriancasJogo() const
{
    return criancas;
}

// a implementar
string Jogo::escreve() const
{
    string final;
    list<Crianca>::const_iterator it;
    for(it = criancas.begin(); it != criancas.end();it++)
    {
        final += it->escreve() + '\n';
    }
    return final;
}

// a implementar
Crianca& Jogo::perdeJogo(string frase)
{

    int num = numPalavras(frase);
    while(criancas.size() > 1)
    {
        int index = (num-1) % criancas.size();
        list<Crianca>::iterator it = criancas.begin();
        for(size_t i = 0; i < index;i++) it++;
        criancas.erase(it);
    }
    return *(criancas.begin());
}

// a implementar
list<Crianca>& Jogo::inverte()
{
    criancas.reverse();
    return criancas;
}

// a implementar
list<Crianca> Jogo::divide(unsigned id)
{
    list<Crianca> removed;
    list<Crianca>::iterator it = criancas.begin();
    while(it != criancas.end())
    {
        if( it->getIdade() > id)
        {
            removed.push_back(*it);
            it = criancas.erase(it);
        }
        else it++;
    }

    return removed;
}

// a implementar
void Jogo::setCriancasJogo(const list<Crianca>& l1)
{
    criancas = l1;
}

// a implementar
bool Jogo::operator==(Jogo& j2)
{

    list<Crianca>::const_iterator it = criancas.begin();
    list<Crianca>::const_iterator it2 = j2.criancas.begin();

    if(criancas.size() != j2.criancas.size()) return false;
    while(it!=criancas.end() && it2!=j2.criancas.end())
    {
        if(!(*it == *it2)) return false;

        it++;
        it2++;
    }

	return true;
}

// a implementar
list<Crianca> Jogo::baralha() const
{
    list<Crianca> nova_criancas;
    list<Crianca> copia;
    for(list<Crianca>::const_iterator ita = criancas.begin(); ita != criancas.end();ita++)
    {
        copia.push_back(*ita);
    }

    int size = copia.size();
    while(copia.size() > 0)
    {
        list<Crianca>::const_iterator it = copia.begin();
        int index = rand() % size;
        for(size_t i = 0; i < index; i++) it++;
        nova_criancas.push_back(*it);
        copia.erase(it);

        size--;
    }

    return nova_criancas;
}
