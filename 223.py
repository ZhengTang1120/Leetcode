class Solution:
    # @param {integer} A
    # @param {integer} B
    # @param {integer} C
    # @param {integer} D
    # @param {integer} E
    # @param {integer} F
    # @param {integer} G
    # @param {integer} H
    # @return {integer}
    def computeArea(self, A, B, C, D, E, F, G, H):
        S1 = (C-A)*(D-B)
        S2 = (G-E)*(H-F)
        s = 0
        l = min(C,G)-max(A,E)
        w = min(H,D)-max(B,F)
        if l > 0 and w >0:
            s = l * w
        S = S1 + S2 -s
        return S