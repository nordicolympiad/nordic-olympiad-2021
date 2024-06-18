#include "validator.h"
#include "bits/stdc++.h"

typedef long long ll;


vector<vector<int > > graph(20*1000,vector<int>());
vector<int> visited(20*1000,0);


void DFS(int curr){
	for (int &nxt: graph[curr]){
		if (visited[nxt]) continue;
		visited[nxt] = 1;
		DFS(nxt);
	}
}


void run() {
    string mode = Arg("mode", "none");
    int maxN = Arg("maxN", 20);
	int minM = Arg("minM",2);
	int maxM = Arg("maxM", 1000);
	
    
	int N = Int(2,maxN);
	Space();
	int M = Int(minM,maxM);
	Space();
	int A = Int(0,N-1);
	Space();
	int B = Int((M-1)*N,M*N-1);
	Endl();

	int Ksum = 0;

	for (int i = 0; i < N*(M-1); i++){
		int K = Int(1,N);
		Space();

		Ksum += K;

		int currLayer = i/N;
		

		for (int j = 0; j < K; j++){
			int u = Int((currLayer + 1) * N,(currLayer + 2)*N-1);
			graph[i].push_back(u);
			if (j != K-1) Space();
		}
		Endl();

	}


	// Make sure the sum of all K is <= 5000
	assert(Ksum <= 5000);

	
	// Make sure there is a path from a to b.
	DFS(A);
	assert(visited[B]);

	

	// Make sure there is a bipartite matching in all m-1 layers
	// TODO


	
    Eof();
}
