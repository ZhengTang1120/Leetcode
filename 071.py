class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        folders = path.split("/")
        temp = []
        for folder in folders:
            if folder == "..":
                temp = temp[:-1]
            elif folder == "." or folder == "":
                pass
            else:
                temp.append(folder)
        ans = ""
        for f in temp:
            ans += "/"+f
        if ans == "":
            ans = "/"
        return ans
        