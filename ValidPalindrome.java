import java.util.*;
class Solution {
    public boolean isPalindrome(String s) {
        if(s.isEmpty()){
            return true;
        }
        s = s.toLowerCase();
        char values[] = s.toCharArray();
        int left = 0;
        int right = values.length-1;
        while(left <= right){
            if(!Character.isLetterOrDigit(values[left])){
                left++;
            }
            else if(!Character.isLetterOrDigit(values[right])){
                right--;
            }
            else{
                if(values[left] != values[right]){
                    return false;
                }
                left++;
                right--;
            }  
        }
        return true;
    }
}