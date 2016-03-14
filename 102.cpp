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
    vector<vector<int> > levelOrder(TreeNode *root) {
        vector<vector<int> > lot(0);
        if(root == NULL)
            return lot;
        queue<TreeNode *> nodeQueue;  
        nodeQueue.push(root);
        TreeNode *node;
        queue<int> levelQueue;
        int level = 0;
        levelQueue.push(level);
        while(!nodeQueue.empty()){
            node = nodeQueue.front();
            nodeQueue.pop();
            level = levelQueue.front();
            levelQueue.pop();
            lot.resize(level+1);
            lot[level].push_back(node->val);
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
        return lot;
    }
};