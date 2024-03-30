import sys
import io
import unittest
from HW4 import *

class HW4Tests(unittest.TestCase):
    def setUp(self):
        pass

    def testDictPush2(self):
        dictstack.clear()
        dictPush({"/a": 1, "/b": 2})
        self.assertEqual(dictstack[-1], {"/a": 1, "/b": 2})

    def testDefine2(self):
        dictstack.clear()
        define("/x", "(CptS355)")
        self.assertEqual(dictstack[-1], {"/x": "(CptS355)"})

    def testLookup2(self):
        dictstack.clear()
        dictPush({"/a": 1, "/b": 2})
        dictPush({"/c": 3, "/d": 4})
        self.assertEqual(lookup("c"), 3)

    def testSub2(self):
        opstack.clear()
        opPush(10)
        opPush(5)
        opPush("(hello)")
        sub()
        self.assertEqual(opPop(), "(hello)")
        self.assertEqual(opPop(), 10)

    def testMul2(self):
        opstack.clear()
        opPush(3)
        opPush(0)
        mul()
        self.assertEqual(opPop(), 0)

    def testDiv2(self):
        opstack.clear()
        opPush(10)
        opPush(0)
        div()
        self.assertEqual(opPop(), 0)
        self.assertEqual(opPop(), 10)

    def testEq(self):
        opstack.clear()
        opPush(5)
        opPush(5)
        eq()
        self.assertEqual(opPop(), True)

    def testLt2(self):
        opstack.clear()
        opPush(5)
        opPush(5)
        lt()
        self.assertEqual(opPop(), False)

    def testGt(self):
        opstack.clear()
        opPush(5)
        opPush(3)
        gt()
        self.assertEqual(opPop(), True)

    def testLength2(self):
        opstack.clear()
        opPush("(abcdefg)")
        length()
        self.assertEqual(opPop(), 7)

    def testGet2(self):
        opstack.clear()
        opPush("(WSU)")
        opPush(2)
        get()
        self.assertEqual(opPop(), ord('U'))

    def testGetInterval2(self):
        opstack.clear()
        opPush("(Pullman)")
        opPush(1)
        opPush(4)
        getinterval()
        self.assertEqual(opPop(), "(ullm)")

    def testPut2(self):
        opstack.clear()
        opPush("(Cougs)")
        dup()
        opPush(4)
        opPush(ord('a'))
        put()
        self.assertEqual(opPop(), "(Couga)")

    def testCopy2(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(2)
        copy()
        self.assertListEqual(opstack, [1, 2, 3, 2, 3])

    def testRoll2(self):
        opstack.clear()
        opPush(1)
        opPush(2)
        opPush(3)
        opPush(4)
        opPush(2)
        opPush(-1)
        roll()
        self.assertListEqual(opstack, [1, 2, 4, 3])

    def testBegin2(self):
        opstack.clear()
        dictstack.clear()
        opPush({"/x": 1, "/y": 2})
        opPush({"/a": 10, "/b": 20})
        begin()
        self.assertEqual(dictstack[-1], {"/a": 10, "/b": 20})

    def testPsDef2(self):
        opstack.clear()
        dictstack.clear()
        opPush(3) 
        psDict()
        begin()
        opPush("/x")
        opPush(10)
        psDef()
        self.assertEqual(dictstack[-1], {"/x": 10})

if __name__ == '__main__':
    unittest.main()

