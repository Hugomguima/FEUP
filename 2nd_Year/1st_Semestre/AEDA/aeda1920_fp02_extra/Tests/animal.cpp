
#include "animal.h"
#include <sstream>
using namespace std;

/*
 * Classe Animal
 */

string Animal::getNome() const {
	return nome;
}

Animal::Animal(string nome, int idade) {
    this -> nome = nome;
    this -> idade = idade;
}

int Animal::getMaisJovem() {
    return maisJovem;
}


Cao::Cao(string nome, int idade, string raca):Animal(nome,idade) {
    this -> raca = raca ;
}

Voador::Voador(int vmax, int amax) {
    velocidade_max = vmax;
    altura_max = amax;
}

Morcego::Morcego(string nome, int idade, int vmax, int amax):Animal(nome,idade),
Voador(vmax,amax){}
