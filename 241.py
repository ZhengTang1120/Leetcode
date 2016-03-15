class Solution:
    # @param {string} input
    # @return {integer[]}
    def diffWaysToCompute(self, input):
        result = []
        for i in range(0,len(input)):
            c = input[i]
            if(c == '+' or c == '-' or c == '*'):
                left = self.diffWaysToCompute(input[0:i])
                right = self.diffWaysToCompute(input[i+1:])
                for j in range(0,len(left)):
                    for k in range(0,len(right)):
                        if c == '+':
                            result.append(left[j]+right[k])
                        if c == '-':
                            result.append(left[j]-right[k])
                        if c == '*':
                            result.append(left[j]*right[k])
        if len(result)==0:
            result.append(int(input))
        return result