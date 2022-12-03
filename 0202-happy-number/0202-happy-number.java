class Solution {
    public int numberToSumOfSquares(int n){
        double sumOfSquares = 0;
        while (n > 0){
            sumOfSquares += Math.pow((n%10), 2);
            n /= 10;
        }
        return (int) sumOfSquares;
    }
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<Integer>();
        
        while (n != 1){
            if (set.contains(n)){
                return false;
            }
            set.add(n);
            n = numberToSumOfSquares(n);
        }
        return (n==1) ? true: false;
        
    }
}