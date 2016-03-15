class Solution {
public:
    int majorityElement(vector<int> &num) {
        sort( num.begin() , num.end() );
        int maj = num[0];
        int count = 1;
        for(int i=1;i<num.size();i++){
            if(maj == num[i]){
                count++;
                if(count > num.size()/2)
                    break;
            }
            else{
                maj = num[i];
                count = 1;
            }
        }
        return maj;
    }
};