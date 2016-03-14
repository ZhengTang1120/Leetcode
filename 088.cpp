class Solution {
public:
    void merge(int A[], int m, int B[], int n) {
        int pointA=0,pointB=0,pointC =0;
        int C[m+n];
        while(pointA<m && pointB<n){
            if(A[pointA]<B[pointB]){
                C[pointC] = A[pointA];
                pointA++;
                pointC++;
            }else{
                C[pointC] = B[pointB];
                pointB++;
                pointC++;
            }
        }
        if(pointA < m){
            for(int i = pointC;i<m+n;i++){
                C[i] = A[pointA];
                pointA++;
            }
        }else{
            for(int i = pointC;i<m+n;i++){
                C[i] = B[pointB];
                pointB++;
            }
        }
        for(int j = 0;j<m+n;j++){
            A[j] = C[j];
        }
    }
};