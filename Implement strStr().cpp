class Solution
{
public:
    int strStr(string haystack, string needle){
        int temp = 0;
        int count = 0;
        if (haystack == "" && needle == ""){
            return 0;
        }
        if (haystack != "" && needle == ""){
            return 0;
        }
        int mark = 0;
        for(int i=0; i<haystack.size(); i++){
            if(needle[temp]==haystack[i]){
                temp++;
                count++;
                if(count==needle.size()){
                    //cout << "break" << endl;
                    mark = i;
                    break;
                }
            }
            else{
                //cout << "  else" << endl;
                i = i-count;
                temp=0;
                count = 0;
            }

        }
        if(count == needle.size()){
            return mark-needle.size()+1;
        }
        else{
            return -1;
        }
    }
};
