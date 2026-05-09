class Solution {
    public int[] replaceElements(int[] arr) {
        int max = Integer.MIN_VALUE;
        int left = 0, right = arr.length - 1;
        while (left < arr.length - 1) {
            if (arr[right] > max) max = arr[right];
            if (right == left + 1) {
                arr[left] = max;
                left++;
                right = arr.length - 1;
                max = Integer.MIN_VALUE;
            } else {
                right -= 1;
            }
        }
        arr[arr.length - 1] = -1;
        return arr;
    }
}