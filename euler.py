import time
from fractions import *
import os
import sys
import resource
import copy
from Queue import *

#Increase recursion limit for p57... probably a better way to do it
sys.setrecursionlimit(1500)

def memoize(f):
    import functools
    cachedResults = dict()
    @functools.wraps(f)
    def wrapper(*args):
        if args not in cachedResults:
            cachedResults[args] = f(*args)
        return cachedResults[args]
    return wrapper

def p1():
    sum = 0
    for x in xrange(1000):
        if x % 3 == 0 or x % 5 == 0:
            sum += x
    return sum

def p2():
    a = [1, 2]
    i = 1
    sum = 2
    while a[i] < 4000000:
        newTerm = a[i - 1] + a[i]
        a += [newTerm]
        if newTerm % 2 == 0:
            sum += newTerm
        i += 1
    #print a
    #print sum

def p3():
    num = 600851475143
    maxFactor = num ** (0.5)
    check = 1
    maxSoFar = check
    while check < maxFactor:
        if isPrime(check) and num % check == 0:
            maxSoFar = check
        check += 2
    return maxSoFar

def isPrime(n):
    if n < 2:
        return False
    else:
        check = 2
        while check <= (n ** 0.5):
            if n % check == 0:
                return False
            check += 1
        return True

def p4():
    maxSoFar = 0
    for x in xrange(999, 99, -1):
        for y in xrange(999, 99, -1):
            check = x * y
            if isPalindrome(check) and maxSoFar < check:
                maxSoFar = check
    return maxSoFar

def isPalindrome(n):
    a = str(n)
    b = a[::-1]
    return a == b

def p5():
    x = 20
    while True:
        numDivisible = 0
        for y in xrange(1, 21):
            if x % y == 0:
                numDivisible += 1
        if numDivisible == len(xrange(1, 21)):
            return x
        #if x % 10000 == 0:
            #print x
        x += 20

def p6():
    #sum of the squares of first 100 natural numbers
    sum = 0
    for y in xrange(1, 101):
        sum += (y ** 2)
    big = (100 * 101) / 2
    return (big ** 2) - sum

def p7(n):
    check = 1
    while n > 0:
        check += 1
        if isPrime(check):
            n -= 1
    return check

def p8(n):
    string = str(n)
    maxProduct = 0
    for i in xrange(len(str(n)) - 5):
        product = 1
        for j in xrange(5):
            product *= int(string[i + j])
        if product > maxProduct:
            maxProduct = product
    return maxProduct

def p9():
    for b in xrange(1, 500):
        for a in xrange(1, b):
            cSquared = a ** 2 + b ** 2
            c = cSquared ** 0.5
            if c % 1 == 0:
                if a + b + c == 1000:
                    #print a, b, c
                    return (a * b * c)
            if a + b + c > 1000:
                break

def p10():
    sum = 0
    for x in xrange(2, 2*(10 ** 6) + 1):
        if isPrime(x):
            sum += x
    return sum

def p11():
    matrix = \
    [[8, 2, 22, 97, 38, 15, 0, 40, 0, 75, 4, 5, 7, 78, 52, 12, 50, 77, 91, 8],
     [49, 49, 99, 40, 17, 81, 18, 57, 60, 87, 17, 40, 98, 43, 69, 48, 4, 56, 62, 0],
     [81, 49, 31, 73, 55, 79, 14, 29, 93, 71, 40, 67, 53, 88, 30, 3, 49, 13, 36, 65],
     [52, 70, 95, 23, 4, 60, 11, 42, 69, 24, 68, 56, 1, 32, 56, 71, 37, 2, 36, 91],
     [22, 31, 16, 71, 51, 67, 63, 89, 41, 92, 36, 54, 22, 40, 40, 28, 66, 33, 13, 80],
     [24, 47, 32, 60, 99, 3, 45, 2, 44, 75, 33, 53, 78, 36, 84, 20, 35, 17, 12, 50],
     [32, 98, 81, 28, 64, 23, 67, 10, 26, 38, 40, 67, 59, 54, 70, 66, 18, 38, 64, 70],
     [67, 26, 20, 68, 2, 62, 12, 20, 95, 63, 94, 39, 63, 8, 40, 91, 66, 49, 94, 21],
     [24, 55, 58, 5, 66, 73, 99, 26, 97, 17, 78, 78, 96, 83, 14, 88, 34, 89, 63, 72],
     [21, 36, 23, 9, 75, 0, 76, 44, 20, 45, 35, 14, 0, 61, 33, 97, 34, 31, 33, 95],
     [78, 17, 53, 28, 22, 75, 31, 67, 15, 94, 3, 80, 4, 62, 16, 14, 9, 53, 56, 92],
     [16, 39, 5, 42, 96, 35, 31, 47, 55, 58, 88, 24, 0, 17, 54, 24, 36, 29, 85, 57],
     [86, 56, 0, 48, 35, 71, 89, 7, 5, 44, 44, 37, 44, 60, 21, 58, 51, 54, 17, 58],
     [19, 80, 81, 68, 5, 94, 47, 69, 28, 73, 92, 13, 86, 52, 17, 77, 4, 89, 55, 40],
     [4, 52, 8, 83, 97, 35, 99, 16, 7, 97, 57, 32, 16, 26, 26, 79, 33, 27, 98, 66],
     [88, 36, 68, 87, 57, 62, 20, 72, 3, 46, 33, 67, 46, 55, 12, 32, 63, 93, 53, 69],
     [4, 42, 16, 73, 38, 25, 39, 11, 24, 94, 72, 18, 8, 46, 29, 32, 40, 62, 76, 36],
     [20, 69, 36, 41, 72, 30, 23, 88, 34, 62, 99, 69, 82, 67, 59, 85, 74, 4, 36, 16],
     [20, 73, 35, 29, 78, 31, 90, 1, 74, 31, 49, 71, 48, 86, 81, 16, 23, 57, 5, 54],
     [1, 70, 54, 71, 83, 51, 54, 69, 16, 92, 33, 48, 61, 43, 52, 1, 89, 19, 67, 48]]
     #all of the directions, up left, up, up right, etc.
    dirs = [(-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)]
    numRows, numCols = len(matrix), len(matrix[0])
    #just to see where it finds the answer
    maxProduct = 0
    maxStartRow = 0
    maxStartCol = 0
    maxDir = 0
    #iterates through all of the items in the matrix
    for curRow in xrange(numRows):
        for curCol in xrange(numCols):
            for dir in dirs:
                checkProduct = 1
                for i in xrange(4):
                    checkRow = curRow + i * dir[0]
                    checkCol = curCol + i * dir[1]
                    #checks to see if the next item is in the matrix
                    if (checkRow not in xrange(numRows) or 
                        checkCol not in xrange(numCols)):
                        break
                    #otherwise gets the product with the number at that index
                    else: checkProduct *= matrix[checkRow][checkCol]
                if checkProduct > maxProduct: 
                    maxProduct = checkProduct
                    maxStartRow = curRow
                    maxStartCol = curCol
                    maxDir = dir
    #gives the start location and the direction to follow
    #print "Row: ", maxStartRow, "Col: ", maxStartCol, "Dir: ", maxDir
    return maxProduct

def p12():
    startTime = time.time()
    x = 1
    while True:
        #can improve efficiency by not re-calculating over and over...
        testNum = nthTriangleNumber(x)
        numfactors = fasterNumFactors(testNum)
        if numfactors >= 500:
            endTime = time.time()
            #print "Time Taken:", endTime - startTime, "seconds"
            return testNum
        x += 1

def nthTriangleNumber(n):
    return (n * (n + 1)) / 2

