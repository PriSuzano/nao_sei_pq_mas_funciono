#include <bits/stdc++.h>
 
using namespace std;
typedef pair <int, int> pii;
 
int main(){
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);
 
    int nodos, kVidente, aux;
    cin >> nodos >> kVidente;
 
    vector < vector <int> > arvorinha(nodos+1);
 
    for(int i=1; i<=nodos-1; i++){
        cin >> aux;
 
        arvorinha[aux].push_back(i+1);
        arvorinha[i+1].push_back(aux);
    }
 
    queue <int> fila;
    vector <bool> visitados(nodos+1);
    vector <int> profundidade(nodos+1);
    vector <int> paizao(nodos+1);
    priority_queue <pii> filaPrior;
    int pai=1;
    profundidade[pai] = 1;
    fila.push(pai);
 
    while(!fila.empty()){
        pai = fila.front();
        fila.pop();
        visitados[pai] = true;
 
        for(int filhos : arvorinha[pai]){
 
            if(!visitados[filhos]){
                profundidade[filhos] = profundidade[pai]+1;
                paizao[filhos] = pai;
                fila.push(filhos);
                visitados[filhos] = true;
            }
        }
 
        if(arvorinha[pai].size()==1){
            filaPrior.push(pii(profundidade[pai],pai));
        }
    }
 
    vector <bool> visitados2(nodos+1);
    visitados2[0]=true;
    priority_queue <int> maiorEfeitoDomino;
    int folha;
 
    while(!filaPrior.empty()){
        folha = filaPrior.top().second;
        filaPrior.pop();
        visitados2[folha];
        int caminho=1;
        
        while (!visitados2[paizao[folha]]){
            caminho++;
            folha = paizao[folha];
            visitados2[folha] = true;                       
        }
        maiorEfeitoDomino.push(caminho);
    }
 
    int cont=0;
    for(int i=0; i<kVidente; i++){
        cont += maiorEfeitoDomino.top();
        maiorEfeitoDomino.pop();
    }
 
    cout << cont << endl;
 
    return 0;
}

#include <bits/stdc++.h>

using namespace std;
typedef pair <int, int> pii;

int main(){
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);

	int nodos, kVidente, aux;
	cin >> nodos >> kVidente;

	vector < vector <int> > arvorinha(nodos+1);

	for(int i=1; i<=nodos-1; i++){
		cin >> aux;

		arvorinha[aux].push_back(i+1);
		arvorinha[i+1].push_back(aux);
	}

	queue <int> fila;
	vector <bool> visitados(nodos+1);
	vector <int> profundidade(nodos+1);
	vector <int> paizao(nodos+1);
	priority_queue <pii> filaPrior;
	int pai=1;
	profundidade[pai] = 1;
	fila.push(pai);

	while(!fila.empty()){
		pai = fila.front();
		fila.pop();
		visitados[pai] = true;

		for(int filhos : arvorinha[pai]){

			if(!visitados[filhos]){
				profundidade[filhos] = profundidade[pai]+1;
				paizao[filhos] = pai;
				fila.push(filhos);
				visitados[filhos] = true;
			}
		}

		if(arvorinha[pai].size()==1){
			filaPrior.push(pii(profundidade[pai],pai));
		}
	}

	vector <bool> visitados2(nodos+1);
	visitados2[0]=true;
	priority_queue <int> maiorEfeitoDomino;
	int folha;

	while(!filaPrior.empty()){
		folha = filaPrior.top().second;
		filaPrior.pop();
		visitados2[folha];
		int caminho=1;
		
		while (!visitados2[paizao[folha]]){
			caminho++;
			folha = paizao[folha];
			visitados2[folha] = true;						
		}
		maiorEfeitoDomino.push(caminho);
	}

	int cont=0;
	for(int i=0; i<kVidente; i++){
		cont += maiorEfeitoDomino.top();
		maiorEfeitoDomino.pop();
	}

	cout << cont << endl;

	return 0;
}