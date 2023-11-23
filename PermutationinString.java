class Solution {
    public boolean checkInclusion(String s1, String s2) {
        if(s1.length() > s2.length()){
            return false;
        }
        int[] s1arr = new int[26];
        int[] s2arr = new int[26];
        for(int i = 0; i < s1.length(); i++){
            s1arr[s1.charAt(i)-'a']++;
            s2arr[s2.charAt(i)-'a']++;
        }
        int left = 0;
        for(int right = s1.length(); right < s2.length(); right++){
            if(checkEqual(s1arr, s2arr)){
                return true;
            }
            s2arr[s2.charAt(right)-'a']++;
            s2arr[s2.charAt(left)-'a']--;
            left++;
        }
        return checkEqual(s1arr, s2arr);
    }
    public boolean checkEqual(int[] s1arr, int[] s2arr){
        for(int i = 0; i < 26; i++){
            if(s1arr[i] != s2arr[i]){
                return false;
            }
        }
        return true;
    }
}