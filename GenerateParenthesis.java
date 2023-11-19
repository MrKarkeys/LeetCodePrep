class Solution {
    public List<String> generateParenthesis(int n) {
        List<String> vals = new ArrayList<String>();
        ParenthesisRecurs(0, 0, vals, n, "");
        return vals;
    }

    public void ParenthesisRecurs(int open, int closed, 
    List<String> list, int n, String parenthesis){
        if(open == closed && closed == n){
            list.add(parenthesis);
            return;
        }
        if(open < n){
            ParenthesisRecurs(open+1, closed, list, n, parenthesis + "(");
        }
        if(closed < open){
            ParenthesisRecurs(open, closed+1, list, n, parenthesis + ")");
        }
    }
}