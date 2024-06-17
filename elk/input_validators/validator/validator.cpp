#include "validator.h"
#include "bits/stdc++.h"

typedef long long ll;


vector<vector<int > > graph(50000,vector<int>());
vector<int> visited(50000,0);


void DFS(int curr){
	for (int &nxt: graph[curr]){
		if (visited[nxt]) continue;
		visited[nxt] = 1;
		DFS(nxt);
	}
}


void run() {
    string mode = Arg("mode", "none");
    int maxN = Arg("maxN", 50000);
	int maxM = Arg("maxM", 100000);
	
    
	int N = Int(2,maxN);
	Space();
	int M = Int(2,maxM);
	Space();
	int A = Int(0,N-1);
	Space();
	int B = Int(0,N-1);
	Endl();

	assert(A != B);

	vector<pair<int, int > > edges;
	//vector<vector<int > > graph(N,vector<int>());

	for (int i = 0; i < M; i++){
		int u = Int(0,N-1);
		Space();
		int v = Int(0,N-1);
		Endl();

		assert (u != v);

		if (v < u) swap(u,v);

		edges.push_back({u,v});
		graph[u].push_back(v);
		graph[v].push_back(u);
	} 

	sort(edges.begin(), edges.end());


	// Check that all edges are unique
	for (int i = 0; i < edges.size()-1; i++){
		int x1,y1,x2,y2;

		tie(x1,y1) = edges[i];
		tie(x2,y2) = edges[i+1];

		assert(!(x1 == x2 && y1 == y2));
	}

	DFS(A);

	assert(visited[B] == 1);


	if (mode == "tree"){
		assert(M == N-1);
		for (int i = 0; i < N; i++) assert(visited[i]);
	}
	

    Eof();
}
