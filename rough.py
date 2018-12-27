def solve(s):
    index=s.find("@")
    result=[]
    while index!=-1:
        newInd=index
        while s[newInd]!=" ":
            newInd-=1
            result.append(s[newInd+1:index])
            index=s.find
            

def nthArmanNum(i):
    found,guess=0,0
    while found<=i:
        guess+=1
        if isArmanNum(guess):
            found+=1
    return guess

def isLowerTriangular(l):
    for row in range(len(l)):
        for col in range(len(l)):
            if row==col!=len(l):
                if l[row][col+1:].count(0)>=1:
                    return False
    return True


def reverseD(d):
    ans={}
    for key in d:
        if d[key] in ans:
            ans[d[key]]=set(ans[d[key]]) | {key}
        else:
            ans[d[key]]=key
        
    return ans
    
import math

def nearestPalindrome(start):
    if isPal(start):return start
    guessU=start+1
    guessD=start-1
    while not (isPal(guessU) or isPal(guessD)):
        guessU+=1
        guessD-=1
    if isPal(guessU):
        return guessU
    return guessD

def isPal(num):
    if num>=0:
        num2=num
        dig =int(math.log10(num))+1
        new=0
        while num2>0:
            new+=(num2%10)*10**(dig-1)
            dig-=1
            num2//=10
        return new==num
    return False

def findRectSizeNM(L2,N,M):
    rows,cols=len(L2)-M+1,len(L2)-N+1
    for r in range(rows):
        for c in range(cols):
            if isGood(r,c,N,M,L2):
                return True
    return False

def isGood(r,c,N,M,L2):
    for i in range(M):
        l=L2[r+i][c:c+N]
        if sum(l)!=len(l):
            return False
    return True

def palindromePartition(s):
    s=s
    ans=[]
    i=0
    return solve(s,ans,i)
    
def solve(s,ans,i):
    if "".join(ans)==s and len(ans)!=len(s):
        return ans
    else:
        for j in range(len(s),i-1,-1):
            if isPalindrome(s[i:j]):
                ans.append(s[i:j])
                i2=i
                i=j
                tmp=solve(s,ans,i)
                if not tmp:
                    ans.pop()
                    i=i2
                else:return tmp
        return None

def isPalindrome(s):
    return len(s)>=1 and s==s[::-1]

def powerset(l):
    if len(l)==0:
        return [[]]
    else:
        all=[]
        for sub in powerset(l[1:]):
            all.append(sub)
            all.append(sub+[l[0]])
        return all

def permutations(l):
    if len(l)==0:
        return [[]]
    else:
        all=[]
        for sub in permutations(l[1:]):
            for i in range(len(sub)+1):
                all.append(sub[:i]+[l[0]]+sub[i:])
        return all

def recFindL(L):
    if passed(L):
        return True
    elif -10<L<10:return False
    else:
        return recFindL(L//10)
    
def passed(L):
    return L%10==(L//10)%10
    
import copy
class A(object):
    def __init__(self, x):
        self.x = 2 * x
    
    def __str__(self):
        return "A(" + str(self.x) + ")"
    def add(self, n):
        return self.x + n
class B(A):
    def __init__(self, x, y):
        super().__init__(x)
        self.y = 3 * y
    def sub(self, n):
        return self.x - n
        
def ct1():
    try:
        a, b = A(1), B(3, 4)
        print(a)
        print(b)
        print(b.add(4))
        print(a.sub(2))
        print("All good!")
    except:
        print("Uh oh!")

def passGen(l,num):
    l=l
    num=num
    return gen(l,num)
    
'''def gen(l,num):
    if len(l)==0:
        return [[[l[0]]]]
    else:
        all=[]
        for sub in gen(l[1:],num):
            if len(sub)<=1:
                all.append(sub)
                for i in range(len(l)):
                    all.append([l[i]]+sub])
                    all.append(sub+[l[i]]])
        return all'''

def ct1(s, lst):
    if s in lst:
        print(s, "repeat!")
        return
    else:
        lst.append(s)
    if len(s) == 1:
        print(s)
    else:
        if len(s) == 3:
            print("\n3:", s)
        ct1(s[1:], lst)
        ct1(s[:-1], lst)
ct1("woah", [])