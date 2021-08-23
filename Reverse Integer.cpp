class Solution {
public:
    int reverse(int x) {
        long long a=0;
        int count = 0;
        int x1=x;
        while(x1!=0)
        {
            x1/=10;
            count++;
        }
        for(int i=count-1; i>=0; i--){
            a = a + x%10*pow(10,i);
            x/=10;
        }
        return (a>INT_MAX||a<INT_MIN)?0:a;
    }
};
