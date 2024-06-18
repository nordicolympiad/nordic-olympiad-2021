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

vi is_bridge;
vi allowed_bridge;
vi vis_e;
vector<vector<p2>> edges;
vi vis;


bool dfs2(int a, int b)
{
	if (a == b) return 1;
	if (vis[a]) return 0;
	vis[a] = 1;

	repe(e, edges[a])
	{
		if (dfs2(e.first,b))
		{
			if (is_bridge[e.second]) allowed_bridge[e.second] = 1;
			return 1;
		}
	}

	return 0;
}

void dfs3(int a)
{
	if (vis[a]) return;
	vis[a] = 1;

	repe(e, edges[a])
	{
		if (is_bridge[e.second] && !allowed_bridge[e.second]) continue;
		dfs3(e.first);
	}
}

signed main()
{
	fast();

	int n, m, a, b;
	cin >> n >> m >> a >> b;
	vis.resize(n);
	edges.resize(n);
	is_bridge.resize(m,1);
	allowed_bridge.resize(m);
	vis_e.resize(m);
	vector<p2> edge_list;
	rep(i, m)
	{
		int a, b;
		cin >> a >> b;
		edges[a].emplace_back(b,i);
		edges[b].emplace_back(a,i);
		edge_list.emplace_back(a, b);
	}
	

	vi vis1[2];
	vis1[0] = vi(n);
	vis1[1] = vi(n);
	int version = 10;
	rep(i, m)
	{
		version++;

		queue<p2> q;
		q.emplace(edge_list[i].first, 0);
		q.emplace(edge_list[i].second, 1);
		while (q.size())
		{
			int u, v;
			tie(u, v) = q.front();
			q.pop();

			if (vis1[v][u]==version) continue;
			vis1[v][u] = version;
			
			if (vis1[!v][u]==version)
			{
				is_bridge[i] = 0;
				break;
			}
			repe(e, edges[u]) if (e.second!=i)q.emplace(e.first, v);
		}
	}

	rep(i, n) vis[i] = 0;
	dfs2(a, b);
	rep(i, n) vis[i] = 0;
	dfs3(a);

	int ans = 0;
	rep(i, n) ans += vis[i] == 0;
	cout << ans << "\n";
	rep(i, n) if (!vis[i]) cout << i << "\n";

	return 0;
}
