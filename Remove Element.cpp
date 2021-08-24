class Solution
{
public:
    int removeElement(vector<int> &nums, int val)
    {
        int count = 0;
        if(nums.size()==0){
            return 0;
        }
        for (int i = 0; i < nums.size(); i++){
            if (nums[i] == val){
               nums[i] = -1;
               count++;
            }
        }
        for (int i = 0; i < nums.size(); i++){
            for(int j= nums.size()-1;j>i; j--){
                if(nums[i]==-1){
                    if(nums[j]!=-1){
                        swap(nums[i],nums[j]);
                        break;
                    }
                }
            }
        }
        return nums.size()-count;
    }
};
