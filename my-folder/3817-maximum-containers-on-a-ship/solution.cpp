class Solution {
public:
    int maxContainers(int n, int w, int maxWeight) {
        if(n*n<maxWeight/w){
            return n*n;
        }
        if(n*n>=maxWeight/w){
            return maxWeight/w;
        }
        return 0;
    }
};
