class Solution {
public:
    vector<int> getRow(int rowIndex) {
        vector<int> pascal(rowIndex+1);
        for(int i = 0;i<=rowIndex/2;i++)
            pascal[rowIndex-i] = pascal[i] = combination(i,rowIndex);
        return pascal;
    }
    int combination(int r,int n){
        if(r == 0 || r == n)
            return 1;
         long ret = 1;
        for( int i = n; i > (n-r); i--){
            ret *= i;
            ret /= (n - i + 1);
        }
        return (int)ret;
    }
};