def fasterNumFactors(n):
    if n == 1: return n
    numfactors = 0
    for check in xrange(1, int(round((n ** 0.5))) + 1):
        if n % check == 0:
            numfactors += 2
    return numfactors

def p13():
    list = [37107287533902102798797998220837590246510135740250,
     46376937677490009712648124896970078050417018260538,
     74324986199524741059474233309513058123726617309629,
     91942213363574161572522430563301811072406154908250,
     23067588207539346171171980310421047513778063246676,
     89261670696623633820136378418383684178734361726757,
     28112879812849979408065481931592621691275889832738,
     44274228917432520321923589422876796487670272189318,
     47451445736001306439091167216856844588711603153276,
     70386486105843025439939619828917593665686757934951,
     62176457141856560629502157223196586755079324193331,
     64906352462741904929101432445813822663347944758178,
     92575867718337217661963751590579239728245598838407,
     58203565325359399008402633568948830189458628227828,
     80181199384826282014278194139940567587151170094390,
     35398664372827112653829987240784473053190104293586,
     86515506006295864861532075273371959191420517255829,
     71693888707715466499115593487603532921714970056938,
     54370070576826684624621495650076471787294438377604,
     53282654108756828443191190634694037855217779295145,
     36123272525000296071075082563815656710885258350721,
     45876576172410976447339110607218265236877223636045,
     17423706905851860660448207621209813287860733969412,
     81142660418086830619328460811191061556940512689692,
     51934325451728388641918047049293215058642563049483,
     62467221648435076201727918039944693004732956340691,
     15732444386908125794514089057706229429197107928209,
     55037687525678773091862540744969844508330393682126,
     18336384825330154686196124348767681297534375946515,
     80386287592878490201521685554828717201219257766954,
     78182833757993103614740356856449095527097864797581,
     16726320100436897842553539920931837441497806860984,
     48403098129077791799088218795327364475675590848030,
     87086987551392711854517078544161852424320693150332,
     59959406895756536782107074926966537676326235447210,
     69793950679652694742597709739166693763042633987085,
     41052684708299085211399427365734116182760315001271,
     65378607361501080857009149939512557028198746004375,
     35829035317434717326932123578154982629742552737307,
     94953759765105305946966067683156574377167401875275,
     88902802571733229619176668713819931811048770190271,
     25267680276078003013678680992525463401061632866526,
     36270218540497705585629946580636237993140746255962,
     24074486908231174977792365466257246923322810917141,
     91430288197103288597806669760892938638285025333403,
     34413065578016127815921815005561868836468420090470,
     23053081172816430487623791969842487255036638784583,
     11487696932154902810424020138335124462181441773470,
     63783299490636259666498587618221225225512486764533,
     67720186971698544312419572409913959008952310058822,
     95548255300263520781532296796249481641953868218774,
     76085327132285723110424803456124867697064507995236,
     37774242535411291684276865538926205024910326572967,
     23701913275725675285653248258265463092207058596522,
     29798860272258331913126375147341994889534765745501,
     18495701454879288984856827726077713721403798879715,
     38298203783031473527721580348144513491373226651381,
     34829543829199918180278916522431027392251122869539,
     40957953066405232632538044100059654939159879593635,
     29746152185502371307642255121183693803580388584903,
     41698116222072977186158236678424689157993532961922,
     62467957194401269043877107275048102390895523597457,
     23189706772547915061505504953922979530901129967519,
     86188088225875314529584099251203829009407770775672,
     11306739708304724483816533873502340845647058077308,
     82959174767140363198008187129011875491310547126581,
     97623331044818386269515456334926366572897563400500,
     42846280183517070527831839425882145521227251250327,
     55121603546981200581762165212827652751691296897789,
     32238195734329339946437501907836945765883352399886,
     75506164965184775180738168837861091527357929701337,
     62177842752192623401942399639168044983993173312731,
     32924185707147349566916674687634660915035914677504,
     99518671430235219628894890102423325116913619626622,
     73267460800591547471830798392868535206946944540724,
     76841822524674417161514036427982273348055556214818,
     97142617910342598647204516893989422179826088076852,
     87783646182799346313767754307809363333018982642090,
     10848802521674670883215120185883543223812876952786,
     71329612474782464538636993009049310363619763878039,
     62184073572399794223406235393808339651327408011116,
     66627891981488087797941876876144230030984490851411,
     60661826293682836764744779239180335110989069790714,
     85786944089552990653640447425576083659976645795096,
     66024396409905389607120198219976047599490197230297,
     64913982680032973156037120041377903785566085089252,
     16730939319872750275468906903707539413042652315011,
     94809377245048795150954100921645863754710598436791,
     78639167021187492431995700641917969777599028300699,
     15368713711936614952811305876380278410754449733078,
     40789923115535562561142322423255033685442488917353,
     44889911501440648020369068063960672322193204149535,
     41503128880339536053299340368006977710650566631954,
     81234880673210146739058568557934581403627822703280,
     82616570773948327592232845941706525094512325230608,
     22918802058777319719839450180888072429661980811197,
     77158542502016545090413245809786882778948721859617,
     72107838435069186155435662884062257473692284509516,
     20849603980134001723930671666823555245252804609722,
     53503534226472524250874054075591789781264330331690]
    return sum(list)

def p14():
    maxLength = 1
    for x in xrange(1, 1000000):
        length = testCollatz(x)
        #if x % 50000 == 0:
            #print x
        if length > maxLength:
            maxLength = length
            num = x
    return num

def testCollatz(n):
    numTerms = 1
    while n != 1:
        if n % 2 == 0:
            n /= 2
        elif n % 2 == 1:
            n = 3*n + 1
        numTerms += 1
    return numTerms

def p15(n):
    grid = [[0 for x in xrange(n + 1)] for y in xrange(n + 1)]
    startPos = (0, 0) #the topleft of the grid is where it starts
    findRoute(startPos, grid, 0, 0)

def findRoute(curPos, grid, numDown, numRight):
    numRoutes = 0
    if isEnd(curPos, grid):
        return 1 + numRoutes
    elif isLegal15(curPos, grid):
        dirs = [(1, 0), (0, 1)]
        for dir in dirs:
            newPos = (curPos[0] + dir[0]*numDown, curPos[1] + dir[1]*numRight)
            findRoute(newPos, grid, numDown + 1, numRight)
            findRoute(newPos, grid, numDown, numRight + 1)
    else:
        return 0

def isEnd(curPos, grid):
    return curPos == (len(grid), len(grid[0]))

def isLegal15(pos, grid):
    return pos[0] in xrange(len(grid)) and pos[1] in xrange(len(grid[0]))

def p16():
    num = 2 ** 1000
    return sumDigits(num)

def sumDigits(n):
    sum = 0
    while n > 9:
        sum += n % 10 #gets the last digit
        n /= 10
    return sum + n #adds the very last digit

def getDigit(n, place):
    ## 543 % 10 = 3
    ## 543 / 10 % 10 = 4
    ## 543 / 100 % 10 = 4
    return (n / (10 ** (place - 1))) % 10

