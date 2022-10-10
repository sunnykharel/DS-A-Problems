class Solution {
    public int[][] merge(int[][] intervals) {
        // [1,3], [2,6], [8, 10], [15, 8]
            
        // go linearly right  until you cannot merge any further
        
        Arrays.sort(intervals, (a,b)->a[0]-b[0]);
        if ( intervals.length == 0 || intervals.length == 1 )
            return intervals;
        
        int start = 0;
        int i = 1;
        List<int[]> merged = new LinkedList<>();
        
        while ( i < intervals.length ){
            if (intervals[i-1][1] < intervals[i][0]){
                merged.add(_merge(intervals[start], intervals[i-1]));
                start=i;
            }
            intervals[i][1] = Math.max(intervals[i][1], intervals[i-1][1]);
            i+=1;
        }
        
        merged.add(_merge(intervals[start], intervals[i-1]));
        
        return merged.toArray(new int[merged.size()][]);
    }
    
    public int[] _merge(int[] curr, int[] prev){
        int start = Math.min(curr[0], prev[0]);
        int end = Math.max(curr[1], prev[1]);
        int[] merge = {start, end};
        return merge;
    }
    
}