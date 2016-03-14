class Solution {
public:
    string countAndSay(int n) {
        if(n == 1)
            return "1";
        string str = "1";
        for(int i=1;i<n;i++){
            int count = 1;
            char begin = str[0];
            string temp = "";
            for(int j=1;j<str.size();j++){
                if(str[j] == begin)
                    count++;
                else{
                    temp = temp + (char)(count + '0') + begin;
                    begin = str[j];
                    count = 1;
                }
            }
            temp = temp + (char)(count + '0') + begin;
            str = temp;
        }
        return str;
    }
};