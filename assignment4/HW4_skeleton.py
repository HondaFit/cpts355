#------------------------- 10% -------------------------------------
# The operand stack: define the operand stack and its operations
opstack = [] #assuming top of the stack is the end of the list

# Now define the helper functions to push and pop values on the opstack 
# (i.e, add/remove elements to/from the end of the Python list)
# Remember that there is a Postscript operator called "pop" so we choose 
# different names for these functions.
def opPop():
    if len(opstack) > 0:
        return opstack.pop()
    else:
        print("Error: opstack is empty")

# opPop should return the popped value.
# The pop() function should call opPop to pop the top value from the opstack, 
# but it will ignore the popped value.
def opPush(value):
    opstack.append(value)

#-------------------------- 20% -------------------------------------
# The dictionary stack: define the dictionary stack and its operations
dictstack = [] #assuming top of the stack is the end of the list

# now define functions to push and pop dictionaries on the dictstack, to
# define name, and to lookup a name
def dictPop():
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        print("Error: dictstack is empty")

# dictPop pops the top dictionary from the dictionary stack.
def dictPush(d):
    dictstack.append(d)

#dictPush pushes the dictionary 'd' to the dictstack. 
#Note that, your interpreter will call dictPush only when Postscript
#"begin" operator is called. "begin" should pop the empty dictionary from 
#the opstack and push it onto the dictstack by calling dictPush.
def define(name, value):
    if len(dictstack) == 0:
        newDict = dict()
        newDict[name] = value
        dictstack.append(newDict)
    else:
        dictstack[-1][name] = value

#add name:value pair to the top dictionary in the dictionary stack.
#Keep the '/' in the name constant.
#Your psDef function should pop the name and value from operand stack and 
#call the "define" function.
def lookup(name):
    if not name.startswith("/"):
        name = "/" + name
    for d in reversed(dictstack):
        if name in d:
            value = d[name]
            return value
    print(f"Error: name {name} not found in dictstack")
    return None


# return the value associated with name
# What is your design decision about what to do when there is no definition for "name"? 
# If "name" is not defined, your program should not break, but should give an appropriate error message.

#--------------------------- 10% ------------------------------------- 
# Arithmetic and comparison operators: add, sub, mul, div, mod, eq, lt, gt
# Make sure to check the operand stack has the correct number of parameters 
# and types of the parameters are correct.
def add():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            opPush(op1 + op2)
        else:
            print("Error: add expects two numeric operands")
            opPush(op2)
            opPush(op1)
    else: 
        print("Error: add expects two operands")

def sub():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()  
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op2 - op1)
        else:
            print("Error: sub expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: sub expects two operands")

def mul():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op1 * op2)
        else:
            print("Error: mul expects two integer operands") 
            opPush(op2)
            opPush(op1)
    else:
        print("Error: mul expects two operands")