def p17(inputNum):
    #uses getLength to get numDigits
    y = 1 #looping value
    answer = 0
    while y <= inputNum:
        numDigits = getLength(y)
        onesDigit = getDigit(y, 1)
        if numDigits == 1:
            answer = addSingleDigitWords(onesDigit, answer)
        elif numDigits == 2:
            tensDigit = getDigit(y, 2)
            if tensDigit == 1:
                answer = addTeens(onesDigit, answer)
            elif onesDigit != 0:
                answer = addRealTens(tensDigit, answer)
                answer = addSingleDigitWords(onesDigit, answer)
            elif onesDigit == 0:
                answer = addRealTens(tensDigit, answer)
        elif numDigits == 3:
            tensDigit = getDigit(y, 2)
            hundredsDigit = getDigit(y, 3)
            answer = addSingleDigitWords(hundredsDigit, answer)
            answer += 7 #hundred
            if not (tensDigit == 0 and onesDigit == 0):
                answer += 3 #and
            if tensDigit == 0:
                answer = addSingleDigitWords(onesDigit, answer)
            elif tensDigit == 1:
                answer = addTeens(tensDigit, answer)
            elif onesDigit != 0:
                answer = addRealTens(tensDigit, answer)
                answer = addSingleDigitWords(onesDigit, answer)
            elif onesDigit == 0:
                answer = addRealTens(tensDigit, answer)
        elif numDigits == 4:
            answer += 3 #one
            answer += 8 #thousand
        #print "y is: " + str(y) + " answer is: " + str(answer)
        y += 1
    return answer

def addRealTens(n, answer):
    if n == 4 or n == 5 or n == 6:
        answer += 5
    elif n == 2 or n == 3 or n == 8 or n == 9:
        answer += 6
    else:
        answer += 7 #seventy
    return answer
    # twenty 6
    # thirty 6
    # forty 5
    # fifty 5
    # sixty 5
    # seventy 7
    # eighty 6
    # ninety 6

def addSingleDigitWords(n, answer):
    if n == 1 or n == 2 or n == 6:
        answer += 3 #all three letter words
    elif n == 4 or n == 5 or n == 9:
        answer += 4 #4 letters
    elif n != 0:
        answer += 5 #three seven eight
    return answer

def addTeens(n, answer):
    #eleven 6
    #twelve 6
    #thirteen 8
    #fourteen 8
    #fifteen 7
    #sixteen 7
    #seventeen 9
    #eighteen 8
    #nineteen 8
    if n == 0:
        answer += len("ten")
    if n == 1 or n == 2:
        answer += len("eleven") #twelve is the same len
    if n == 3 or n == 4 or n == 8 or n == 9:
        answer += len("thirteen") #all eight letters long
    if n == 5 or n == 6:
        answer += len("fifteen") #all seven letters long
    if n == 7:
        answer += len("seventeen")
    return answer

def p18():
    tree = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 4, 82, 47, 65,
            19, 1, 23, 75, 3, 34, 88, 2, 77, 73, 7, 63, 67, 99, 65,
            4, 28, 6, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 
            41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 
            43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 
            68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 
            48, 63, 66, 4, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
            4, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 4, 23]
    tree_length = len(tree)
    cur_index = 0
    height = 1
    l_c = cur_index + height
    r_c = l_c + 1
    ##print "l_c is: " + str(l_c) + " r_c is: " + str(r_c)
    max_sum = tree[0] + max(p18_helper(tree, l_c, tree_length, height + 1), 
                            p18_helper(tree, r_c, tree_length, height + 1))
    return max_sum

def p18_helper(tree, cur_index, tree_length, h):
    if cur_index not in range(tree_length):
        return 0
    else:
        l_c = cur_index + h
        r_c = l_c + 1
        x =  tree[cur_index] + max(p18_helper(tree, l_c, tree_length, h+1), 
                                   p18_helper(tree, r_c, tree_length, h+1))
        #print "max is: " + str(x)
        return x

def p19():
    days = 1 #1 Jan 1900
    month = 1
    result = 0
    year = 1900
    while year <= 2000:
        while month <= 12:
            if (month == 1 or month == 3 or month == 5 or month == 7 
                or month == 8 or month == 10 or month == 12):
                days += 31
                month += 1
            elif (month == 2):
                if year != 1900 and year % 4 == 0:
                    days += 29
                else:
                    days += 28
                month += 1
            elif (month == 4 or month == 6 or month == 9 or month == 11):
                days += 30
                month += 1
            if days % 7 == 0 and year != 1900:
                result += 1
                #print "year is: " + str(year) + " month is: " + str(month) + \
                " result is: " + str(result)
        assert(month == 13)
        month = 1
        year += 1
    return result

def p20():
    num = factorial(100)
    return sumDigits(num)

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def p21():
    #how the hell do i check if a number is amicable??
    # if d(a) = b and d(b) then == a then it's amicable!
    listAmicable = []
    for a in xrange(1, 10000):
        b = sumDivisors(a)
        if b < 10000 and sumDivisors(b) == a and b != a:
            if a not in listAmicable:
                listAmicable += [a]
            if b not in listAmicable:
                listAmicable += [b]
    #print listAmicable
    return sum(listAmicable)

def p22():
    with open("names.txt", "r") as f:
        names = f.readline().strip().replace('"', '').split(',')
        names.sort()
    total = 0
    for i in range(len(names)):
        name = names[i]
        subtotal = 0
        for char in name:
            value = (ord(char) - 64) * (i + 1) #gets the cardinality
            subtotal += value
        total += subtotal
    return total

def p23():
    result = []
    abundantNums = []
    for i in range(1, 28124):
        if isAbundant(i):
            abundantNums.append(i)
        #if i % 1000 == 0:
            #print "i is: " + str(i)
    possible = dict()
    for a in range(1, 28124):
        possible[a] = False
    #print "Dictionary made!"
    for j in range(0, len(abundantNums)):
        for k in range(j, len(abundantNums)):
            #if j % 1000 == 0 and k % 1000 == 0:
                #print "j is: " + str(j) + " k is: " + str(k)
            candidate = abundantNums[j] + abundantNums[k]
            if candidate <= 28123:
                possible[candidate] = True
    #print "True's put in place"
    result = []
    for l in range(1, 28124):
        #if l % 1000 == 0:
            #print l
        if possible[l] == False:
            result.append(l)
    return sum(result)

def p24():
    a = "0123456789"
    a = permutations(a)
    a.sort()
    return a[999999]

def permutations(a):
    # returns a list of all permutations of the list a
    if (len(a) == 0):
        return [[]]
    else:
        allPerms = [ ]
        for subPermutation in permutations(a[1:]):
            for i in xrange(len(subPermutation)+1):
                allPerms += [subPermutation[:i] + [a[0]] + subPermutation[i:]]
        return allPerms

def perm_ints(a):
    # returns a list of all permutations of the list a
    if (len(a) == 0):
        return [[]]
    else:
        allPerms = [ ]
        for subPermutation in perm_ints(a[1:]):
            for i in xrange(len(subPermutation)+1):
                allPerms += [int(subPermutation[:i] + [a[0]] + subPermutation[i:])]
        return allPerms

def getProperFactors(n):
    factors = []
    for i in xrange(1, (n/2) + 1):
        if n % i == 0:
            factors.append(i)
    return factors

def isAbundant(n):
    factors = getProperFactors(n)
    return sum(factors) > n

def sumDivisors(n):
    sum = 0
    for x in xrange(1, n):
        if n % x == 0:
            sum += x
    return sum

def p25():
    a = [1, 1]
    while True:
        nextTerm = a[len(a) - 2] + a[len(a) - 1]
        a += [nextTerm]
        if getLength(nextTerm) == 1000:
            return len(a)

def getLength(n):
    length = 1
    while n > 9:
        n /= 10
        length += 1
    return length

def p26():
    results = []
    for n in range(1, 1000):
        result = ""
        if n <= 10:
            start = 10
        elif n > 10 and n <= 100:
            start = 100
            result += "0"
        elif n > 100 and n <= 1000:
            start = 1000
            result += "00"
        val = start/n
        result += str(val)
        for i in range(5000):
            start = (start % n) * 10
            val = start / n
            result += str(val)
        results.append(result)
    #print results[985]
    num = 1
    max_length = 1
    for l in range(1, 1000):
        #print l,
        cycle_length = getCycleLength(l, results[l-1])
        #print "cycle length is: " + str(cycle_length)
        if cycle_length > max_length:
            max_length = cycle_length
            num = l
    return num
    

