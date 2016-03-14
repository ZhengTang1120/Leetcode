class Solution {
public:
    vector<int> plusOne(vector<int> &digits) {
        int len = digits.size();
        for(int i=0;i<len;i++){
            if(digits[len-i-1]+1<10){
                digits[len-i-1]++;
                return digits;
            }else{
                digits[len-i-1] = 0;
            }
        }
        digits.resize(len+1);
        digits[0] = 1;
        for(int j=1;j<len+1;j++)
            digits[j] = 0;
        return digits;
    }
};