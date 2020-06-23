#include "parque.h"
#include "insertionSort.h"
#include "sequentialSearch.h"
#include <algorithm>
#include <vector>

using namespace std;

bool InfoCartao::operator==(const InfoCartao &inf) const {
    return nome == inf.nome;
}

bool InfoCartao::operator<(const InfoCartao &inf) const {
    if (frequencia > inf.frequencia) return true;
    if (frequencia < inf.frequencia) return false;
    return nome < inf.nome;

}
bool CompNome(const InfoCartao & c1, const InfoCartao & c2 ){
    return c1.nome < c2.nome;
}

ParqueEstacionamento::ParqueEstacionamento(unsigned int lot, unsigned int nMaxCli):
	lotacao(lot), numMaximoClientes(nMaxCli) {
    numClientes = 0;
    vagas=lot; 
}

ParqueEstacionamento::~ParqueEstacionamento() {}

vector<InfoCartao> ParqueEstacionamento::getClientes() const { return clientes; }

unsigned int ParqueEstacionamento::getNumLugares() const { return lotacao; }

unsigned int ParqueEstacionamento::getNumLugaresOcupados() const { return lotacao-vagas; }


// a imnplementar
int ParqueEstacionamento::posicaoCliente(const string &nome) const
{
    InfoCartao info;
    info.nome = nome;
    return sequentialSearch(clientes,info);
}

//a implementar
int ParqueEstacionamento::getFrequencia(const string &nome) const
{
    int pos = posicaoCliente(nome);
    if (pos==-1) throw ClienteNaoExistente(nome);

    return clientes[pos].frequencia;
}

// a alterar/atualizar ?
bool ParqueEstacionamento::adicionaCliente(const string & nome)
{
 	if ( numClientes == numMaximoClientes ) return false;
	if ( posicaoCliente(nome) != -1 ) return false;
	InfoCartao info;
	info.nome = nome;
    info.presente = false;
    info.frequencia = 0;
	clientes.push_back(info);
	numClientes++;
	return true;
}

// a alterar/atualizar ?
bool ParqueEstacionamento::retiraCliente(const string & nome)
{
	for (vector<InfoCartao>::iterator it = clientes.begin(); it != clientes.end(); it++)
		if ( it->nome == nome ) {
			if ( it->presente == false ) {
				clientes.erase(it);
				numClientes--;
				return true;
			}
			else return false;
		}
	return false;
}

// a alterar/atualizar ?
bool ParqueEstacionamento::entrar(const string & nome)
{
	if ( vagas == 0 ) return false;
	int pos = posicaoCliente(nome);
	if ( pos == -1 ) return false;
	if ( clientes[pos].presente == true ) return false;
	clientes[pos].presente = true;
	vagas--;
	clientes[pos].frequencia+=1;
	return true;
}

// a alterar/atualizar ?
bool ParqueEstacionamento::sair(const string & nome)
{
	int pos = posicaoCliente(nome);
	if ( pos == -1 ) return false;
	if ( clientes[pos].presente == false ) return false;
	clientes[pos].presente = false;
	vagas++;
	return true;
}

		
// a implementar
void ParqueEstacionamento::ordenaClientesPorFrequencia()
{
    insertionSort(clientes);
}


// a implementar
void ParqueEstacionamento::ordenaClientesPorNome()
{
    sort(clientes.begin(),clientes.end(),CompNome);
}


// a implementar
vector<string> ParqueEstacionamento::clientesGamaUso(int n1, int n2)
{
    vector<string> nomes;
    vector<InfoCartao>::const_iterator it;
    vector<InfoCartao> temp = clientes;
    insertionSort(temp);
    for(it = temp.begin(); it != temp.end(); it++)
    {
        if((*it).frequencia >= n1 && (*it).frequencia <= n2) nomes.push_back(it->nome);
    }
    return nomes;

}


// a implementar
ostream & operator<<(ostream & os, const ParqueEstacionamento & pe)
{
    vector<InfoCartao>::const_iterator it;
    string presenca;
    for(it = pe.clientes.begin(); it != pe.clientes.end();it++)
    {
        if(it->presente) presenca = "Sim"; else presenca ="Nao";
        os << "Nome :" << it->nome << endl;
        os << "Presente: " << presenca << endl;
        os << "Frequencia: " << it->frequencia << endl;
    }
    return os;
}


// a implmentar
InfoCartao ParqueEstacionamento::getClienteAtPos(vector<InfoCartao>::size_type p) const
{
    if( p >= clientes.size()) throw PosicaoNaoExistente(p);
    return clientes[p];
}