def getCycleLength(n, s):
    start = 50 #just a guess, no mathematical justification
    cycle_length = 1
    while True:
        end_index = start + cycle_length
        repeat_end = start + (cycle_length * 2)
        if (s[start:end_index]*2 == s[start:repeat_end]):
            return cycle_length
        else:
            cycle_length += 1



def p27():
    maxConsecutivePrimes = 0
    for a in xrange(-999, 1000):
        for b in xrange(-999, 1000):
            test = getNumConsecutivePrimes(a, b)
            if test > maxConsecutivePrimes:
                maxConsecutivePrimes = test
                maxProduct = a * b
                maxA = a
                maxB = b
    #print maxA, maxB
    return maxProduct

def p28(n):
    sum = 1
    for i in range(3, n+1, 2):
        top_right = i ** 2
        top_left = top_right - (i - 1)
        bottom_left = top_right - (2 * (i - 1))
        bottom_right = top_right - (3 * (i - 1))
        sum += (top_right + top_left + bottom_left + bottom_right)
    return sum

def p29():
    finalAnswer = set()
    for a in xrange(2, 101):
        for b in xrange(2, 101):
            term = a**b
            finalAnswer.add(term)
    return len(finalAnswer)

def better29():
    return len(set([a**b for a in xrange(2, 101) for b in xrange(2, 101)]))

def getNumConsecutivePrimes(a, b):
    n = 0
    while True:
        candidate = (n ** 2) + (a * n) + b
        if isPrime(candidate):
            n += 1
        else:
            return n

def p30():
    upperBound = find30UpperBound()
    listAnswers = []
    for x in xrange(2, upperBound):
        #if x % 100000 == 0:
            #print x
        if isFifthSum(x):
            listAnswers += [x]
    #print listAnswers
    return sum(listAnswers)

def isFifthSum(n):
    numLength = getLength(n)
    check = n
    numSum = 0
    while numLength > 0:
        onesDigit = check % 10 # gets ones digit
        numSum += onesDigit ** 5 #by defn of problem
        check /= 10 #gets rid of ones digit
        numLength -= 1
    return numSum == n

def find30UpperBound():
    numDigits = 1
    while True:
        testNum = 0
        for x in xrange(numDigits):
            testNum += 9 * (10 ** x)
        if (9 ** 5) * numDigits < testNum:
            return testNum
        numDigits += 1

def p31():
    result = 0
    for pence in range(0, 201):
        #print pence
        total = 0
        for two_pence in range(0, 201, 2):
            one_two_total = pence + two_pence
            if one_two_total > 200:
                continue
            for five_pence in range(0, 201, 5):
                one_two_five_total = one_two_total + five_pence
                if one_two_five_total > 200:
                    continue
                for ten_pence in range(0, 201, 10):
                    t_t = one_two_five_total + ten_pence
                    if t_t > 200:
                        continue
                    for twenty_pence in range(0, 201, 20):
                        twenty_t = t_t + twenty_pence
                        if twenty_t > 200:
                            continue
                        for fifty_pence in range(0, 201, 50):
                            fifty_t = twenty_t + fifty_pence
                            for one_pound in range(0, 201, 100):
                                one_p_t = fifty_t + one_pound
                                if one_p_t > 200:
                                    continue
                                for two_pound in range(0, 201, 200):
                                    total = pence + two_pence + five_pence
                                    total += ten_pence + twenty_pence
                                    total += fifty_pence + one_pound
                                    total += two_pound
                                    if total > 200:
                                        continue
                                    if total == 200:
                                        result += 1

    return result

def p32():
    a = permutations("123456789")
    products = []
    length = len(a)
    ##print length
    for x in range(len(a)):
        for i in range(1, 5):
            for j in range(i+1, i+4):
                num1 = ""
                num2 = ""
                num3 = ""
                for element in a[x][0:i]:
                    num1 += element
                for element2 in a[x][i:j]:
                    num2 += element2
                for element3 in a[x][j:len(a[x])]:
                    num3 += element3
                if (int(num1)*int(num2) == int(num3) and 
                    int(num3) not in products):
                    ##print "num1 is:", num1, "num2 is:", num2, "num3 is:", num3
                    products.append(int(num3))   
    return sum(products)

def p34():
    answerList = []
    for x in xrange(3, 1000000):
        #if x % 100000 == 0:
            #print x
        if isCurious(x):
            answerList += [x]
    #print answerList
    return sum(answerList)

def isCurious(n):
    numLength = getLength(n)
    check = n
    numSum = 0
    while numLength > 0:
        onesDigit = check % 10 #gets ones digit
        addend = factorial(onesDigit)
        if addend > n:
            return False
        numSum += addend
        if numSum > n:
            return False
        check /= 10 #gets rid of ones digit
        numLength -= 1
    return numSum == n

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

def p35(n):
    #get the number of circular primes under 1 million
    numCircularPrimes = 0
    for x in xrange(2, n + 1): #inclusive up to n
        if isCircularPrime(x):
            #I don't think I'll have to deal with leading 0s...
            #consider 1001. eventually, the 0 will be in the
            #place, and won't be prime and will break before
            #getting the next rotation
            numCircularPrimes += 1
    return numCircularPrimes

def isCircularPrime(n):
    numLength = numRotations = getLength(n)
    while numRotations > 0:
        if not isPrime(n):
            return False
        n = nextRotation(n, numLength)
        numRotations -= 1
    return True

def nextRotation(n, numLength):
    onenigit = n % 10
    n /= 10 #gets rid of ones digit
    frontDigit = onenigit * (10 ** (numLength - 1))
    return frontDigit + n

def convert_to_bin(n):
    if n == 0:
        return "0"
    s = ""
    while n > 0:
        if n % 2 == 0:
            ch = "0"
        if n % 2 == 1:
            ch = "1"
        s = ch + s
        n = n/2
    return s

def p36():
    total = 0
    for i in range(1000001):
        if isPalindrome(str(i)) and isPalindrome(convert_to_bin(i)):
            #print i
            total += i
    return total

def p37():
    """Returns sum of eleven truncatable primes"""
    numPrimes = 11
    iter = 8 #skips 2, 3, 5, and 7
    primes = []
    while numPrimes > 0:
        #if iter % 100000 == 0:
            #print iter
        if isLeftTrunc(iter) and isRightTrunc(iter):
            primes.append(iter)
            numPrimes -= 1
        iter += 1
    #print primes
    return sum(primes)

def isLeftTrunc(n):
    numLength = getLength(n)
    while numLength > 0:
        if isPrime(n):
            n %= 10 ** (numLength - 1)#removes leftmost digit
            numLength -= 1
        else:
            return False
    return True

def isRightTrunc(n):
    numLength = getLength(n)
    while numLength > 0:
        if isPrime(n):
            n /= 10 #removes rightmost digit
            numLength -= 1
        else:
            return False
    return True

def p40():
    temp = 1
    thingy = ""
    while len(thingy) < 1000000:
        thingy += str(temp)
        temp += 1
    d1 = int(thingy[1-1])
    d10 = int(thingy[10-1])
    d100 = int(thingy[100-1])
    d1000 = int(thingy[1000-1])
    d10000 = int(thingy[10000-1])
    d100000 = int(thingy[100000-1])
    d1000000 = int(thingy[1000000-1])
    answer = d1*d10*d100*d1000*d10000*d100000*d1000000
    return answer

