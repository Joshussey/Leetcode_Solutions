class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x > 0 and len(str(x)) > 2:
            for digit in str(x):
                fwdnum = digit
                for revdigit in reversed(str(x)):
                    revnum = revdigit

                    if revnum == fwdnum:
                        return True

        return False
        
        return False