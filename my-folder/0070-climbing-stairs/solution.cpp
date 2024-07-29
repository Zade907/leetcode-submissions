class Solution {
public:
    int climbStairs(int n) {
        int a = 0,b = 1,temp;
        for(int i =0;i<n;i++){
            temp = b;
            b += a; 
            a = temp;}
        return b; 
    }
};