def p41():
    max_num = 2
    #print "Generating permutations"
    c = permutations("1234567")
    #print "Done!"
    length = len(c)
    for x in range(len(c)):
        num = ""
        for a in c[x]:
            num += a
        #if x % 1000 == 0:
            #print (float(x)/length)*100, "% complete"
        if isPrime(int(num)) and int(num) > max_num:
            max_num = int(num)
    return max_num

def p43():
    #print "Generating list with permutations..."
    a = permutations("0123456789")
    #print "Done!"
    #print "Solving problem..."
    length = len(a)
    nums_with_property = []
    ##print length
    for perm in a:
        p1 = perm[1] + perm[2] + perm[3]
        if not (int(p1) % 2 == 0):
            continue
        p2 = perm[2] + perm[3] + perm[4]
        if not (int(p2) % 3 == 0):
            continue
        p3 = perm[3] + perm[4] + perm[5]
        if not (int(p3) % 5 == 0):
            continue
        p4 = perm[4] + perm[5] + perm[6]
        if not (int(p4) % 7 == 0):
            continue
        p5 = perm[5] + perm[6] + perm[7]
        if not (int(p5) % 11 == 0):
            continue
        p6 = perm[6] + perm[7] + perm[8]
        if not (int(p6) % 13 == 0):
            continue
        p7 = perm[7] + perm[8] + perm[9]
        if not (int(p7) % 17 == 0):
            continue
        number = ""
        for x in perm:
            number += x
        #print number + " was added!"
        nums_with_property.append(int(number))
    return sum(nums_with_property)

def p44():
    curNumUpper = 2
    while True:
        curNumLower = 1
        while curNumLower < curNumUpper:
            Pj = nthPentNum(curNumLower)
            Pk = nthPentNum(curNumUpper)
            if isPentNum(Pj + Pk) and isPentNum(Pk - Pj):
                #print "Pk = ", Pk, "Pj = ", Pj
                #print curNumLower, "th pent num, ", curNumUpper, "th pent num"
                return abs(Pk - Pj)
            else:
                curNumLower += 1
        #if curNumUpper % 1000 == 0:
            #print curNumUpper
        curNumUpper += 1

def nthPentNum(n):
    return (n * (3*n - 1))/2

def isPentNum(n):
    n = float(n)
    #based on formula Pn = n(3n-1)/2
    a = 3
    b = -1
    c = 2*(-n) #move to other side of eqn
    try:
        soln1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    except:
        soln1 = -1 #return false
    try:
        soln2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    except:
        soln2 = -1 #returns false
    return (soln1 % 1 == 0 and soln1 > 0) or \
        (soln2 % 1 == 0 and soln2 > 0)

def isTriNum(n):
    n = float(n)
    #based on formula Tn = n(n+1)/2
    a = 1
    b = 1
    c = 2*(-n) #move to other side of eqn
    try:
        soln1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    except:
        soln1 = -1 #return false
    try:
        soln2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    except:
        soln2 = -1 #returns false
    return (soln1 % 1 == 0 and soln1 > 0) or \
        (soln2 % 1 == 0 and soln2 > 0)

def isHexNum(n):
    n = float(n)
    #based on formulat Hn = n(2n-1)
    a = 2
    b = -1
    c = (-1)*n #move to other side of eqn
    try:
        soln1 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)
    except:
        soln1 = -1 #return false
    try:
        soln2 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)
    except:
        soln2 = -1 #returns false
    return (soln1 % 1 == 0 and soln1 > 0) or \
        (soln2 % 1 == 0 and soln2 > 0)

def p45(n):
    start = 2 #second triangle number
    while n > 0:
        tester = int((start*(start + 1))/2.0)
        #if start % 10000 == 0:
            #print tester
        if isTriNum(tester) and isPentNum(tester) and isHexNum(tester):
            #print tester, "is the", str(start)+"th Triangle Number"
            n -= 1
        start += 1
    return None

def p46():
    check = 1
    while True:
        if isPrime(check):
            check += 2
        else:
            represent = False
            for x in xrange(check):
                if isPrime(x):
                    for y in xrange(int(check ** (0.5))):
                        if x + (2 * (y ** 2)) == check:
                            #print check, " = ", x, " + ", "2 * ", y, "** 2"
                            represent = True
                            break
                if represent:
                    break
            if not represent:
                return check
            check += 2

def p47(n):
    """Returns n consecutive numbers with n distinct prime factors."""
    curNum = 2
    while True:
        numConsecutive = 0 
        #keeps track of consecutive numbers that follow criteria
        while numConsecutive <= n:
            factorization = getPrimeFactorization(curNum)
            if len(factorization) != n:
                break
            else:
                numConsecutive += 1
                curNum += 1
        if numConsecutive == n:
            listNums = []
            for x in xrange(n):
                listNums.append(curNum - x - 1)
                #the additional - 1 comes from the poorly written loop above
            listNums.reverse()
            return listNums
        curNum += 1
        #if curNum % 10000 == 0:
            #print curNum

    #while loop through numbers
    #get a prime factorization, store into a set
    #check to check size of set
    #check to see how many consecutive numbers have this property

def getPrimeFactorization(n):
    primeFactors = set()
    if n <= 1: return primeFactors
    while not isPrime(n):
        factorCheck = 2
        while True:
            if n % factorCheck == 0:
                n /= factorCheck
                primeFactors.add(factorCheck)
                break
            else:
                factorCheck += 1
    primeFactors.add(n)
    return primeFactors

def p48(number, num_digits):
    #n = 10 ** 10
    answer = (1 ** 1) % (10 ** num_digits)
    total = 1
    for i in range(2, number):
        term = (i ** i) % (10 ** num_digits)
        answer = (answer + term) % (10 ** num_digits)
    return answer

#this is some ugly ass code
def p49():
    primes = []
    candidates = []
    for i in range(1000, 10000):
        if isPrime(i):
            primes.append(i)
    for prime in primes:
        num = str(prime)
        a = permutations(num)
        #the next three lines remove duplicates
        for element in range(len(a)):
            a[element] = tuple(a[element])
        a = list(set(a)) #sets do not have duplicates
        numPrime = 0
        primeList = [prime]
        for x in range(len(a)):
            checker = getNum(a, x)
            if (isPrime(checker) and getLength(checker) == 4 and 
                checker not in primeList):
                numPrime += 1
                primeList.append(checker)
        if numPrime >= 3:
            candidates.append(primeList)
    for y in candidates:
        y.sort()
    answers = []
    #printer = False
    for curList in candidates:
        for j in range(len(curList)-2):
            for k in range(j+1, len(curList)-1):
                for l in range(k+1, len(curList)):
                    d1 = curList[k] - curList[j]
                    d2 = curList[l] - curList[k]
                    if (d1 == d2 and (curList[j], curList[k], curList[l]) 
                        not in answers):
                        answers += [(curList[j], curList[k], curList[l])]
    return answers


def getNum(permutations, index):
    temp = ""
    b = permutations[index] #gets the sublist in permutations you want
    for element in b:
        temp += element
    return int(temp)

def p50(n):
    primes = [2]
    maxSum = 0
    max_terms = 0
    #print "Generating list of primes..."
    for i in range(3, n/2, 2):
        if isPrime(i):
            primes.append(i)
    #print "Done!"
    #print "Searching for longest sum..."
    total = 0
    #print len(primes)
    for j in range(len(primes)):
        #if j % 1000 == 0:
            #print j
        ##print "j is: ", j
        index = j
        while total < n:
            if index >= len(primes):
                break
            ##print "total is: ", total, "primes[index] is: ", primes[index]
            total += primes[index]
            index += 1
            if (total > maxSum and isPrime(total) and (index - j) > max_terms
                and total < n):
                maxSum = total
                start_prime = primes[j]
                max_terms = (index - j)
        total = 0
    #print "Done!"
    return (maxSum, start_prime, max_terms)

