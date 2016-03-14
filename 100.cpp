/**
 * Definition for binary tree
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */
class Solution {
public:
    string str;
    void leftOrder(TreeNode *T){
	    if(T != NULL){
	        stringstream ss;
            ss<<T->val; 
            string s1 = ss.str();
    		str = str + s1;
		    leftOrder(T->left);
		    leftOrder(T->right);
    	}
    	else
    	    str = str + "#";
    }
    bool isSameTree(TreeNode *p, TreeNode *q) {
        str = "";
        leftOrder(p);
        string pstr = str;
        str = "";
        leftOrder(q);
        string qstr = str;
        if(pstr == qstr)
            return true;
        else
            return false;
    }
};