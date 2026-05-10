class Solution {
public:
    long long minArraySum(vector<int>& nums) {
        unordered_set<int> s(nums.begin(), nums.end());

        long long ans = 0;

        for (int x : nums) {
            int best = x;

            for (int i = 1; 1LL * i * i <= x; i++) {
                if (x % i == 0) {

                    if (s.count(i)) {
                        best = min(best, i);
                    }

                    int other = x / i;

                    if (s.count(other)) {
                        best = min(best, other);
                    }
                }
            }

            ans += best;
        }

        return ans;
    }
};