def p54():
    p1_hands = []
    p2_hands = []
    #this part reads from the file and generates a 2d list of
    #poker hands, where corresponding indices between p1_hands and
    #p2_hands are two hands that are played against each other
    with open("poker.txt") as f:
        for line in f:
            both_hands = line.strip().split()
            cur_p1_hand = [both_hands[a] for a in range(5)]
            cur_p2_hand = [both_hands[b] for b in range(5, len(both_hands))]
            p1_hands.append(cur_p1_hand)
            p2_hands.append(cur_p2_hand)
    poker_hand_ranks = assign_poker_hand_vals()
    for i in range(len(p1_hands)):
        p1_cur_hand = p1_hands[i]
        p2_cur_hand = p2_hands[i]
        winner = assign_winner(p1_cur_hand, p2_cur_hand, poker_hand_ranks)

def assign_winner(p1_hand, p2_hand, poker_hand_dict):
    p1_rank = getHandRank(p1_hand)
    p2_rank = getHandRank(p2_hand)
    if poker_hand_dict[p1_rank] > poker_hand_dict[p2_rank]:
        return 1
    elif poker_hand_dict[p2_rank] > poker_hand_dict[p1_rank]:
        return 2
    elif poker_hand_dict[p1_rank] == poker_hand_dict[p2_rank]:
        pass
        #compare the next highest card

#finish this.....
def getHandRank(hand):
    hand_ranks = []
    c1, c2, c3, c4, c5 = hand[0], hand[1], hand[2], hand[3], hand[4]
    c1_s, c2_s, c3_s, c4_s, c5_s = \
        getSuit(c1), getSuit(c2), getSuit(c3), getSuit(c4), getSuit(c5)
    all_suits = set([c1_s, c2_s, c3_s, c4_s, c5_s])
    c1_r, c2_r, c3_r, c4_r, c5_r = \
        getRank(c1), getRank(c2), getRank(c3), getRank(c4), getRank(c5)
    all_ranks = set([c1_r, c2_r, c3_r, c4_r, c5_r])
    #checks flush
    if len(all_suits) == 1:
        hand_ranks += ["Flush"]
    #checks straight
    least_card_r = min(all_ranks)
    if (least_card_r + 1 in all_ranks and least_card_r + 2 in all_ranks and
        least_card_r + 3 in all_ranks and least_card_r + 4 in all_ranks):
        hand_ranks += ["Straight"]
    #checks four of a kind or a full house
    if len(all_ranks) == 2:
        if max_num_same_rank(hand) == 4:
            hand_ranks += ["Four of a Kind"]
        #technically this can be an else, but I want to be explicit
        elif max_num_same_rank(hand) == 3:
            hand_ranks += ["Full House"]


def max_num_same_rank(hand):
    #since the card is in the hand, must count itself as 
    #having the same rank
    max_same_rank = 1
    num_same_rank = 1
    for card in hand:
        card_rank = getRank(card)
        for other_card in hand:
            #check all the other cards in the hand
            if other_card == card:
                continue
            else:
                other_rank == getRank(other_card)
                if other_rank == card_rank:
                    num_same_rank += 1
        if num_same_rank > max_same_rank:
            max_same_rank = num_same_rank
    return max_same_rank

def assign_poker_hand_vals():
    dictionary = dict()   
    dictionary["High Card"] = 0
    dictionary["One Pair"] = 1
    dictionary["Two Pair"] = 2
    dictionary["Three of a Kind"] = 3
    dictionary["Straight"] = 4
    dictionary["Flush"] = 5
    dictionary["Full House"] = 6
    dictionary["Four of a Kind"] = 7
    dictionary["Straight Flush"] = 8
    dictionary["Royal Flush"] = 9
    return dictionary

def getRank(card):
    try:
        return int(card[0])
    except:
        if card[0] == "T":
            return 10
        elif card[0] == "J":
            return 11
        elif card[0] == "Q":
            return 12
        elif card[0] == "K":
            return 13
        elif card[0] == "A":
            return 14

def getSuit(card):
    return card[1]

def p57(n):
    answer = 0
    for i in range(1, n+1):
        if i % 100 == 0:
            print i
        tester = 1 + p57_helper(i)
        num_digits_numerator = getLength(tester.numerator)
        num_digits_denominator = getLength(tester.denominator)
        if num_digits_numerator > num_digits_denominator:
            answer += 1
    return answer

def p57_helper(n):
    #REQUIRES n >= 1
    assert(n >= 1)
    if n == 1:
        return Fraction(1, 2)
    else:
        return Fraction(1, (2 + p57_helper(n-1)))

def p58():
    side = 3
    ratio = 1
    #b_right_diag will never be prime!!
    b_left_diag_primes = 0
    t_right_diag_primes = 0
    t_left_diag_primes = 0
    while ratio > 0.10:
        # if side % 99 == 0:
        #     print side
        #b_left
        if isPrime(side**2 - (side - 1)):
            b_left_diag_primes += 1
        #t_left
        if isPrime(side**2 - (2 * (side - 1))):
            t_left_diag_primes += 1
        #t_right
        if isPrime(side**2 - (3 * (side - 1))):
            t_right_diag_primes += 1
        total_primes = b_left_diag_primes + t_right_diag_primes \
                        + t_left_diag_primes
        total_nums = 1 + (4 * (side/2))
        ratio = float(total_primes)/total_nums
        side += 2
    return side - 2 #since it adds side at the end

def p59():
    #I ran this first to figure out what the passcode was
    #then added the part to calculate the answer
    #this section parses the file and returns code as a list with ints
    code = []
    with open("cipher1.txt", "r") as f:
        for line in f:
            code += line.strip().split(",")
    for element in range(len(code)):
        code[element] = int(code[element])
    decode_copy = copy.copy(code)
    plaintext = ""
    decode_i = 0
    char_i = 0
    answer = 0
    #this part generates all possible 3 character lower case passwords
    for i in range(ord("a"), ord("z") + 1):
        for j in range(ord("a"), ord("z") + 1):
            for k in range(ord("a"), ord("z") + 1):
                ascii_vals = [i, j, k]
                #this part decodes the file
                while decode_i < len(code):
                    plaintext += chr(code[decode_i] ^\
                                          ascii_vals[char_i])
                    decode_i += 1
                    char_i = (char_i + 1) % 3
                if "the" in plaintext and "is" in plaintext:
                    print "password is: ", chr(i)+chr(j)+chr(k)
                    print plaintext
                if chr(i)+chr(j)+chr(k) == "god":
                    for q in plaintext:
                        answer += ord(q)
                    return answer
                plaintext = ""
                decode_i = 0
                char_i = 0

def list_n_primes(n):
    result = []
    counter = 2
    while len(result) < n:
        if isPrime(counter):
            result.append(counter)
        counter += 1
    return result

def n_subset_binstring_indices(n, len_list):
    result = []
    biggest_num = 2**(len_list)
    #note, the longest possible bin_string is the length of the list
    for i in xrange(1, biggest_num+1):
        bin_string = int_to_bin_string(i)
        bin_string = "0" * (len_list-len(bin_string)) + bin_string
        a = has_n_ones_indices(n, bin_string)
        if a != None:
            #print(a, bin_string)
            result.append(a)
    return result

def int_to_bin_string(n):
    result = ""
    while n > 0:
        if n % 2 == 0:
            result = "0" + result
        else:
            result = "1" + result
        n //= 2
    return result

