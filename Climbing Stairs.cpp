class Solution {
public:
    int climbStairs(int n) {
        int temp1=0 , temp2 = 0;
        if(n==0){
            return 0;
        }
        if(n==1){
            return 1;
        }
        if(n==2){
            return 2;
        }
        temp1 = 2;
        temp2 = 1;
        int t=0;
        for(int i=3; i<=n; i++){
            t = temp1;
            temp1 = temp1 +temp2;
            temp2 = t;
        }
        return temp1;
    }
};
