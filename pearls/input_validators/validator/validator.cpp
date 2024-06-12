#include "validator.h"
#include "bits/stdc++.h"

typedef long long ll;





void run() {
    string mode = Arg("mode", "none");
    int maxNM = Arg("maxNM", 100000);
    int maxK = Arg("maxK", 100000);
	int minK = Arg("minK", 1);


	int n = Int(1, maxNM);
	Space();
	int k = Int(minK, maxK);
	Space();
	int m = Int(1, maxNM);
	Endl();

	if (mode == "NisK") assert(n == k);


	for (int i = 0; i < m; i++){
		char c = Char();
		Space();
		int x = Int(1,n);
		Endl();

		assert(c == 'C' || c == 'O');
	}

    Eof();
}
