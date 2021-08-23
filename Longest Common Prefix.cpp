class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        int mark = 99999;
        int countt = 0;
        if(strs.size()==1){
            return strs[0];
        }
        for(int i=0; i<strs.size(); i++){
            if(strs[i].length()<mark){
                countt = i;
                mark  = strs[i].length();
            }
        }
        string s ="";

        char temp;
        int flag = 0;
        for(int i=0; i<mark; i++){
            for(int j=1; j<strs.size(); j++){
                if(strs[0][i] == strs[j][i]){
                    temp = strs[0][i];
                    flag = 0;
                }
                else{
                    flag = 1;
                    break;
                }
            }
            if(flag == 0){
                s += temp;
            }
            else{
                return s;
            }
        }
        return s;
    }
};
