#include <bits/stdc++.h>
using namespace std;

//function to remove spaces and turn string in lowercase
string clean(string s){
    string str = "";
    for(char c : s){
        if(isalnum(c)){
            str += tolower(c);
        }
    }
    return str;
}

bool isAnagram(string s, string t) {
    //return false if lengths are different
    if (s.length() != t.length()) {
        return false;
    }
    
    //sort both strings
    sort(s.begin(), s.end());
    sort(t.begin(), t.end());

    //if sorted strings are same return true else return false
    return s == t;
}

int main() {
    //read input
    string combined, s, t;

    //extract the 2 strings from input
    getline(cin, combined);
    for(int i = 0; i < combined.length(); i++){
        if(combined[i] == ','){
            s = combined.substr(0, i);
            t = combined.substr(i + 1);
            break;
        }
    }

    //print true/false using above anagram function on cleaned strings
    if(isAnagram(clean(s), clean(t))){
        cout << "true";
    }
    else{
        cout << "false";
    }
    return 0;
}