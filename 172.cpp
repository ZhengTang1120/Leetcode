class Solution {
public:
    int trailingZeroes(int n) {
        int zeroes = 0;
        while(n){
            zeroes = zeroes + n/5;
            n = n/5;
        }
        return zeroes;
    }
};