# returns a list containing the indices of the n ones in the bin string
# or None if the bin_string does not contain exactly n ones
def has_n_ones_indices(n, bin_string):
    total_ones = 0
    result = []
    for i in range(len(bin_string)):
        if bin_string[i] == "1":
            total_ones += 1
            result.append(i)
    if total_ones == n:
        return result

# assumes you pass in a list of all the possible combinations
# of subsets of size n, then returns a list of all the subsets
# from the list named list of size n
def get_n_subset(n, list):
    result = []
    subset_indices = n_subset_binstring_indices(n, len(list))
    for sublist in subset_indices:
        subset = []
        for i in xrange(len(sublist)):
            subset.append(list[sublist[i]])
        result.append(subset)
    return result

def get_pair_coords(list):
    #this is not the best style since it's hardcoded...
    subsets = []
    for i in range(len(list)-1):
        for j in range(i, len(list)):
            if i != j:
                subsets.append([i, j])
    return subsets

def is_pairwise_concat_prime(list):
    subsets = get_pair_coords(list)
    for subset in subsets:
        print("cur subset", subset)
        first_concat = int(str(list[subset[0]]) + str(list[subset[1]]))
        second_concat = int(str(list[subset[1]]) + str(list[subset[0]]))
        print(first_concat, second_concat)
        if not isPrime(first_concat) or not isPrime(second_concat):
            return False
    return True

#this is general enough to figure out the smallest set of n
#numbers with the desired property, although the efficiency
#is greatly reduced as n increases
def p60(n):
    # start with a list of first n primes
    primes = list_n_primes(n)
    while True: #who knows when to stop...
        highest_prime = primes[-1]
        print(primes, highest_prime)
        n_prime_subsets = get_n_subset(n, primes)
        print("n prime subsets:", n_prime_subsets)
        for prime_subset in n_prime_subsets:
            if is_pairwise_concat_prime(prime_subset):
              return prime_subset
        #otherwise, not possible and need to add one more bigger prime
        next_prime = highest_prime + 2
        while True: #guaranteed to find a prime b/c proof of infinite primes
            if isPrime(next_prime):
                primes.append(next_prime)
                break
            next_prime += 2

# much more simply... wow
def p60b():
    primes = 


def concat_nums(a, b):
    return a * (10 ** getLength(b)) + b

def p62():
    nth_cube = 1
    while True:
        num_perms_cubic = 0
        cube = nth_cube ** 3
        perms = perms_to_ints(cube, permutations(str(cube)))
        if len(perms) > 1:
            print nth_cube, len(perms)
        if len(perms) == 5:
            return nth_cube
        nth_cube += 1

def perms_to_ints(n, perms):
    result = []
    for sublist in perms:
        cur_num = ""
        for num in sublist:
            cur_num += num
        ####this is where you check for is cube!!
        if (getLength(int(cur_num)) == getLength(n) and 
           int(cur_num) not in result and isCube(int(cur_num))):
            result += [int(cur_num)]
    return result

def isCube(n):
    epsilon = 0.0000001
    test = 1 - ((n ** (1.0/3)) % 1)
    return (test == 1) or ((epsilon > test) and (test > -epsilon))

def p63():
    answer = set([])
    #note that 10**n will always be greater than n digits
    #and same for any base larger than 10
    for i in range(1, 10):
    #I sorta guessed on the upper bound for an exponent...
    #no mathematical justification here but observation yields
    #intuition that getLength(i**j) will never catch up to j
    #once you take a look at the printed statements
        for j in range(1, 500):
            #print i, j, getLength(i**j), i**j
            if getLength(i**j) == j:
                answer = answer.union(set([i**j]))
    print answer
    return len(answer)

def p67():
    # tree = [75, 95, 64, 17, 47, 82, 18, 35, 87, 10, 20, 04, 82, 47, 65,
    #         19, 01, 23, 75, 03, 34, 88, 02, 77, 73, 07, 63, 67, 99, 65,
    #         04, 28, 06, 16, 70, 92, 41, 41, 26, 56, 83, 40, 80, 70, 33, 
    #         41, 48, 72, 33, 47, 32, 37, 16, 94, 29, 53, 71, 44, 65, 25, 
    #         43, 91, 52, 97, 51, 14, 70, 11, 33, 28, 77, 73, 17, 78, 39, 
    #         68, 17, 57, 91, 71, 52, 38, 17, 14, 91, 43, 58, 50, 27, 29, 
    #         48, 63, 66, 04, 68, 89, 53, 67, 30, 73, 16, 69, 87, 40, 31,
    #         04, 62, 98, 27, 23, 9, 70, 98, 73, 93, 38, 53, 60, 04, 23]
    tree = parseTriangle()
    tree_length = len(tree)
    #1 and 2 to skip the first element in tree
    cur_index = 1
    height = 2
    cur_spot_in_row = 1
    while cur_index < tree_length:
        #if it's not the leftmost num in a row
        l_p_i = cur_index - height if cur_spot_in_row != 1 else None
        r_p_i = cur_index - height + 1 if cur_spot_in_row != height else None
        l_p = tree[l_p_i] if l_p_i != None else None
        r_p = tree[r_p_i] if r_p_i != None else None
        #add the value of the left parent or right parent, whichever is bigger
        #print tree[cur_index], max(l_p, r_p)
        tree[cur_index] += max(l_p, r_p)
        if height == cur_spot_in_row:
            cur_spot_in_row = 1
            height += 1
        else:
            cur_spot_in_row += 1
        cur_index += 1
    return list_max(tree[tree_length-1-height:tree_length])

def list_max(list):
    if len(list) < 2:
        return list
    else:
        max_elt = list[0]
        for i in range(len(list)):
            if list[i] > max_elt:
                max_elt = list[i]
        return max_elt

def parseTriangle():
    with open("triangle.txt", "r") as f:
        tree = [line.strip().split() for line in f]
    tree = flatten(tree)
    tree = [int(element) for element in tree]
    return tree

def p69(j):
    maximum = 1
    n = 1
    for i in range(2, j+1):
        if i % 10000 == 0:
            print i
        test = float(i)/totient(i)
        if test > maximum:
            maximum = test
            n = i
    return (n, maximum)

#this could certainly be much more efficient...
#as of right now this takes about 5 mins to run... too much
def p70(j):
    answer = 1
    minRatio = 10**7
    for x in xrange(2, j+1):
        if x % 100000 == 0:
            print x
        test = totient(x)
        #print x
        if isPermutation(x, test):
            ratio = x / float(test)
            if ratio < minRatio:
                minRatio = ratio
                answer = x
    return answer

def isPermutation(n, x):
    if getLength(n) == getLength(x):
        string = str(n)
        xString = str(x)
        for char in string:
            i = xString.find(char)
            if i != -1:
                xString = xString[:i] + xString[i+1:]
            else:
                return False
        return xString == ""
    return False

def p78():
    pass
##def p78 in Mathematica:
# num = 2;
# numPartitions = PartitionsP[num];
# While[Mod[numPartitions , 1000000] != 0,
#   If[Mod[num, 500] == 0,
#     Print[num, " ", numPartitions];
#     ]
#    num++;
#   numPartitions = PartitionsP[num];
#   ];
# Print[num];

def nChooseK(n, k):
    return int(float(factorial(n)) / (factorial(k)*factorial(n-k)))

