import java.util.*;
class Solution {
    public boolean isAnagram(String s, String t) {
        char[] set1 = s.toCharArray();
        char[] set2 = t.toCharArray();

        Arrays.sort(set1);
        Arrays.sort(set2);

        return(Arrays.equals(set1, set2));
    }
}