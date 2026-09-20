#include <iostream>

bool isPrime(long long n) {
    if (n < 2) return false;
    for (long long i = 2; i * i < n; i++) {
        if (n % i == 0) return false;
    }
    return true;
}

int main() {
    long long n;
    std::cin >> n;
    std::cout << (isPrime(n) ? "prime" : "not prime") << "\n";
}
