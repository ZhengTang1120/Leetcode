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
    int minDepth(TreeNode *root) {
        if(root == NULL)
            return 0;
        queue<TreeNode *> nodeQueue;  
        nodeQueue.push(root);
        TreeNode *node;
        queue<int> levelQueue;
        int level = 1;
        levelQueue.push(level);
        while(!nodeQueue.empty()){
            node = nodeQueue.front();
            nodeQueue.pop();
            level = levelQueue.front();
            levelQueue.pop();
            if(node->left == NULL && node->right == NULL)
                return level;
            if(node->left){
                nodeQueue.push(node->left); 
                levelQueue.push(level+1);
            }
            if(node->right){
                nodeQueue.push(node->right);  
                levelQueue.push(level+1);
            }
            level++;
        }
    }
};