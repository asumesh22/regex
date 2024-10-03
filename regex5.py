import sys; args = sys.argv[1:]
idx = int(args[0])-70

'''
There may not be any capital letters in it, nor apostrophes, spaces, dashes, 
nor any other punctuation, nor any letters used only in foreign alphabets, 
nor letters with diacritical marks (such as a dieresis or tilde).

Find all words ...
70: ... where each vowel occurs at least once
71: ... containing exactly 5 vowels
72: ... with w acting as vowel
73: ... where if all but the first 3 and last 3 letters are removed, a palindrome results
74: ... where there is exactly one b and one t, and they are adjacent to each other
75: ... with the longest contiguous block of one letter
76: ... with the greatest number of a repeated letter
77: ... with the greatest number of adjacent pairs of identical letters
78: ... with the greatest number of consonants
79: ... where no letter is repeated more than once
'''

myRegexLst = [  
    r"/^(?=.*a)(?=.*e)(?=.*i)(?=.*o)(?=.*u)[a-z]*$/m", # 70
    r"/^([^aeiouA-Z\W]*[aeiou]){5}[^aeiou\W]*$/m", # 71
    r"/^(?=\w*[^aeiou\W]w[^aeiou\W]([^aeiou\W]|$))[a-z]*$/m", # 72
    r"/^(?=([a-z])(\w)(\w))\w*\3\2\1$|^aa?$/m", # 73
    r"/^[^\WA-Zbt]*(tb|bt)[^\Wbt]*$/m", # 74
    r"/^[a-z]*(\w)\1\w*$/m", #75
    r"/^[a-z]*(\w)(\w*\1){5}\w*$/m", # 76
    r"/^[a-z]*((\w)\2){3}\w*$/m", # 77
    r"/^(\w*[^aeiou\W]){13}/m", # 78
    r"/^(([a-z])(?!.*\2.*\2))*$/m" # 79
]

if idx < len(myRegexLst):
  print(myRegexLst[idx])

# Aaryan Sumesh, Period 2, Class of 25