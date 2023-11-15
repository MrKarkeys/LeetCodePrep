class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> values = new Stack<>();
        for(int i = 0; i < tokens.length; i++){
            int val1 = 0;
            int val2 = 0;
            if(tokens[i].equals("/")){
                val1 = values.pop();
                val2 = values.pop();
                values.push(val2/val1);
            }
            else if(tokens[i].equals("-")){
                val1 = values.pop();
                val2 = values.pop();
                values.push(val2-val1);
            }
            else if(tokens[i].equals("+")){
                val1 = values.pop();
                val2 = values.pop();
                values.push(val2+val1);
            }
            else if(tokens[i].equals("*")){
                val1 = values.pop();
                val2 = values.pop();
                values.push(val2*val1);
            }
            else{
                int val = Integer.valueOf(tokens[i]); 
                values.push(val);
            }
        }
        return values.pop();
    }
}