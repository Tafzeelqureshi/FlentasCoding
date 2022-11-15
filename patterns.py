def checkInclusion(s1: str, s2: str):
        n1 = len(s1)
        n2 = len(s2)
        
        if n1 > n2: return False

        s1Count = [0] * 26
        s2Count = [0] * 26
        for i in range(n1):
            s1Count[ord(s1[i]) - ord('a')] += 1
            s2Count[ord(s2[i]) - ord('a')] += 1

        for i in range(n2-n1):
            if s1Count == s2Count:
                return True
            s2Count[ord(s2[i]) - ord('a')] -= 1
            s2Count[ord(s2[i+n1]) - ord('a')] += 1
        return s1Count == s2Count

totalCases=int(input())
results=[]
for i in range(totalCases):
  str1=input().strip()
  str2=input().strip()
  results.append(checkInclusion(str1,str2))
for i in results:
  returns="NO"
  if(i):
    returns="YES"
  print(returns)
