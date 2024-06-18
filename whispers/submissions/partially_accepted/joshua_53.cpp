#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
#define int ll
const int inf = int(1e18);

typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int, int> p2;

#define rep(i, high) for (int i = 0; i < high; i++)
#define repp(i, low, high) for (int i = low; i < high; i++)
#define repe(i, container) for (auto& i : container)
#define sz(container) ((int)container.size())
#define all(x) begin(x),end(x)
#define ceildiv(x,y) (((x) + (y) - 1) / (y))

inline void fast() { ios::sync_with_stdio(false); cin.tie(NULL); cout.tie(NULL); }

auto Start = chrono::high_resolution_clock::now();
void resettimer() { Start = chrono::high_resolution_clock::now(); }
int elapsedmillis() { return chrono::duration_cast<chrono::milliseconds>(chrono::high_resolution_clock::now() - Start).count(); }

#if _LOCAL
#define __builtin_clz __lzcnt
#define assert(x) if (!(x)) __debugbreak()
#endif

bool dfs(int u, vi& vis, vi& btoa, vvi& edges)
{
	if (btoa[u] == -1) return 1;
	if (vis[u]) return 0;
	vis[u] = 1;

	int a = btoa[u];
	repe(e, edges[a])
	{
		if (dfs(e,vis,btoa,edges))
		{
			btoa[e] = a;
			return 1;
		}
	}
	return 0;
}

vi getviable(int n, int m, vvi edges, int a, bool up)
{
	vi ret(n * m);
	
	vi good(n);
	int start = up ? 0 : n * (m - 1);
	good[a-start] = 1;

	rep(i, m - 1)
	{
		vvi localgraph(n);
		int nextg = start + (up ? n : -n);

		rep(j, n) if (good[j]) ret[start + j] = 1;

		rep(j, n)
		{
			repe(e, edges[start + j]) localgraph[j].push_back(e - nextg);
		}

		vi nextgood(n);

		vi btoa(n, -1);
		vi vis(n);

		int nummatched = 0;
		rep(j, n)
		{
			rep(k, n)vis[k] = 0;
			repe(e, localgraph[j])
			{
				if (dfs(e, vis, btoa, localgraph))
				{
					btoa[e] = j;
					nummatched++;
					break;
				}
			}
		}
		assert(nummatched == n);
		rep(j, n)
		{
			if (btoa[j] != -1)
			{
				if (good[btoa[j]]) nextgood[j] = 1;
			}
		}

		rep(j, n)
		{
			if (!good[j]) continue;

			int works = -1;
			rep(k, n) if (btoa[k] == j)btoa[k] = -1, works = k;
			//if (works == -1) continue;
			repe(e, localgraph[j])
			{
				if (nextgood[e])
				{
					continue;
				}
				rep(k, n)vis[k] = 0;
				if (dfs(e,vis,btoa, localgraph))
				{
					works = e;
					nextgood[e] = 1;
					btoa[e] = -1;

				}
			}
			assert(works != -1);
			rep(k, n)vis[k] = 0;
			assert(dfs(works, vis, btoa, localgraph));
		}
		good = nextgood;
		start = nextg;
	}
	rep(j, n) if (good[j]) ret[start + j] = 1;

	return ret;
}

signed main()
{
	fast();

	int n, m, a, b;
	cin >> n >> m >> a >> b;
	vector<p2> edgelist;
	vvi graphup(n * (m-1));
	vvi graphdown(n * m);
	rep(i, n)
	{
		rep(j, m-1)
		{
			int deg;
			cin >> deg;
			rep(k, deg)
			{
				int b;
				cin >> b;
				graphup[j + i * (m-1)].push_back(b);
				graphdown[b].push_back(j + i * (m - 1));
				edgelist.emplace_back(j + i*m, b);
			}
		}
	}

	vi l = getviable(n, m, graphup, a, 1);
	vi r = getviable(n, m, graphdown, b, 0);

	int ans = 0;
	rep(i, sz(l)) ans += l[i] && r[i];
	cout << ans << "\n";
	rep(i, sz(l))
	{
		if (l[i] && r[i]) cout << i << "\n";
	}

	return 0;
}
