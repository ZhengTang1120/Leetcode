class Solution:
    # @param {string} str
    # @return {integer}
    def myAtoi(self, str):
        numberStr = re.findall('^([\+\-]?0*\d+)\D*', str.strip())

        if numberStr:
            number = int(numberStr[0])
            MAX_INT = 2147483647
            MIN_INT = -2147483648
            if number < MIN_INT:
                return MIN_INT
            elif number > MAX_INT:
                return MAX_INT
            else:
                return number
        else:
            return 0
        