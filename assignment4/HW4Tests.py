import sys
import io
import unittest
from HW4 import *

class HW4Tests(unittest.TestCase):
    def setUp(self):
        pass
    
    
           
#-------------------------------------------------------------------------# 
#Testing push pop using different types
#testing pop from empty stack
 
    def testOpPushString(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[-1], "(Hello)")

    def testOpPushInteger(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1], 5)

    def testOpPopString(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opPop(), "(Hello)")

    def testOpPopInteger(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(), 5)

    def testOpPopEmpty(self):
        opstack.clear()
        self.assertIsNone(opPop())
        
#-------------------------------------------------------------------------#  
#test push pop dict 
#test pop from empty dict  
    
    def testDictPush(self):
        dictstack.clear()
        sample_dict = {"/a": 1, "/b": 2}
        dictPush(sample_dict)
        self.assertDictEqual(dictstack[-1], sample_dict)

    def testDictPop(self):
        dictstack.clear()
        sample_dict = {"/x": 10, "/y": 20}
        dictPush(sample_dict)
        popped_dict = dictPop()
        self.assertDictEqual(popped_dict, sample_dict)
        self.assertEqual(len(dictstack), 0)

    def testDictPopEmpty(self):
        dictstack.clear()
        popped_dict = dictPop()
        self.assertIsNone(popped_dict)
        self.assertEqual(len(dictstack), 0)
        
#-------------------------------------------------------------------------#   
#test define and lookup value
#test lookup with undefined value 
 
    def testDefine(self):
        dictstack.clear()
        define("/myvariable", 42)
        self.assertEqual(len(dictstack), 1)
        self.assertIn("/myvariable", dictstack[-1])
        self.assertEqual(dictstack[-1]["/myvariable"], 42)

    def testLookupUndefined(self):
        dictstack.clear()
        value = lookup("undefined_variable")
        self.assertIsNone(value)
        self.assertEqual(len(dictstack), 0)


#-------------------------------------------------------------------------#    
#test each operant with valid operand
#test eac operator with invalid operand
#test each operator with insufficient operand 

    def testAddValid(self):
        opstack.clear()
        opPush(5)
        opPush(3.14)
        add()
        self.assertAlmostEqual(opPop(), 8.14)

    def testAddInvalid(self):
        opstack.clear()
        opPush(5)
        opPush("(invalid)")
        add()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 5)

    def testAddInsufficient(self):
        opstack.clear()
        opPush(5)
        add()
        self.assertEqual(opPop(), 5)

    def testSubValid(self):
        opstack.clear()
        opPush(10)
        opPush(7)
        sub()
        self.assertEqual(opPop(), 3)

    def testSubInvalid(self):
        opstack.clear()
        opPush(10)
        opPush("(invalid)")
        sub()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 10)

    def testSubInsufficient(self):
        opstack.clear()
        opPush(10)
        sub()
        self.assertEqual(opPop(), 10)

    def testMulValid(self):
        opstack.clear()
        opPush(4)
        opPush(6)
        mul()
        self.assertEqual(opPop(), 24)

    def testMulInvalid(self):
        opstack.clear()
        opPush(4)
        opPush("(invalid)")
        mul()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 4)

    def testMulInsufficient(self):
        opstack.clear()
        opPush(4)
        mul()
        self.assertEqual(opPop(), 4)

    def testDivValid(self):
        opstack.clear()
        opPush(10)
        opPush(4)
        div()
        self.assertEqual(opPop(), 2)

    def testDivInvalid(self):
        opstack.clear()
        opPush(10)
        opPush("(invalid)")
        div()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 10)

    def testDivInsufficient(self):
        opstack.clear()
        opPush(10)
        div()
        self.assertEqual(opPop(), 10)

    def testModValid(self):
        opstack.clear()
        opPush(10)
        opPush(3)
        mod()
        self.assertEqual(opPop(), 1)

    def testModInvalid(self):
        opstack.clear()
        opPush(10)
        opPush("(invalid)")
        mod()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 10)

    def testModInsufficient(self):
        opstack.clear()
        opPush(10)
        mod()
        self.assertEqual(opPop(), 10)

    def testEqValid(self):
        opstack.clear()
        opPush(5)
        opPush(5)
        eq()
        self.assertTrue(opPop())

    def testEqInvalid(self):
        opstack.clear()
        opPush(5)
        opPush("(invalid)")
        eq()
        self.assertFalse(opPop())

    def testEqInsufficient(self):
        opstack.clear()
        opPush(5)
        eq()
        self.assertEqual(opPop(), 5)

    def testLtValid(self):
        opstack.clear()
        opPush(3)
        opPush(5)
        lt()
        self.assertTrue(opPop())

    def testLtInvalid(self):
        opstack.clear()
        opPush(3)
        opPush("(invalid)")
        lt()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 3)

    def testLtInsufficient(self):
        opstack.clear()
        opPush(3)
        lt()
        self.assertEqual(opPop(), 3)

    def testGtValid(self):
        opstack.clear()
        opPush(5)
        opPush(3)
        gt()
        self.assertTrue(opPop())

    def testGtInvalid(self):
        opstack.clear()
        opPush(5)
        opPush("(invalid)")
        gt()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 5)

    def testGtInsufficient(self):
        opstack.clear()
        opPush(5)
        gt()
        self.assertEqual(opPop(), 5)



