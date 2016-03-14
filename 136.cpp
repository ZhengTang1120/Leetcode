class Solution {
public:
    int singleNumber(int A[], int n) {
        if(A == NULL || n == 0){
            return 0;
        }
        int result = A[0];
        
        for(int i = 1; i < n; i++){
            result = result ^ A[i];
        }
        return result;
    }
};