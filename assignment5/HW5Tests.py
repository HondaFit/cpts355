import re

opstack = []


def opPop():
    #Removes and returns the top value from the operand stack
    #Returns None if the operand stack is empty
    if len(opstack) > 0:
        return opstack.pop()
    else:
        # print("Error: opstack is empty")
        pass


def opPush(value):
    #Pushes the given value onto the top of the operand stack
    opstack.append(value)


dictstack = []


def dictPop():
    #Removes and returns the top dict from the dict stack
    #Returns None if the dict stack is empty
    if len(dictstack) > 0:
        return dictstack.pop()
    else:
        # print("Error: dictstack is empty")
        pass


def dictPush(d):
    #Pushes the given dict d onto the top of the dict stack
    dictstack.append(d)


def define(name, value):
    #Adds a name:value pair to the top dict on the dict stack
    #Creates a new dict if no dictionaries are on the stack
    if len(dictstack) == 0:
        newDict = dict()
        newDict[name] = value
        dictstack.append(newDict)
    else:
        dictstack[-1][name] = value


def lookup(name):
    #Searches the dictstack in LIFO order for the given name
    #Returns the value associated with name or None if not found
    if not name.startswith("/"):
        name = "/" + name
    for d in reversed(dictstack):
        if name in d:
            value = d[name]
            return value
        # print(f"Error: name {name} not found in dictstack")
    return None


def add():
    #Pops two numeric operands, adds them, and pushes the result
    #Leaves operands on stack if an error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, (int, float)) and isinstance(op2, (int, float)):
            opPush(op1 + op2)
        else:
            # print("Error: add expects two numeric operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: add expects two operands")
        pass


def sub():
    #Pops two integer operands, subtracts them, and pushes the result
    #Leaves operands on stack if an error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()

        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op2 - op1)
        else:
            # print("Error: sub expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: sub expects two operands")
        pass


def mul():
    #Pops two integer operands, multiplies them, and pushes the result
    #Leaves operands on stack if an error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            opPush(op1 * op2)
        else:
            # print("Error: mul expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: mul expects two operands")
        pass


def div():
    #Pops two integer operands, divides them, and pushes the integer result
    #Leaves operands on stack if an error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op1 != 0:
                opPush(op2 // op1)
            else:
                # print("Error: divide by zero")
                opPush(op2)
                opPush(op1)
        else:
            # print("Error: div expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: div expects two operands")
        pass


def mod():
    #Pops two integer operands, calculates the modulus, and pushes the result
    #Leaves operands on stack if an error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op1 != 0:
                opPush(op2 % op1)
            else:
                # print("Error: mod by zero")
                opPush(op2)
                opPush(op1)
        else:
            # print("Error: mod expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: mod expects two operands")
        pass


def eq():
    #Pops two operands, pushes True if they are equal, False otherwise
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if op1 == op2:
            opPush(True)
        else:
            opPush(False)
    else:
        # print("Error: eq expects two operands")
        pass


def lt():
    #Pops two integer operands, pushes True if op2 is less than op1
    #Pushes False otherwise. Leaves operands on stack if error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 < op1:
                opPush(True)
            else:
                opPush(False)
        else:
            # print("Error: lt expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: lt expects two operands")
        pass


def gt():
    #Pops two integer operands, pushes True if op2 is greater than op1
    #Pushes False otherwise. Leaves operands on stack if error occurs
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 > op1:
                opPush(True)
            else:
                opPush(False)
        else:
            # print("Error: gt expects two integer operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: gt expects two operands")
        pass


def length():
    #Pops string and pushes its length (not counting the enclosing parentheses)
    #Pushes the original value back on the stack if an error occurs
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, str):
            opPush(len(op) - 2)
        else:
            # print("Error: length expects a string operand")
            opPush(op)
    else:
        # print("Error: length expects one operand")
        pass

