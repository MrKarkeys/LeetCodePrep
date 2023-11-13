class MinStack {
    Stack<Integer> values;
    public MinStack() {
        values = new Stack<Integer>();
    }
    
    public void push(int val) {
        values.push(val);
    }
    
    public void pop() {
        values.pop();
    }
    
    public int top() {
        return values.peek();
    }
    
    public int getMin() {
        int min = 0;
        ArrayList<Integer> list = new ArrayList<Integer>();
        int j = 0;
        while(!values.isEmpty()){
            int popped = values.pop();
            if(j == 0){
                min = popped;
            }
            list.add(popped);
            if(popped < min){
                min = popped;
            }
            j++;
        }

        for(int i = list.size()-1; i >= 0; i--){
            values.push(list.get(i));
        }
        return min;
    }
}

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack obj = new MinStack();
 * obj.push(val);
 * obj.pop();
 * int param_3 = obj.top();
 * int param_4 = obj.getMin();
 */