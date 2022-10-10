class Solution {
    public int[] sortArray(int[] nums) {
        mergeSort(nums, 0, nums.length-1);
        return nums;
    }
    public void mergeSort(int[] nums, int l, int r){
        if(l<r){
            int m = (l+r)/2;
            mergeSort(nums, l, m);
            mergeSort(nums, m+1, r);
            merge(nums, l, m, r);
        }
    }
    public void merge(int[] nums, int l, int m, int r){
        int[] left= new int[m-l+1];
        for(int i = 0; i<left.length; i++){
            left[i]=nums[l+i];
        }
        int[] right = new int[r-m];
        for(int i = 0; i<right.length; i++){
            right[i]=nums[m+1+i];
        }
        int leftIndex = 0;
        int rightIndex = 0;
        int k = l; // the location in the original array that you're modifying
        while(leftIndex<left.length && rightIndex<right.length){
            int leftVal= left[leftIndex];
            int rightVal=right[rightIndex];
            if(leftVal<rightVal){
                nums[k]=leftVal;
                leftIndex++;
            }else{
                nums[k]=rightVal;
                rightIndex++;
            }
            k++;
        }if(leftIndex==left.length){
            for(int i =rightIndex; i< right.length; i++){
                nums[k]=right[i];
                k++;
            }
        }
        else{
            for(int i =leftIndex; i< left.length; i++){
                nums[k]=left[i];
                k++;
            }
        }
        
    }
}