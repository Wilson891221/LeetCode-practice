class Solution {
public:
    int removeDuplicates(vector<int>& nums) {

        if(nums.size()==0){
            return 0;
        }
        int j=1, i=0;
        for(i=0; i<nums.size()-1; i++){
            if(nums[i]!=nums[i+1]){
                nums[j] = nums[i+1];
                j++;
            }
        }
        return j;

    }
};
