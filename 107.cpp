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
    vector<vector<int> > levelOrderBottom(TreeNode *root) {
        int depth = TreeDepth(root);
        vector<vector<int> > lot(depth);
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
            lot[depth - level -1].push_back(node->val);
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