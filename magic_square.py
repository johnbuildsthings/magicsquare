    
class MagicSquare(object):
    """MagicSquare takes an odd number as size and a rule that has a 
    start move and else statement in the form start..., move..., else...
    and builds a square with the provide size and rule"""
    def __init__(self, rule, size):
        self.size = size
        self.rule = rule
        
        
    def square(self, size):
        """initiates a square of 0's with size size as a list of lists
        that can be operated on by the other functions"""
        b = [['0' for count in range(self.size)] for count in range(self.size)]
        
        return b
        
    def disRule(self, rule):
        """disRule (disassemble rule) breaks the rule into three parts...
        the start condition... the movement condition... else condition"""
        RList = rule.split(',')
        start = RList[0].split()
        start.remove('start')
        move = RList[1].split()
        move.remove('move')
        move.remove('and')
        other = RList[2].split()
        other.remove('else')
        """
        print 's', start
        print 'm', move
        print 'e', other
        """
        return start, move, other
        
    def upOrLeft(self, index):
        """moves up or left depending on which index is supplied...
        up for indexY left for indexX"""
        if index - 1 < 0:
            return self.size-1
        else:
            return index - 1
    
    def downOrRight(self, index):
        """moves down or to the right depending on which index is 
        supplied... down for indexY right for indexX"""
        if index + 1 >= self.size:
            return 0
        else:
            return index + 1 
            
    def Else(self, index, Else):
        
        if 'up' in Else or 'left' in Else:
            return self.upOrLeft(index)
        else:
            return self.downOrRight(index)
            
    def move(self, indexY):
        """move controls all the movements that are set forth in the
        rule... indexY represents which list in the 'list of lists' 
        to start with"""
        counter = 1
        mgSquare = self.square(self.size)
        
        mgRule = self.disRule(self.rule)
        Move = mgRule[1]
        Else = mgRule[2]
        
        middle = (int(self.size/2))
        indexX = middle
        self.replace(mgSquare[indexY], middle, counter)
        
        for i in range(self.size**2-1):
            
            if 'up' in Move:
                """this condition is met if the rule tells you to move up
                in the 'move' part of the rule"""
                indexY = self.upOrLeft(indexY)
                if 'left' in Move:
                    """this condition is met if the rule tells you to move up
                    and left in the 'move' part of the rule"""
                    counter += 1
                    indexX = self.upOrLeft(indexX)
                    if mgSquare[indexY][indexX] != '0':
                        indexY = self.downOrRight(indexY)
                        indexX = self.downOrRitht(indexX)
                        indexY = self.Else(indexY, Else)
                    self.replace(mgSquare[indexY], indexX, counter)
                else:
                    """this condition is met if the rule tells you to move up
                    and right in the 'move' part of the rule"""
                    counter += 1
                    indexX = self.downOrRight(indexX)
                    if mgSquare[indexY][indexX] != '0':
                        indexY = self.downOrRight(indexY)
                        indexX = self.upOrLeft(indexX)
                        indexY = self.Else(indexY, Else)
                    self.replace(mgSquare[indexY], indexX, counter)
                 
            else:
                """this condition is met if the rule tells you to move down
                in the 'move' part of the rule"""
                indexY = self.downOrRight(indexY)
                
                if 'left' in Move:
                    """this condition is met if the rule tells you to move down
                    and left in the 'move' part of the rule"""
                    counter += 1
                    indexX = self.upOrLeft(indexX)
                    if mgSquare[indexY][indexX] != '0':
                        indexY = self.upOrLeft(indexY)
                        indexX = self.downOrRitht(indexX)
                        indexY = self.Else(indexY, Else)
                    self.replace(mgSquare[indexY], indexX, counter)
                
                else:
                    """this condition is met if the rule tells you to move down
                    and right in the 'move' part of the rule"""
                    counter += 1
                    indexX = self.downOrRight(indexX)
                    if mgSquare[indexY][indexX] != '0':
                        indexY = self.upOrLeft(indexY)
                        indexX = self.upOrLeft(indexX)
                        indexY = self.Else(indexY, Else)
                    self.replace(mgSquare[indexY], indexX, counter)
                    
        return mgSquare
        
        
    def replace(self, List, element, replacement):
        """replace is used to replace to initial 0 (i.e.element)
        in the List to whatever the replacement arg is"""
        replacement = str(replacement)
        if self.size > 9:
            offset = 3
            replacement = replacement.rjust(offset)
           
        elif self.size > 3:
            offset = 2 
            replacement = replacement.rjust(offset)
        List.pop(element)
        List.insert(element, replacement)
        
        
    def buildMagicSq(self):
        
        mgSquare = self.square(self.size)
        mgRule = self.disRule(self.rule)
        Start = mgRule[0]
        middle = (int(self.size/2))
        
        
        if 'top' in Start:
            '''start on top row center'''
            mgSquare = self.move(0)
            self.draw(mgSquare)
            ##print "is magic square: ", self.is_magicSquare(mgSquare)[0]
            print "sum of rows and columns is ", self.is_magic_square(mgSquare)[1]
            
        elif 'bottom' in Start:
            '''start on bottom row center'''
            mgSquare = self.move(self.size-1)           
            self.draw(mgSquare)
            ##print "is magic square: ", self.is_magicSquare(mgSquare)[0]
            print "sum of rows and columns is ", self.is_magic_square(mgSquare)[1]
            
        else:
            '''start in the middle row'''
            mgSquare = self.move(middle)
            self.draw(mgSquare)
            ##print "is magic square: ", self.is_magicSquare(mgSquare)[0]
            print "sum of rows and columns is ", self.is_magic_square(mgSquare)[1]

    def draw(self, square):
        """draw builds the visual representation of the list of lists
        as a nice square"""
        for i in range(self.size):
            print "  ".join(square[i])
          
    def add(self, List):
        result = 0
        for n in List:
            result += int(n)
        return result
        
    def is_magic_square(self, square):
        """tests to see if the sum of each of each row is equal 
        to the sum of each row and column"""
        tests = []
        total = self.add(square[0])
        
        for i in square:
            result = self.add(i)
            tests.append(total == result)
        for i in range(0, self.size):
            result = 0
            for n in range(0, self.size):
                ##print square[n][i]
                result += int(square[n][i])
            tests.append(total == result)
        ##print "Sum of rows and columns is ", total
        return False not in tests, total
        
                
            
t = MagicSquare('start bottom, move down and right, else down', 3)
f = MagicSquare('start bottom, move down and right, else up',11)
t.buildMagicSq()

print " "
f.buildMagicSq()
##print f.is_magic_square()