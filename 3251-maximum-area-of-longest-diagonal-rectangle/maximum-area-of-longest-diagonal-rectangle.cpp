class Solution {
public:
    int areaOfMaxDiagonal(vector<vector<int>>& dimensions) {
        int max_diag = 0;
        int max_area = 0;
        for (auto dimen : dimensions) {
            int diag = dimen[0]*dimen[0] + dimen[1]*dimen[1];
            int area = dimen[0] * dimen[1];
            if (diag > max_diag) {
                max_diag = diag;
                max_area = area;
            } 
            else if (diag == max_diag) {
                max_area = max(max_area, area); 
            }
        }
        return max_area;
    }
};