def get():
    #Pops a string and an index, pushes the ASCII value of the char at that index
    #Pushes the original values back on the stack if an error occurs
    if len(opstack) > 1:
        index = opPop()
        string = opPop()
        if (
            isinstance(index, int)
            and isinstance(string, str)
            and index >= 0
            and index < len(string) - 2
        ):
            opPush(ord(string[index + 1]))
        else:
            # print("Error: get expects a string and an integer within bounds")
            opPush(string)
            opPush(index)
    else:
        # print("Error: get expects two operands")
        pass


def getinterval():
    #Pops a string, start index, and count, and pushes the substring from start to start+count
    #Pushes the original values back on the stack if an error occurs
    if len(opstack) > 2:
        count = opPop()
        index = opPop()
        string = opPop()
        if (
            isinstance(count, int)
            and isinstance(index, int)
            and isinstance(string, str)
            and index >= 0
            and count >= 0
            and (index + count) <= len(string) - 2
        ):
            opPush("(" + string[index + 1 : index + count + 1] + ")")
        else:
            # print("Error: getinterval expects a string and two integers within bounds")
            opPush(string)
            opPush(index)
            opPush(count)
    else:
        # print("Error: getinterval expects three operands")
        pass


def put():
    #Pops a string, index, and ASCII value, and replaces the char at index with the char having the ASCII value
    #Pushes the resulting string. Pushes the original values back on the stack if an error occurs
    if len(opstack) > 2:
        ascii_val = opPop()
        index = opPop()
        string = opPop()
        if (
            isinstance(ascii_val, int)
            and isinstance(index, int)
            and isinstance(string, str)
            and index >= 0
            and index < len(string) - 2
            and ascii_val >= 0
            and ascii_val <= 127
        ):
            new_string = string[: index + 1] + chr(ascii_val) + string[index + 2 :]
            opPush(new_string)
        else:
            #print("Error: put expects a string, an integer index within bounds, and an integer ASCII value")
            opPush(string)
            opPush(index)
            opPush(ascii_val)
    else:
        #print("Error: put expects three operands")
        pass


def dup():
    #Duplicates the top value on the operand stack
    #Does nothing if the operand stack is empty
    if len(opstack) > 0:
        opPush(opstack[-1])
    else:
        # print("Error: dup expects at least one operand")
        pass


def copy():
    #Pops the top value on the stack and pushes that many copies of the next value onto the stack.
    #If there are not enough elements on the stack, it leaves the stack unchanged.
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, int) and op > 0:
            if len(opstack) >= op:
                opstack.extend(opstack[-op:])
            else:
                # print("Error: copy exceeds size of stack")
                opstack.append(op)
        else:
            # print("Error: copy expects a positive int operand")
            opPush(op)
    else:
        # print("Error: copy expects one operand")
        pass


def pop():
    #Pops and discards the top value on the operand stack
    #Does nothing if the operand stack is empty
    if len(opstack) > 0:
        opPop()
    else:
        # print("Error: pop expects at least one operand")
        pass


def clear():
    #Clears all elements from the operand stack
    opstack.clear()


def exch():
    #Exchanges the top two elements on the operand stack
    #Does nothing if there are fewer than 2 elements on the stack
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        opPush(op1)
        opPush(op2)
    else:
        # print("Error: exch expects at least two operands")
        pass


def roll():
    #Pops two integer operands: i and n. Rolls the top n stack elements i positions forward/backward (depending on the sign of i)
    #Does nothing if there are not at least n+2 elements on the stack or abs(i) > n
    if len(opstack) > 1:
        op1 = opPop()
        op2 = opPop()
        if isinstance(op1, int) and isinstance(op2, int):
            if op2 > 0 and op2 <= len(opstack) and op1 != 0:
                rollpart = opstack[-op2:]
                del opstack[-op2:]
                if op1 > 0:
                    for i in range(op1):
                        rollpart.insert(0, rollpart.pop())
                else:
                    for i in range(-op1):
                        rollpart.append(rollpart.pop(0))
                opstack.extend(rollpart)
            else:
                # print("Error: roll indices out of bounds or top index 0")
                opPush(op2)
                opPush(op1)
        else:
            # print("Error: roll expects two int operands")
            opPush(op2)
            opPush(op1)
    else:
        # print("Error: roll expects at least two operands")
        pass