#-------------------------------------------------------------------------#    
#test each operant with valid operand
#test eac operator with invalid operand
#test each operator with insufficient operand 

    def testLengthValid(self):
        opstack.clear()
        opPush("(Hello, World!)")
        length()
        self.assertEqual(opPop(), 13)

    def testLengthInvalid(self):
        opstack.clear()
        opPush(42)
        length()
        self.assertEqual(opPop(), 42)

    def testLengthInsufficient(self):
        opstack.clear()
        length()
        self.assertEqual(len(opstack), 0)

    def testGetValid(self):
        opstack.clear()
        opPush("(Python)")
        opPush(2)
        get()
        self.assertEqual(opPop(), ord('t'))

    def testGetInvalid(self):
        opstack.clear()
        opPush("(Python)")
        opPush("(invalid)")
        get()
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), "(Python)")

    def testGetInsufficient(self):
        opstack.clear()
        opPush("(Python)")
        get()
        self.assertEqual(opPop(), "(Python)")

    def testGetIntervalValid(self):
        opstack.clear()
        opPush("(Learning Python)")
        opPush(6)
        opPush(6)
        getinterval()
        self.assertEqual(opPop(), "g Pytho")

    def testGetIntervalInvalid(self):
        opstack.clear()
        opPush("(Learning Python)")
        opPush("(invalid)")
        opPush(5)
        getinterval()
        self.assertEqual(opPop(), 5)
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), "(Learning Python)")

    def testGetIntervalInsufficient(self):
        opstack.clear()
        opPush("(Learning Python)")
        opPush(6)
        getinterval()
        self.assertEqual(opPop(), 6)
        self.assertEqual(opPop(), "(Learning Python)")

    def testPutValid(self):
        opstack.clear()
        opPush("(Hello, World!)")
        opPush(7)
        opPush(ord('C'))
        put()
        self.assertEqual(opPop(), "(Hello, Corld!)")

    def testPutInvalid(self):
        opstack.clear()
        opPush("(Hello, World!)")
        opPush("(invalid)")
        opPush(ord('C'))
        put()
        self.assertEqual(opPop(), ord('C'))
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), "(Hello, World!)")

    def testPutInsufficient(self):
        opstack.clear()
        opPush("(Hello, World!)")
        opPush(7)
        put()
        self.assertEqual(opPop(), 7)
        self.assertEqual(opPop(), "(Hello, World!)")


