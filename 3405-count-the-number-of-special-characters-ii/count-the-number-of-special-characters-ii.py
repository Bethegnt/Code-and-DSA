class Solution:
   def numberOfSpecialChars(self, word: str) -> int:

       lower = 0
       upper = 0
       invalid = 0

       for ch in word:

           idx = ord(ch.lower()) - ord('a')
           bit = 1 << idx

           if ch.islower():

               # lowercase appearing after uppercase invalidates char
               if upper & bit:
                   invalid |= bit
               else:
                   lower |= bit

           else:
               upper |= bit

       return (lower & upper & ~invalid).bit_count()  