def stack():
    #Prints the contents of the operand stack, from top to bottom, without modifying the stack
    #Prints a message if the stack is empty
    if len(opstack) > 0:
        for item in reversed(opstack):
            print(item)
    else:
        # print("stack is empty")
        pass


def psDict():
    #Pops a size argument, creates a new dict of that size, and pushes it on the operand stack
    #Pushes the original value back on the stack if an error occurs
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, int):
            opPush(dict())
        else:
            # print("Error: dict expects an int operand")
            opPush(op)
    else:
        # print("Error: dict expects one operand")
        pass


def begin():
    #Pops a dict from the operand stack and pushes it onto the dict stack
    #Pushes the original value back on the stack if an error occurs
    if len(opstack) > 0:
        op = opPop()
        if isinstance(op, dict):
            dictPush(op)
        else:
            # print("Error: begin expects a dict operand")
            opPush(op)
    else:
        # print("Error: begin expects one operand")
        pass


def end():
    #Pops the top dict off the dict stack and discards it.
    #Does nothing if the dict stack is empty.
    if len(dictstack) > 0:
        dictPop()
    else:
        # print("Error: dictstack is empty")
        pass


def psDef():
    #Pops a name and a value, and associates them in the top dictionary on the dict stack
    #Leaves the name and value on the stack if an error occurs
    if len(opstack) > 1:
        value = opPop()
        name = opPop()
        if isinstance(name, str) and name.startswith("/"):
            define(name, value)
        else:
            # print("Error: def expects a name starting with '/' and a value")
            opPush(name)
            opPush(value)
    else:
        # print("Error: def expects two operands")
        pass




##############################################################################################################################
def tokenize(s):
    return re.findall("/?[a-zA-Z()][a-zA-Z0-9_()]*|[-]?[0-9]+|[}{]+|%.*|[^\t\n ]", s)

def groupMatching2(it):
    res = []
    for c in it:
        if c == '}':
            return res
        elif c=='{':
            res.append(groupMatching2(it))
        else:
            res.append(c)
    return False

def parse(L):
    res = []
    it = iter(L)
    for c in it:
        if c == '}':
            return res
        elif c == '{':
            res.append(parse(it))
        elif c.isdigit():
            res.append(int(c))
        elif c == "true":
            res.append(True)
        elif c == "false":
            res.append(False)
        else:
            res.append(c)
    return res
# Update your put function from HW4 based on the new requirements
def put():
    if len(opstack) > 2:
        ascii_val = opPop()
        index = opPop()
        string = opPop()
        if (
            isinstance(ascii_val, int)
            and isinstance(index, int)
            and isinstance(string, str)
            and index >= 0
            and index < len(string) - 2
            and ascii_val >= 0
            and ascii_val <= 127
        ):
            new_string = string[: index + 1] + chr(ascii_val) + string[index + 2 :]
            # Update all references to the original string in opstack and dictstack
            for i in range(len(opstack)):
                if id(opstack[i]) == id(string):
                    opstack[i] = new_string
            for i in range(len(dictstack)):
                for key in dictstack[i]:
                    if id(dictstack[i][key]) == id(string):
                        dictstack[i][key] = new_string
            opPush(new_string)
        else:
            opPush(string)
            opPush(index)
            opPush(ascii_val)
    else:
        pass

# Implement the psIf function
def psIf():
    if len(opstack) > 1:
        cond = opPop()
        code = opPop()
        if isinstance(cond, bool) and isinstance(code, list):
            if cond:
                interpretSPS(code)
        else:
            opPush(code)
            opPush(cond)
    else:
        pass

# Implement the psIfelse function
def psIfelse():
    if len(opstack) > 2:
        else_code = opPop()
        then_code = opPop()
        cond = opPop()
        if isinstance(cond, bool) and isinstance(then_code, list) and isinstance(else_code, list):
            if cond:
                interpretSPS(then_code)
            else:
                interpretSPS(else_code)
        else:
            opPush(cond)
            opPush(then_code)
            opPush(else_code)
    else:
        pass

