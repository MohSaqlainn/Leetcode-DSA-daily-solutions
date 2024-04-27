class Solution {
public:
    bool searchMatrix(vector<vector<int>>& mx, int target) {
        int m = mx.size();
        int n = mx[0].size();
        int left = 0, right = m*n - 1;

        while (left<=right) {
            int mid = left + (right - left)/2;
            int mid_val = mx[mid/n][mid%n];

            if (mid_val == target) {
                return true;
            } else if (mid_val < target) {
                left = mid+1;
            } else {
                right = mid-1;
            }
        }

        return false;
    }
};