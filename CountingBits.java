class Solution {
    public int[] countBits(int n) {
        int[] values = new int[n+1];
        int convert = Integer.bitCount(n);
        int i = n;
        while(n >= 0){
            int count = 0;
            values[n] = convert;
            n--;
            convert = Integer.bitCount(n);
        }
        return values;
    }
}