# Implement the psFor function
def psFor():
    if len(opstack) > 3:
        code = opPop()
        end = opPop()
        incr = opPop()
        start = opPop()
        if isinstance(start, int) and isinstance(incr, int) and isinstance(end, int) and isinstance(code, list):
            for i in range(start, end+1, incr):
                opPush(i)
                interpretSPS(code)
        else:
            opPush(start)
            opPush(incr)
            opPush(end)
            opPush(code)
    else:
        pass

# Implement the interpreter function
def interpreter(s): # s is a string
    interpretSPS(parse(tokenize(s)))

# Implement the interpretSPS function
binOp = {
    'add': add,
    'sub': sub,
    'mul': mul,
    'div': div,
    'eq': eq,
    'lt': lt,
    'gt': gt
}
def interpretSPS(code):  # code is a code array
    for token in code:
        if isinstance(token, (int, float, bool, list)):
            opPush(token)
        elif isinstance(token, str):
            if token == "add":
                add()
            elif token == "sub":
                sub()
            elif token == "mul":
                mul()
            elif token == "div":
                div()
            elif token == "mod":
                mod()
            elif token == "eq":
                eq()
            elif token == "lt":
                lt()
            elif token == "gt":
                gt()
            elif token == "length":
                length()
            elif token == "get":
                get()
            elif token == "getinterval":
                getinterval()
            elif token == "put":
                put()
            elif token == "dup":
                dup()
            elif token == "copy":
                copy()
            elif token == "pop":
                pop()
            elif token == "clear":
                clear()
            elif token == "exch":
                exch()
            elif token == "roll":
                roll()
            elif token == "stack":
                stack()
            elif token == "dict":
                psDict()
            elif token == "begin":
                begin()
            elif token == "end":
                end()
            elif token == "def":
                psDef()
            elif token == "if":
                psIf()
            elif token == "ifelse":
                psIfelse()
            elif token == "for":
                psFor()
            else:
                if token.startswith('/'):
                    opPush(token)
                else:
                    value = lookup(token)
                    if value is None:
                        print(f"{token}")
                    else:
                        if isinstance(value, list):
                            interpretSPS(value)
                        else:
                            opPush(value)
        else:
            print(f"Error: Unexpected token '{token}'")


##############################################################################################################################

input1 = """
        /square {
            dup mul
        } def
        (square)
        4 square
        dup 16 eq
        {(pass)} {(fail)} ifelse
        stack
        """

input2 ="""
    (facto) dup length /n exch def
    /fact {
        0 dict begin
        /n exch def
        n 2 lt
        { 1}
        {n 1 sub fact n mul }
        ifelse
        end
    } def
    n fact stack
    """

input3 = """
        /fact{
        0 dict
                begin
                        /n exch def
                        1
                        n -1 1 {mul} for
                end
        } def
        6
        fact
        stack
    """

input4 = """
        /lt6 { 6 lt } def
        1 2 3 4 5 6 4 -3 roll
        dup dup lt6 {mul mul mul} if
        stack
        clear
    """

input5 = """
        (CptS355_HW5) 4 3 getinterval
        (355) eq
        {(You_are_in_CptS355)} if
        stack
        """

input6 = """
        /pow2 {/n exch def
            (pow2_of_n_is) dup 8 n 48 add put
                1 n -1 1 {pop 2 mul} for
            } def
        (Calculating_pow2_of_9) dup 20 get 48 sub pow2
        stack
        """
#comparing in assignment before actual results. Everything has passed
print(tokenize(input1))
print(parse(tokenize(input1)))
print()
print(tokenize(input2))
print(parse(tokenize(input2)) )
print()
print(tokenize(input3))
print(parse(tokenize(input3)))
print()
print(tokenize(input4))
print(parse(tokenize(input4)) )
print()
print(tokenize(input5))
print(parse(tokenize(input5)) )
print()
print(tokenize(input6))
print(parse(tokenize(input6)) )

print()
print()


#clear opstack and dictstack
def clear():
    del opstack[:]
    del dictstack[:]
    
    
    
print(interpreter(input1))
clear()

print(interpreter(input2))
clear()

print(interpreter(input3))
clear()

print(interpreter(input4))
clear()

print(interpreter(input6))
clear()


