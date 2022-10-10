class MyQueue {
    private Stack<Integer> stack_hold;
    private Stack<Integer> stack_pop; 
    
    
    /** Initialize your data structure here. */
    public MyQueue() {
        stack_hold = new Stack<>();
        stack_pop = new Stack<>();
    }
    
    /** Push element x to the back of queue. */
    public void push(int x) {
        stack_hold.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if (stack_pop.empty()){
            while(!stack_hold.empty()){
                stack_pop.push(stack_hold.pop());
            }
        }
        return stack_pop.pop();
    }
    
    /** Get the front element. */
    public int peek() {
        if (stack_pop.empty()){
            while(!stack_hold.empty()){
                stack_pop.push(stack_hold.pop());
            }
        }
        return stack_pop.peek();
    }
    
    /** Returns whether the queue is empty. */
    public boolean empty() {
        return stack_hold.empty() && stack_pop.empty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */