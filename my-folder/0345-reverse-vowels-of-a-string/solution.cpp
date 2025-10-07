#include <stack>
class Solution {
public:
    string reverseVowels(string s) {
        string reverse;
        stack<char> vowels;
        for(int i = 0; i< s.size(); i++){
            char ch = s[i];
            if(ch=='a'||ch == 'A'||ch=='e'||ch== 'E'|| ch == 'i'||ch == 'I'||ch == 'o'||ch == 'O'||ch== 'u'||ch == 'U'){
                vowels.push(ch);
            }
        }
        for(int i = 0; i< s.size(); i++){
            char ch = s[i];
            if(ch =='a'||ch == 'A'||ch=='e'||ch== 'E'|| ch == 'i'||ch == 'I'||ch == 'o'||ch == 'O'||ch== 'u'||ch == 'U'){
                reverse += vowels.top();
                vowels.pop();
            }
            else{
                reverse += ch;
            }
    }
    return reverse;
    }
};
