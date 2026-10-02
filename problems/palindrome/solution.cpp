#include <bits/stdc++.h>
using namespace std;

int main() {
    string userWord;

    getline(cin, userWord);

    string cleaned = "";

    for (int i = 0 ; i < userWord.length() ; i++) {
        char ch = userWord[i];

        if ((ch >= 'a' && ch <= 'z') || (ch >= '0' && ch <= '9')) {
            cleaned += ch;
        }
        else if (ch >= 'A' && ch <= 'Z') {
            cleaned += (ch + 32);
        }
    }

    bool isPalindrome = true;

    int cleanedLength = cleaned.length();

    for (int i = 0 ; i < cleanedLength/2 ; i++) {
        if (cleaned[i] != cleaned[cleanedLength - 1 - i]) {
            isPalindrome = false;
            break;
        }
    }

    if (isPalindrome) {
        cout << "true" << endl;
    } else {
        cout << "false" << endl;
    }
 
    
    return 0;
}
