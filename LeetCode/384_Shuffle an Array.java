class Solution {

    private int[] nums;
    private Random random;
    
    public Solution(int[] nums) {
        this.nums = nums;
        random = new Random();
    }
    
    /** Resets the array to its original configuration and return it. */
    public int[] reset() {
        return nums;
    }
    
    /** Returns a random shuffling of the array. */
    public int[] shuffle() {
        int[] copyiedArray = nums.clone(); //nums 배열 깊은 복사
        for (int j=1; j<copyiedArray.length; j++){
            int i = random.nextInt(j + 1); //0~j까지 난수 생성
            swap(copyiedArray,i,j); //i, j 위치 요소 swap
        }
        
        return copyiedArray;
    }
    

    private void swap(int[] nums, int i, int j) {
        if (i == j) {
            return;
        }
        int tmp = nums[i];
        nums[i] = nums[j];
        nums[j] = tmp;
    }
}