#-------------------------------------------------------------------------#    
#test each operant with valid operand
#test eac operator with invalid operand
#test each operator with insufficient operand 
    def testDupValid(self):
        opstack.clear()
        opPush(42)
        dup()
        self.assertEqual(opPop(), 42)
        self.assertEqual(opPop(), 42)

    def testDupInsufficient(self):
        opstack.clear()
        dup()
        self.assertEqual(len(opstack), 0)

    def testCopyValid(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(2)
        copy()
        self.assertEqual(opstack, [1, 2, 3, 2, 3])

    def testCopyInvalid(self):
        opstack.clear()
        opPush("(invalid)")
        copy()
        self.assertEqual(opPop(), "(invalid)")

    def testCopyInsufficient(self):
        opstack.clear()
        copy()
        self.assertEqual(len(opstack), 0)

    def testPopValid(self):
        opstack.clear()
        opPush(42)
        pop()
        self.assertEqual(len(opstack), 0)

    def testPopInsufficient(self):
        opstack.clear()
        pop()
        self.assertEqual(len(opstack), 0)

    def testClearValid(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        clear()
        self.assertEqual(len(opstack), 0)

    def testExchValid(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertEqual(opPop(), 1)
        self.assertEqual(opPop(), 2)

    def testExchInsufficient(self):
        opstack.clear()
        opPush(1)
        exch()
        self.assertEqual(opPop(), 1)

    def testRollValid(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(5)
        opPush(3)
        opPush(2)
        roll()
        self.assertEqual(opstack, [1, 2, 4, 5, 3])

    def testRollInvalid(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush("(invalid)")
        opPush(1)
        roll()
        self.assertEqual(opPop(), 1)
        self.assertEqual(opPop(), "(invalid)")
        self.assertEqual(opPop(), 2)
        self.assertEqual(opPop(), 1)

    def testRollInsufficient(self):
        opstack.clear()
        opPush(1)
        roll()
        self.assertEqual(opPop(), 1)

    def testStackValid(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        stack()
        self.assertEqual(opstack, [1, 2, 3])

    def testStackEmpty(self):
        opstack.clear()
        stack()
        self.assertEqual(len(opstack), 0)


#-------------------------------------------------------------------------#    
#test each operant with valid operand
#test eac operator with invalid operand
#test each operator with insufficient operand 
    def testPsDictValid(self):
        opstack.clear()
        opPush(1)
        psDict()
        self.assertIsInstance(opPop(), dict)

    def testPsDictInvalid(self):
        opstack.clear()
        opPush("(invalid)")
        psDict()
        self.assertEqual(opPop(), "(invalid)")

    def testPsDictInsufficient(self):
        opstack.clear()
        psDict()
        self.assertEqual(len(opstack), 0)

    def testBeginValid(self):
        opstack.clear()
        dictstack.clear()
        opPush({})
        begin()
        self.assertEqual(len(dictstack), 1)

    def testBeginInvalid(self):
        opstack.clear()
        dictstack.clear()
        opPush(42)
        begin()
        self.assertEqual(opPop(), 42)
        self.assertEqual(len(dictstack), 0)

    def testBeginInsufficient(self):
        opstack.clear()
        dictstack.clear()
        begin()
        self.assertEqual(len(opstack), 0)
        self.assertEqual(len(dictstack), 0)

    def testEndValid(self):
        opstack.clear()
        dictstack.clear()
        dictPush({})
        end()
        self.assertEqual(len(dictstack), 0)

    def testEndInvalid(self):
        opstack.clear()
        dictstack.clear()
        dictPush(42)
        end()
        self.assertEqual(len(dictstack), 0)

    def testEndInsufficient(self):
        opstack.clear()
        dictstack.clear()
        end()
        self.assertEqual(len(dictstack), 0)

    def testPsDefValid(self):
        opstack.clear()
        dictstack.clear()
        dictPush({})
        opPush("/x")
        opPush(10)
        psDef()
        self.assertEqual(dictstack[-1]['/x'], 10)

    def testPsDefInvalid(self):
        opstack.clear() 
        dictstack.clear()
        dictPush({})
        opPush(10)
        opPush("/x")
        psDef()
        self.assertEqual(opPop(), "/x")
        self.assertEqual(opPop(), 10)

    def testPsDefInsufficient(self):
        opstack.clear()
        dictstack.clear()
        dictPush({})
        opPush("/x")
        psDef()
        self.assertEqual(opPop(), "/x")
     
#-------------------------------------------------------------------------#    using sample test cases

    def testOpPush(self):
        opstack.clear()
        opPush("(Hello)")
        self.assertEqual(opstack[-1],"(Hello)")
    
    def testOpPush2(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opstack[-1],5)

    def testOpPop(self):
        opstack.clear()
        opPush(5)
        self.assertEqual(opPop(),5)
    
    def testDictPush(self):
        dictstack.clear()
        dictPush({})
        self.assertEqual(dictstack[-1],{})

    def testDictPop(self):
        dictstack.clear()
        dictPush({})
        dictPop()
        self.assertEqual(len(dictstack),0)

    def testDefine(self):
        dictstack.clear()
        define("/a",1)
        self.assertEqual(len(dictstack),1)

    def testLookup(self):
        dictstack.clear()  
        opPush("/n1")       
        opPush("(hornswaggle)")  
        psDef()
        self.assertEqual(lookup("n1"),"(hornswaggle)")

    def testAdd(self):
        opstack.clear()     
        opPush(1.0)       
        opPush(2.0)       
        add()       
        self.assertEqual(opPop(),3)

    def testAdd2(self):
        opstack.clear()     
        opPush(3)
        opPush("(notanum)")
        add()       
        self.assertEqual(opPop(),"(notanum)")
        self.assertEqual(opPop(),3)

    def testSub(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        sub()
        self.assertEqual(opPop(),1)
    
    def testMul(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mul()
        self.assertEqual(opPop(),6)

    def testDiv(self):
        opstack.clear()
        opPush(4)
        opPush(2)
        div()
        self.assertEqual(opPop(),2)
    
    def testMod(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        mod()
        self.assertEqual(opPop(),1)

    def testEq2(self):
        opstack.clear()
        opPush(3)
        opPush(2)
        eq()
        self.assertEqual(opPop(),False)

    def testLt(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        lt()
        self.assertEqual(opPop(),True)

    def testGt2(self):
        opstack.clear()
        opPush(2)
        opPush(3)
        gt()
        self.assertEqual(opPop(),False)

    def testLength(self):
        opstack.clear()
        opPush("(Hello)")
        length()
        self.assertEqual(opPop(),5)

    def testGet(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        get()
        self.assertEqual(opPop(),ord('C'))

    def testGetInterval(self):
        opstack.clear()
        opPush("(CptS355)")
        opPush(0)
        opPush(3)
        getinterval()
        self.assertEqual(opPop(),"(Cpt)")

    def testPut(self):
        opstack.clear()
        opPush("(CptS355)")
        dup()
        opPush(0)
        opPush(48)
        put()
        self.assertEqual(opPop(),"(0ptS355)")

    def testDup(self):
        opstack.clear()
        opPush(3)
        dup()
        self.assertEqual(len(opstack),2)

    def testPop(self):
        opstack.clear()
        opPush(1)
        pop()
        self.assertEqual(len(opstack),0)
    
    def testClear(self):
        opstack.clear()
        opPush(1)
        clear()
        self.assertEqual(len(opstack),0)

    def testExch(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        exch()
        self.assertListEqual(opstack,[2,1])

    def testRoll(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(2)
        opPush(3)
        roll()
        self.assertListEqual(opstack,[1,2,4,3])
    
    def testStack(self):
        pass # unsure how to test print, maybe have it return instead
        text_trap = io.StringIO()
        sys.stdout = text_trap
        opstack.clear()
        opPush(2)
        opPush(3)
        stack()
        sys.stdout = sys.__stdout__
        self.assertEqual(text_trap.getvalue(), "3\n2\n")

    def testPsDict(self):
        opstack.clear()
        opPush(2)
        psDict()
        self.assertIsInstance(opPop(), dict)

    def testPsDef(self):
        opstack.clear()
        dictstack.clear()
        opPush(2)
        psDict()
        begin()
        opPush("/a")
        opPush(2)
        psDef()
        self.assertEqual(dictstack[-1],{"/a":2})

if __name__ == '__main__':
    unittest.main()

