class Solution {
public:
    int lengthOfLastWord(string s) {
        int ans = 0;
        int temp = 0;
        for(int i=s.length()-1; i>=0; i--){
            if(s[i]!=' '){
                temp = i;
                break;
            }
        }
        for(int i = temp; i>=0; i--){
            if(s[i]!=' '){
                ans++;
            }
            else{
                break;
            }
        }
        return ans;
    }
};
