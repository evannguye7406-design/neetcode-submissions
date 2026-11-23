class Solution:
    def isPalindrome(self, s: str) -> bool:
        # declaring int as pointers for front and back
        front: int = 0
        back: int = len(s) - 1

        # trace pointers through string
        while front < back:

            # check front and back and see if they're alphanumeric
            if not s[front].isalnum():
                # skip non-alphanumeric chars
                front += 1
            elif not s[back].isalnum():
                back -= 1
            else:
                # compare front and back
                # if not equal, return false
                if not s[front].lower() == s[back].lower():
                    return False

                # move pointers close inwards
                front += 1
                back -= 1

        # if the loop completes without mismatches, it's a valid palindrome
        return True