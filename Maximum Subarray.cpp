class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int temp = 0;
        int ans = -INT_MAX;
        for(int i=0; i<nums.size(); i++){
            temp = 0;
            for(int j=i; j<nums.size(); j++){
                //cout << nums[i] << "  +  " << nums[j] << endl;
                temp += nums[j];
                if(temp>ans){
                    ans = temp;
                }
            }
        }
        return ans;
    }
};
