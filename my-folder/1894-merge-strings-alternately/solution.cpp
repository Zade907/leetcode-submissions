class Solution {
public:
    string mergeAlternately(string word1, string word2) {
        string string3 = "";
        int i = 0;
        while(i < word1.length() || i < word2.length()){
            if(i < word1.length()){
                string3 += word1[i];
                }
            if(i < word2.length()){
                string3 += word2[i];
                }
            i++;
        }
        return string3;
    }
};
