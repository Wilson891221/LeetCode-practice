class Solution {
public:
    bool isPalindrome(int x) {
        stringstream s;
        string a;
        s << x;
        s >> a;
        int j = a.length()-1;
        int count = 1;
        for(int i=0; i<a.length()-1; i++){
            //cout << "this is i:  " << i << endl;
            //cout << "this is j:  " << j << endl;
            if (a[i]!=a[j]){
                count =0;
                break;
            }
            else{
                j--;
            }
        }
        if(count == 0){
            //cout << "false" << endl;
            return 0;
        }
        else{
            //cout << "true" << endl;
            return 1;
        }

    }
};
