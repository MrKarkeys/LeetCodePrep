class Solution {
    public boolean isValid(String s) {
        Stack<Character> string = new Stack<Character>();
        char[] vals = s.toCharArray();
        if(vals.length % 2 != 0){
            return false;
        }
        for(int i = 0; i < vals.length; i++){
            if(vals[i] == '('){
                string.push(')');
            }
            else if(vals[i] == '{'){
                string.push('}');
            }
            else if(vals[i] == '['){
                string.push(']');
            }
            else if(string.isEmpty() || string.pop() != vals[i]){
                return false;
            }
        }
        if(string.isEmpty()){
            return true;
        }
        return false;
    }
}