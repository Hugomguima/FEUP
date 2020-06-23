#include "veiculo.h"
#include "frota.h"
#include <iostream>
#include <utility>

using namespace std;

Veiculo::Veiculo(string mc, int m, int a): marca(std::move(mc)), mes(m), ano(a) {}

string Veiculo::getMarca() const {return marca;}

bool Veiculo::operator<(const Veiculo &v) const {
    if(ano < v.ano) return true;
    if(ano > v.ano) return false;
    return mes < v.mes;
}

int Veiculo::getAno() const {return ano;}

const Frota Veiculo::info() const {
    cout << "marca: " << marca << endl;
    cout << "ano: " << ano << endl;
    cout << "mes : " << mes;

    return 3;
}

Motorizado::Motorizado(string mc, int m, int a, string c, int cil): Veiculo(std::move(mc),m,a),
combustivel(std::move(c)), cilindrada(cil){}

string Motorizado::getCombustivel() const {return combustivel;}

int Motorizado::info() const {
    Veiculo::info();
    cout << endl;
    cout << "combustivel: " << combustivel << endl;
    cout << "cilindrada: " << cilindrada;

    return 5;
}

float Motorizado::calcImposto() const {

    if(combustivel == "gasolina" && cilindrada <= 1000 && ano > 1995) return 14.56;
    if(combustivel == "gasolina" && cilindrada > 1000 && cilindrada <= 1300 && ano > 1995) return 29.06;
    if(combustivel == "gasolina" && cilindrada > 1300 && cilindrada <= 1750 && ano > 1995) return 45.15;
    if(combustivel == "gasolina" && cilindrada > 1750 && cilindrada <= 2600 && ano > 1995) return 113.98;
    if(combustivel == "gasolina" && cilindrada > 2600 && cilindrada <= 3500 && ano > 1995) return 181.17;
    if(combustivel == "gasolina" && cilindrada > 3500 && ano > 1995) return 320.89;

    if(combustivel == "gasolina" && cilindrada <= 1000 && ano <= 1995) return 8.1;
    if(combustivel == "gasolina" && cilindrada > 1000 && cilindrada <= 1300 && ano <= 1995) return 14.56;
    if(combustivel == "gasolina" && cilindrada > 1300 && cilindrada <= 1750 && ano <= 1995) return 22.65;
    if(combustivel == "gasolina" && cilindrada > 1750 && cilindrada <= 2600 && ano <= 1995) return 54.89;
    if(combustivel == "gasolina" && cilindrada > 2600 && cilindrada <= 3500 && ano <= 1995) return 87.13;
    if(combustivel == "gasolina" && cilindrada > 3500 && ano <= 1995) return 148.37;


    if(combustivel != "gasolina" && cilindrada <= 1500 && ano > 1995) return 14.56;
    if(combustivel != "gasolina" && cilindrada > 1500 && cilindrada <= 2000 && ano > 1995) return 29.06;
    if(combustivel != "gasolina" && cilindrada > 2000 && cilindrada <= 3000 && ano > 1995) return 45.15;
    if(combustivel != "gasolina" && cilindrada >= 3000 && ano > 1995) return 113.98;

    if(combustivel != "gasolina" && cilindrada <= 1500 && ano <= 1995) return 8.1;
    if(combustivel != "gasolina" && cilindrada > 1500 && cilindrada <= 2000 && ano <= 1995) return 14.56;
    if(combustivel != "gasolina" && cilindrada > 2000 && cilindrada <= 3000 && ano <= 1995) return 22.65;
    if(combustivel != "gasolina" && cilindrada >= 3000 && ano <= 1995) return 54.89;

    return 0;
}

Automovel::Automovel(string mc, int m, int a, string c, int cil) : Motorizado(std::move(mc), m, a, c, cil) {}

int Automovel::info() const {return Motorizado::info();}

Camiao::Camiao(string mc, int m, int a, string c, int cil, int cm): Motorizado(std::move(mc),m,a,c,cil),
carga_maxima(cm) {}

int Camiao::info() const {
    Motorizado::info();
    cout << endl;
    cout << "carga maxima: " << carga_maxima;
    return 6;
}

Bicicleta::Bicicleta(string mc, int m, int a, string t): Veiculo(mc,m,a),tipo(std::move(t)) {}

int Bicicleta::info() const {
    Veiculo::info();
    cout << endl;
    cout << "tipo: " << endl;
    return 4;
}

float Bicicleta::calcImposto() const {return 0;}
