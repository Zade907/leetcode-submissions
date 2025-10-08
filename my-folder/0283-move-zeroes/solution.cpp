class Solution {
public:
    void moveZeroes(vector<int>& nums) {
        int n = 0;
        for(int i = 0; i < nums.size(); i ++){
            if(nums[i]==0){
                nums.erase(nums.begin()+i);
                n++;
                i--;
            }
        }
        for(int j = 0;j<n;j++){
            nums.push_back(0);
        }
    }
};
