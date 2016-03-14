class Solution {
public:
    int removeElement(int A[], int n, int elem) {
        int index = n-1;
        int i = 0;
        while(i<=index){
            if(A[i] == elem){
                A[i] = A[index];
                index--;
            }
            else
                i++;
        }
        return i;
    }
};