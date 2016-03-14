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
    int TreeDepth(TreeNode* pRoot)  
    {  
        if (pRoot == NULL)  
            return 0;  
  
        int nLeftDepth = TreeDepth(pRoot->left);  
        int nRightDepth = TreeDepth(pRoot->right);  
  
        return (nLeftDepth>nRightDepth)?(nLeftDepth+1):(nRightDepth+1);  
    } 
    bool isBalanced(TreeNode *root) {
        if(root== NULL)  
        return true;  
  
        int nLeftDepth = TreeDepth(root->left);  
        int nRightDepth = TreeDepth(root->right);  
        int diff = nRightDepth-nLeftDepth;  
  
        if (diff>1 || diff<-1)  
            return false;  
  
        return isBalanced(root->left)&&isBalanced(root->right);  
    }
};