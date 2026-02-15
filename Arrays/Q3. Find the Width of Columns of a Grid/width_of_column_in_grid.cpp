class Solution {
public:
    vector<int> findColumnWidth(vector<vector<int>>& grid) {
        int m = grid.size(); //no of rows
        int n = grid[0].size(); //no of columns
        vector<int> ans(n);

        for(int i=0; i<n; i++) {
            int maxLen = 0;
            for(int j=0; j<m; j++) {
                string s = to_string(grid[j][i]);
                int len = s.size();
                maxLen = max(maxLen, len);
            }
            ans[i] = maxLen;
        }
        return ans;
    }
};
