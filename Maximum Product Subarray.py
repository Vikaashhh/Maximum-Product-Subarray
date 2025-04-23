#User function Template for python3
class Solution:

    # Function to find maximum product subarray
    def maxProduct(self, arr):
        if not arr:
            return 0

        # Initialize karte hain:
        max_product = curr_max = curr_min = arr[0]

        for i in range(1, len(arr)):
            num = arr[i]

            # Agar number negative hai, toh max aur min ko swap kar do
            if num < 0:
                curr_max, curr_min = curr_min, curr_max

            # Yeh teen cheezein update karo:
            curr_max = max(num, curr_max * num)
            curr_min = min(num, curr_min * num)

            # Har step pe max_product ko update karte chalo
            max_product = max(max_product, curr_max)

        return max_product
    

if __name__ == "__main__":
    arr = list(map(int, input("Enter array elements: ").split()))
    sol = Solution()
    print("Maximum product subarray is:", sol.maxProduct(arr))