class Solution {
public:
    vector<vector<int> > generate(int numRows) {
        vector<vector<int> > pascal(numRows);
        for(int k = 0;k<numRows;k++){
            pascal[k].resize(k+1);
            pascal[k][0] = 1;
            pascal[k][k] = 1;
        }
        for(int i = 2;i<numRows;i++){
            for(int j = 1;j<i;j++){
                pascal[i][j] = pascal[i-1][j-1]+pascal[i-1][j];
            }
        }
        return pascal;
    }
};