def div():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1,int) and isinstance(op2,int):
            if op1 != 0:
                opPush(op2 // op1)
            else:
                print("Error: divide by zero")
                opPush(op2)
                opPush(op1)                
        else:
            print("Error: div expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:        
        print("Error: div expects two operands")

def mod():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op1 != 0:
                opPush(op2 % op1)
            else:
                print("Error: mod by zero")
                opPush(op2)
                opPush(op1)
        else:
            print("Error: mod expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: mod expects two operands")

def eq():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if op1 == op2:
            opPush(True)
        else:
            opPush(False)
    else:
        print("Error: eq expects two operands")

def lt():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 < op1:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: lt expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: lt expects two operands")
        
def gt():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 > op1:
                opPush(True)
            else:
                opPush(False)
        else:
            print("Error: gt expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        print("Error: gt expects two operands")

#--------------------------- 15% ------------------------------------- 
# String operators: define the string operators length, get, getinterval, put 
def length():
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, str):
            opPush(len(op) - 2)
        else:
            print("Error: length expects a string operand")
            opPush(op)
    else:
        print("Error: length expects one operand")
        
def get():
    if len(opstack) > 1:
        index = opPop()
        string = opPop()
        if isinstance(index, int) and isinstance(string, str) and index >= 0 and index < len(string) - 2:
            opPush(ord(string[index + 1]))
        else:
            print("Error: get expects a string and an integer within bounds")
            opPush(string)
            opPush(index)
    else:
        print("Error: get expects two operands")

def getinterval():
    if len(opstack) > 2:
        count = opPop()
        index = opPop()
        string = opPop()
        if isinstance(count, int) and isinstance(index, int) and isinstance(string, str) and index >= 0 and count >= 0 and (index + count) <= len(string) - 2:
            opPush('(' + string[index + 1 : index + count + 1] + ')')
        else:
            print("Error: getinterval expects a string and two integers within bounds")
            opPush(string)
            opPush(index)
            opPush(count)
    else:
        print("Error: getinterval expects three operands")
        
        
def put():
    if len(opstack) > 2:
        ascii_val = opPop()
        index = opPop()
        string = opPop()
        if isinstance(ascii_val, int) and isinstance(index, int) and isinstance(string, str) and index >= 0 and index < len(string) - 2 and ascii_val >= 0 and ascii_val <= 127:
            new_string = string[:index + 1] + chr(ascii_val) + string[index + 2:]
            opPush(new_string)
        else:
            print("Error: put expects a string, an integer index within bounds, and an integer ASCII value")
            opPush(string)
            opPush(index)
            opPush(ascii_val)
    else:
        print("Error: put expects three operands")

#--------------------------- 25% ------------------------------------- 
# Define the stack manipulation and print operators: dup, copy, pop, clear, exch, roll, stack
def dup():
    if len(opstack) > 0:
        opPush(opstack[-1])
    else:
        print("Error: dup expects at least one operand")

def copy():
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, int) and op > 0:
            if len(opstack) >= op:
                opstack.extend(opstack[-op:]) 
            else:
                print("Error: copy exceeds size of stack")
                opstack.append(op)
        else:
            print("Error: copy expects a positive int operand")
            opPush(op)
    else:
        print("Error: copy expects one operand")

def pop():
    if len(opstack) > 0:
        opPop() 
    else:
        print("Error: pop expects at least one operand")  

def clear():
    opstack.clear()

def exch():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        print("Error: exch expects at least two operands")

def roll():
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 > 0 and op2 <= len(opstack) and op1 != 0: 
                rollpart = opstack[-op2:]
                del opstack[-op2:]
                if op1 > 0: 
                    for i in range(op1):
                        rollpart.insert(0,rollpart.pop())
                else:
                    for i in range(-op1):
                        rollpart.append(rollpart.pop(0))
                opstack.extend(rollpart)
            else:
                print("Error: roll indices out of bounds or top index 0")
                opPush(op2)
                opPush(op1)
        else:
            print("Error: roll expects two int operands")
            opPush(op2)            
            opPush(op1)
    else:
        print("Error: roll expects at least two operands")
  
def stack():
    if len(opstack) > 0:
        for item in reversed(opstack):
            print(item)
    else:
        print("stack is empty")


#--------------------------- 20% -------------------------------------
# Define the dictionary manipulation operators: psDict, begin, end, psDef
# name the function for the def operator psDef because def is reserved in Python. 
# Similarly, call the function for dict operator as psDict.
# Note: The psDef operator will pop the value and name from the opstack and call your own "define" operator 
# (pass those values as parameters). 
# Note that psDef() won't have any parameters.
def psDict():
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, int):
            opPush(dict())
        else:
            print("Error: dict expects an int operand")
            opPush(op)
    else:
        print("Error: dict expects one operand")

def begin():
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, dict):
            dictPush(op)
        else:
            print("Error: begin expects a dict operand")
            opPush(op)
    else:
        print("Error: begin expects one operand")

def end():
    if len(dictstack) > 0:
        dictPop()
    else:
        print("Error: dictstack is empty")
        
def psDef():
    if len(opstack) > 1:
        value = opPop()
        name = opPop()
        if isinstance(name, str) and name.startswith('/'):
            define(name, value)
        else:
            print("Error: def expects a name starting with '/' and a value")
            opPush(name)
            opPush(value)
    else:
        print("Error: def expects two operands")