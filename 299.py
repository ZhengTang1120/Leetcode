class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        bull = 0
        cow = 0
        d = {}
        for i in xrange(len(secret)):
            try:
                d[secret[i]] += 1
            except KeyError:
                d[secret[i]] = 1
        for i in xrange(len(guess)):
            if guess[i] == secret[i]:
                bull+=1
                d[guess[i]] -= 1
        for i in xrange(len(guess)):
            if guess[i] != secret[i] and guess[i] in secret and d[guess[i]] != 0:
                cow+=1
                d[guess[i]] -= 1
        return str(bull)+"A"+str(cow)+"B"