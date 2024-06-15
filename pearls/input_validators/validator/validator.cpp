#include "validator.h"
#include "bits/stdc++.h"

typedef long long ll;





void run() {
    //string mode = Arg("mode", "none");
    int maxA = Arg("maxA", 200000);
	int maxB = Arg("maxB", 200000);
	int maxK = Arg("maxK",26*26-1);
	int maxQ = Arg("maxQ", 100000);
    
	int la = Int(1,maxA);
	Space();
	int lb = Int(1,maxB);
	Space();
	int k = Int(0,maxK);
	Space();
	int q = Int(1, maxQ);
	Endl();

	string a = Line();
	string b = Line();
	assert(a.size() == la && b.size() == lb);

	for (int i = 0; i < la; i++){
		assert('a' <= a[i] && a[i] <= 'z');
	}
	for (int i = 0; i < lb; i++){
		assert('a' <= b[i] && b[i] <= 'z');
	}

	for (int i = 0; i < k; i++){
		char u = Char();
		Space();
		char v = Char();
		Endl();

		assert('a' <= u && u <= 'z');
		assert('a' <= v && v <= 'z');
	}

	for (int i = 0; i < q; i++){
		ll query = Int(0,(ll)la * (ll)lb * (ll)2- (ll)1); // Could be bounded even more, but gen_random makes sure that the query will be valid
		Endl();
	}

    Eof();
}
