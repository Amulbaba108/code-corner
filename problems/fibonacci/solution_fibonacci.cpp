#include <bits/stdc++.h>

using namespace std;

long long fibonacciSeries(int num) {
    if (num == 0) return 0;
    if (num == 1) return 1;

    long long back2 = 0;
    long long back1 = 1;
    long long current = 0;

    for (int i = 2; i <= num; i++) {
        current = back1 + back2;
        back2 = back1;
        back1 = current;
    }
    return current;
}

int main() {
    int num;
    if (cin >> num) {
        cout << fibonacciSeries(num) << endl;
    }
    return 0;
}