#this is not very efficient, but runs fairly quickly!
#take the printed result, and look at each key. The first set
#will tell you how many elements come before it, so obviously
#if the first set is empty then that key is the first digit.
#following the same logic, you can determine the passcode
def p79():
    logins = []
    with open("keylog.txt", "r") as f:
        for line in f:
            logins += line.strip().split()
    for element in range(len(logins)):
        logins[element] = int(logins[element])
    rules = create_rules_dict(logins)
    for num in logins:
        num_len = getLength(num)
        #iterate over each digit of each num
        for i in range(num_len):
            cur_digit = (num / (10 ** (num_len - 1 - i))) % 10
            #digits that must come before
            #print num, cur_digit, sublist_digits(num, num_len, 0, i), sublist_digits(num, num_len, i+1, num_len)
            rules[cur_digit][0] = \
                rules[cur_digit][0].union(set(sublist_digits(num, num_len, 
                                                            0, i)))
            #digits that must come after
            rules[cur_digit][1] = \
                rules[cur_digit][1].union(set(sublist_digits(num, num_len, 
                                                            i+1, num_len)))
    for key in rules:
        print key, rules[key]


def create_rules_dict(logins):
    rules = dict()
    for num in logins:
        num_len = getLength(num)
        for i in range(num_len):
            cur_digit = (num / (10 ** (num_len - 1 - i))) % 10
            rules[cur_digit] = [set([]), set([])] 
            #first list contains list of numbers that must be before
            #second list contains list of numbers that must be after
    return rules

def sublist_digits(n, num_len, lower, upper):
    #iterates over digits from ones place to tens to hundresds, etc
    #and returns a sublist from the lowerth digit to the upperth digit
    #with upper being exclusive
    assert(0 <= lower and lower <= upper and upper <= getLength(n))
    result = []
    for i in range(lower, upper):
        cur_digit = (n / (10 ** (num_len - 1 - i))) % 10
        result += [cur_digit]
    return result

# def permutations(n):
#     string = str(n)
#     if len(string) == 0:
#         return [[]]
#     else:
#         allPerms = []
#         for subPermutation in permutations(string[1:]):
#             for i in xrange(len(subPermutation) + 1):
#                 allPerms += [subPermutation[:i] + [string[0]] + subPermutation[i:]]
#         return allPerms

def p81():
    """initial testing stuff
    matrix = [[131, 673, 234, 103, 18],
              [201, 96, 342, 965, 150],
              [630, 803, 746, 422, 111],
              [537, 699, 497, 121, 956],
              [805, 732, 524, 37, 331]]
    for sublist in matrix:
        for element in sublist:
            cache[element] = None"""
    #this part parses the matrix.txt file into a 2D array
    matrix = parse_matrix_file()
    #this part makes a cache to store seen positions in the matrix
    #to increase efficiency
    cache = create_matrix_cache(matrix)
    total = matrix[0][0] #top left corner
    answer = p81_helper(matrix, 0, 0, len(matrix)-1, len(matrix[0])-1, cache)
    return answer

def create_matrix_cache(matrix):
    cache = dict()
    for sublist in matrix:
        for element in sublist:
            cache[element] = None
    return cache

def parse_matrix_file():
    matrix = []
    with open("matrix.txt", "r") as f:
        for line in f:
            matrix.append(line.strip().replace('"', '').split(','))
    for sublist in matrix:
        for element in range(len(sublist)):
            sublist[element] = int(sublist[element])
    return matrix

#returns sum of minimal path from any start point x, y in matrix
#to any end_x, end_y point in matrix (as long as only going down and right)
def p81_helper(matrix, x, y, end_x, end_y, cache):
    assert(x <= end_x and y <= end_y)
    if cache[matrix[x][y]] != None:
        #print "yay this happened once!"
        return cache[matrix[x][y]]
    elif x == end_x and y == end_y:
        cache[matrix[x][y]] = matrix[end_x][end_y]
        return matrix[end_x][end_y]
    elif x+1 > end_x:
        #reached the bottom, must go right
        if cache[matrix[x][y+1]] != None:
            #print "cache used for right lookup"
            return matrix[x][y]+cache[matrix[x][y+1]]
        else:
            route_val = p81_helper(matrix, x, y+1, end_x, end_y, cache)
            cache[matrix[x][y+1]] = route_val
            return matrix[x][y]+route_val
    elif y+1 > end_y:
        #reached the right, must go down
        if cache[matrix[x+1][y]] != None:
            #print "cache used for down lookup"
            return matrix[x+1][y]+cache[matrix[x+1][y]]
        else:
            route_val = p81_helper(matrix, x+1, y, end_x, end_y, cache)
            cache[matrix[x+1][y]] = route_val
            return matrix[x][y]+route_val
    else:
        #this part looks to the right
        if cache[matrix[x][y+1]] != None and cache[matrix[x+1][y]] != None:
            #print "cache used in else case"
            return matrix[x][y] + min(cache[matrix[x][y+1]], 
                                      cache[matrix[x+1][y]])
        #this part looks to the right, first checks if it has been visited
        if cache[matrix[x][y+1]] != None:
            #print "cache used for right lookup"
            right_route_val = cache[matrix[x][y+1]]
        else:
            right_route_val = p81_helper(matrix, x, y+1, end_x, end_y, cache)
        #this part looks down, but first checks if it has been visited
        if cache[matrix[x+1][y]] != None:
            #print "cache used for down lookup"
            down_route_val = cache[matrix[x+1][y]]
        else:
            down_route_val = p81_helper(matrix, x+1, y, end_x, end_y, cache)
        #return the minimal path sum
        return matrix[x][y] + min(right_route_val, down_route_val)

#this is supposed to be a faster version of phi... we'll see
def totient(n):
    #this is based on Euler's product formula
    a = getPrimeFactorization(n)
    list_prime_factors = list(a)
    answer = n
    for element in list_prime_factors:
        answer *= (1 - (float(1)/element))
    return int(answer)

def phi(n):
    total = 0
    for k in range(1, n):
        if gcd(k, n) == 1: #they are relatively prime
            total += 1
    return total

def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)

def flatten(a):
    if len(a) == 0:
        return []
    elif type(a[0]) == list:
        return flatten(a[0]) + flatten(a[1:])
    else:
        return [a[0]] + flatten(a[1:])

def p92():
    start_time = time.time()
    total = 0
    for i in range(2, 10000000):
        end = squareDigitChain(i)
        if end == 89:
            total += 1
        # if i % 100000 == 0:
        #     print i
    end_time = time.time()
    print "Took", end_time-start_time, "seconds"
    return total

def squareDigitChain(n):
    while True:
        temp = 0
        num_len = getLength(n)
        for q in range(num_len):
            cur_digit = (n / (10 ** (num_len - 1 - q))) % 10
            temp += cur_digit**2
        #print temp,
        if temp == 1 or temp == 89:
            #print
            return temp
        n = temp

def p214():
    numbers = []
    for i in range(3, 40000000, 2):
        #if i % 3333 == 0:
            #print i
        if isPrime(i):
            num_terms = 1
            cur_term = i
            while cur_term != 1 and num_terms < 27:
                cur_term = phi(cur_term)
                num_terms += 1
            if num_terms == 25:
                numbers.append(i)
    return sum(numbers)

def p432(n, m):
    answer = 0
    for i in range(1, m + 1):
        if i % 100000 == 0:
            print i
        answer += totient(n * i)
        answer %= 10**9
    return answer

def p448(n, j=999999017):
    total = 0
    for k in range(1, n+1):
        if k % 10000 == 0:
          print(k)
        total += (A(k) % j)
    return total % j

def A(n):
    result = 1 if n == 1 else 2*n #accounts for lcm(n, 1) and lcm(n, n)
    for i in range(2, n):
        result += lcm(n, i)
    return result/n

def lcm(a, b):
    return int(float(a*b)/gcd(a,b))