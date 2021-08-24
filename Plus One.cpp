class Solution {
public:
    vector<int> plusOne(vector<int>& digits) {
        vector<int> temp;
        if(digits.size()==1){
            digits[0] +=1;
            if(digits[0]==10){
                temp.push_back(1);
                temp.push_back(0);
                return temp;
            }
            else{
                return digits;
            }

        }
        digits[digits.size()-1] +=1;
        for(int i=digits.size()-1; i>0; i--){
            if(digits[i]>=10){
                digits[i-1] +=1;
                digits[i] = 0;
                if(digits[0]==10){
                    temp.push_back(1);
                    temp.push_back(0);
                    for(int i=1; i<digits.size(); i++){
                        temp.push_back(digits[i]);
                    }
                    return temp;
                }
            }
            else{
                break;
            }
        }
        return digits;
    }

};
