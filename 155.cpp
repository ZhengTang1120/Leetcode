class MinStack {
public:
    stack<int> st;
    stack<int> min;
    void push(int x) {
        st.push(x);
        if(min.empty() || (!min.empty() && x <= min.top()))
            min.push(x);
    }

    void pop() {
        if(st.top() == min.top())
            min.pop();
        st.pop();
    }

    int top() {
        return st.top();
    }

    int getMin() {
        return min.top();
    }
};