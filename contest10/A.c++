#include <bits/stdc++.h>
using namespace std;

using ll = long long;

const int MAXN = 100000;
ll tree[4 * MAXN], lazy[4 * MAXN];

void push(int v) {
    if (lazy[v] != 0) {
        tree[v] += lazy[v];
        lazy[v * 2] += lazy[v];
        lazy[v * 2 + 1] += lazy[v];
        lazy[v] = 0;
    }
}

void update(int v, int tl, int tr, int l, int r, ll val) {
    if (l >= r) return;
    if (l == tl && r == tr) {
        lazy[v] += val;
        return;
    }
    push(v);
    int tm = (tl + tr) / 2;
    update(v * 2, tl, tm, l, min(r, tm), val);
    update(v * 2 + 1, tm, tr, max(l, tm), r, val);
    tree[v] = min(tree[v * 2] + lazy[v * 2],
                  tree[v * 2 + 1] + lazy[v * 2 + 1]);
}

ll query(int v, int tl, int tr, int l, int r) {
    if (l >= r) return LLONG_MAX;
    if (l == tl && r == tr) {
        return tree[v] + lazy[v];
    }
    push(v);
    int tm = (tl + tr) / 2;
    return min(
        query(v * 2, tl, tm, l, min(r, tm)),
        query(v * 2 + 1, tm, tr, max(l, tm), r)
    );
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n, m;
    cin >> n >> m;

    while (m--) {
        int type;
        cin >> type;
        if (type == 1) {
            int l, r;
            ll v;
            cin >> l >> r >> v;
            update(1, 0, n, l, r, v);
        } else {
            int l, r;
            cin >> l >> r;
            cout << query(1, 0, n, l, r) << "\n";
        }
    }
}
