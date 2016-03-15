class Solution {
public:
    string convertToTitle(int n) {
        string title = "";
        while(n){
            n--;
            char c = n%26 + 'A';
            title = c + title;
            n = n/26;
        }
        return title;
    }
};