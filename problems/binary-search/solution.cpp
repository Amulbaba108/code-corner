#include <iostream>
#include <vector>
using namespace std;

int main()
{
    // input target
    int target;
    cin >> target;

    // make a vector
    vector<int> nums;
    int num;

    // input vector
    while (cin >> num)
    {
        nums.push_back(num);
    }

    // set high and low
    int lb = 0, hb = nums.size() - 1;
    int ans = -1;

    while (lb <= hb)
    {
        int mid = (lb + hb) / 2;

        if (nums[mid] == target)
        {
            ans = mid;
            break;
        }

        if (nums[mid] < target)
        {
            lb = mid + 1;
        }
        else
        {
            hb = mid - 1;
        }
    }

    // output
    cout << ans << endl;

    return 0;
}