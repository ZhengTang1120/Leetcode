class Solution {
public:
    int compareVersion(string version1, string version2) {
        string[] v1 = version1.split("\\.");  
        string[] v2 = version2.split("\\.");
        int size;
        int result;
        if(v1.size() > v2.size()){
            size = result2.size();
            result = 1;
        }else if(v1.size() < v2.size()){
            size = result1.size();
            result = -1;
        }else{
            size = result1.size();
            result = 0;
        }
        for(int i = 0;i<size;i++){
            if(v1[i]>v2[i])
                result = 1;
            else if(v1[i]<v2[i])
                result = -1;
        }
        return result;
    }
};