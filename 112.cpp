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
    bool dfs(TreeNode *root, int sum, int cursum){
        if(root != NULL){
            if(root->left == NULL && root->right == NULL)
                return (cursum + root->val == sum);
            else{
                return dfs(root->left,sum,cursum+root->val) || dfs(root->right,sum,cursum+root->val);
            }
        }else
            return false;
    }
    bool hasPathSum(TreeNode *root, int sum) {
        return dfs(root,sum,0);
    }
};