#include "frota.h"
#include <string>

using namespace std;


void Frota::adicionaVeiculo(Veiculo *v1) {veiculos.push_back(v1);}

int Frota::numVeiculos() const {return veiculos.size();}

int Frota::menorAno() const {
    if(numVeiculos() == 0) return 0;
    int menor = veiculos[0]->getAno();
    for(size_t i = 1; i < veiculos.size();i++)
    {
        if( veiculos[i]->getAno() < menor) menor = veiculos[i]->getAno();
    }
    return menor;
}

ostream &operator<<(ostream &o, const Frota &f) {
    for(size_t i = 0; i < f.veiculos.size(); i++)
    {
        int infoV = f.veiculos[i]->info();
    }
    return o;
}

vector<Veiculo *> Frota::operator()(int anoM) const {
    vector<Veiculo *> v;
    for(auto veiculo : veiculos)
    {
        if(veiculo->getAno() == anoM) v.push_back(veiculo);
    }

    return v;
}

float Frota::totalImposto() const {
    float total = 0;
    for(auto veiculo : veiculos)
    {
        total += veiculo->calcImposto();
    }
    return total;
}
