class Solution {
    public String removeDuplicates(String s) {
        Stack<Character> stack = new Stack<>();
        Stack<Integer> stackIndicies = new Stack<>();
        String[] string = new String[s.length()];
        for (int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if (!stack.empty() && c == stack.peek()) {
                stack.pop();
                int a = i;
                int b = stackIndicies.pop();
                string[a] = ""; string[b] = "";
            } else {
                string[i] = "" + s.charAt(i);
                stack.add(s.charAt(i));
                stackIndicies.add(i);
            }
        }
        return String.join("", string);
    }
}