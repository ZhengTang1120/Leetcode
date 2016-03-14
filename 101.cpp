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
    string lstr;
    string rstr;
    void leftOrder(TreeNode *T){
	    if(T != NULL){
	        stringstream ss;
            ss<<T->val; 
            string s1 = ss.str();
    		lstr = lstr + s1;
		    leftOrder(T->left);
		    leftOrder(T->right);
    	}
    	else
    	    lstr = lstr + "#";
    }
   void rightOrder(TreeNode *T){
	    if(T != NULL){
	        stringstream ss;
            ss<<T->val; 
            string s1 = ss.str();
    		rstr = rstr + s1;
		    rightOrder(T->right);
		    rightOrder(T->left);
    	}
    	else
    	    rstr = rstr + "#";
    }
    bool isSymmetric(TreeNode *root) {
        if(root == NULL)
            return true;
        else{
            leftOrder(root->left);
            rightOrder(root->right);
            if(string(lstr) == string(rstr))
                return true;
            else
                return false;
        }
    }
};