#include <iostream>
#include <vector>

using namespace std;

/**
 * Versao da classe generica Grafo usando a classe vector
 */

template <class N, class A> class Aresta;

template <class N, class A>
class No {
public:
	N info;
	vector< Aresta<N,A> > arestas;
	No(N inf) {
		info = inf;
	}
};

template <class N, class A>
class Aresta {
public:
	A valor;
	No<N,A> *destino;
	Aresta(No<N,A> *dest, A val) {
		valor = val;
		destino = dest;
	}
};

template <class N, class A> 
class Grafo { 
	vector< No<N,A> *> nos;
  public: 
    Grafo() {}
    ~Grafo();
    Grafo & inserirNo(const N &dados);
    Grafo & inserirAresta(const N &inicio, const N &fim, const A &val);
    Grafo & eliminarAresta(const N &inicio, const N &fim);
    A & valorAresta(const N &inicio, const N &fim);
    int numArestas(void) const;
    int numNos(void) const;
    void imprimir(std::ostream &os) const;
    friend ostream &operator<<(ostream &o, const Grafo<N,A> &g);
};

template<class N, class A>
int Grafo<N, A>::numArestas(void) const {
    unsigned int n_arestas = 0;
    typename vector< No<N,A> *>::iterator it;
    for(it = nos.begin() ; it != nos.end;it++)
    {
        n_arestas += (*it)->arestas;
    }
    return n_arestas;
}

template<class N, class A>
int Grafo<N, A>::numNos(void) const {return nos.size();}

template<class N, class A>
Grafo<N, A>::~Grafo() {
    typename vector< No<N,A> *>::iterator it;
    for(it = nos.begin();it != nos.end();it++) delete *it;
}

template<class N, class A>
Grafo<N, A> &Grafo<N, A>::inserirNo(const N &dados) {
    typename vector< No<N,A> *>::iterator it;
    for( it = nos.begin(); it != nos.end();it++)
    {
        if( (*it) == dados) throw NoRepetido(dados);
    }
    No<N,A> * no_novo = new No<N,A> *(dados);
    nos.push_back(no_novo);
    return *this;
}

template<class N, class A>
Grafo<N,A> &Grafo<N, A>::inserirAresta(const N &inicio, const N &fim, const A &val) {

    typename vector< No<N,A> *>::iterator it;
    typename  vector<Aresta<N,A>>::iterator ita;
    bool encontrouInicio = false;
    bool encontrouFim = false;

    No<N,A> *noInicio = NULL;
    No<N,A> *noFim = NULL;

    for(it = nos.begin(); it != nos.end(); it++)
    {
        if((*it)->info == inicio)
        {
            encontrouInicio = true;
            noInicio = *it;
            for(ita = (*it)->arestas.begin(); ita != (*it)->arestas.end();ita++ )
            {
                if ( ita->destino->info == fim) throw ArestaRepetida(inicio, fim);
            }
            if (encontrouFim) break;
        }
        else if((*it)->info == fim)
        {
            encontrouFim = true;
            noFim = *it;
            if(encontrouInicio ) break;
        }
    }
    if(!encontrouInicio) throw NoInexistente(inicio);
    if(!encontrouFim) throw NoInexistente(fim);

    Aresta<N,A> aresta_nova(noFim, val);
    noInicio->arestas.push_back(aresta_nova);

    return *this;
}

template<class N, class A>
void Grafo<N, A>::imprimir(std::ostream &os) const {
    typename vector< No<N,A>*>::const_iterator it;
    typename vector<Aresta<N,A>>::const_iterator ita;

    for(it = nos.begin();it != nos.end(); it++)
    {
        os << "( " << (*it)->info;
        for (ita = (*it)->arestas.begin(); ita != (*it)->arestas.end(); ita ++)
        {
            os << "[ " << ita->destino->info << " " << ita->valor << "] ";
        }
        os << ") ";
    }
}

template<class N, class A>
Grafo<N,A> &Grafo<N, A>::eliminarAresta(const N &inicio, const N &fim) {


    return *this;
}

template<class N, class A>
A &Grafo<N, A>::valorAresta(const N &inicio, const N &fim) {
    typename vector< No<N,A>*>::const_iterator it;
    typename  vector<Aresta<N,A>>::const_iterator ita;

    for(it = nos.begin(); it != nos.end(); it++)
    {
        if ((*it)->info == inicio) {
            for (ita = (*it)->arestas.begin(); ita != (*it)->arestas.end(); ita++) {
                if (ita->destino->info == fim) return ita->valor;
            }
            throw ArestaInexisitente(inicio,fim);
        }
    }
    throw NoInexistente(inicio);
}
template <class N,class A>
ostream &operator<<(ostream &out, const Grafo<N,A> &g) {
    g.imprimir(out);
    return out;
}


template <class N, class A> 
std::ostream & operator<<(std::ostream &out, const Grafo<N,A> &g);


// excecao NoRepetido
template <class N>
class NoRepetido
{
public:
   N info;
   NoRepetido(N inf) { info=inf; }
};
template <class N> 
std::ostream & operator<<(std::ostream &out, const NoRepetido<N> &no)
{ out << "No repetido: " << no.info; return out; }


// excecao NoInexistente
template <class N>
class NoInexistente {
public:
	N info;
	NoInexistente(N inf) {
		info = inf;
	}
};

// excessao ArestaRepetida
template <class N >
class ArestaRepetida {
public:
    N inicio;
    N fim;
    ArestaRepetida(N in,N fi) {
        inicio = in;
        fim = fi;
    }
};

// excessao ArestaInexistente
template <class N >
class ArestaInexistente {
public:
    N inicio;
    N fim;
    ArestaInexistente(N in,N fi) {
        inicio = in;
        fim = fi;
    }
};

template <class N>
std::ostream & operator<<(std::ostream &out, const NoInexistente<N> &ni)
{ out << "No inexistente: " << ni.info; return out; }



