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
    int maxDepth(TreeNode *root) {
        if (root == NULL)  
            return 0;  
  
        int nLeftDepth = maxDepth(root->left);  
        int nRightDepth = maxDepth(root->right);  
  
        return (nLeftDepth>nRightDepth)?(nLeftDepth+1):(nRightDepth+1); 
    }
};