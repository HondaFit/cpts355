import unittest
import HW5

class TestInterpretSPS(unittest.TestCase):
    def setUp(self):
        HW5.opstack.clear()
        HW5.dictstack.clear()

    def test_arithmetic_operations(self):
        code = [1, 2, 'add', 3, 'sub', 4, 'mul', 5, 'div']
        HW5.interpretSPS(code)
        self.assertEqual(HW5.opPop(), 2)
        self.assertEqual(HW5.opPop(), -8)

    # Add more test cases for arithmetic operations

    def test_comparison_operations(self):
        code = [2, 3, 'lt', 4, 5, 'gt', 2, 2, 'eq']
        HW5.interpretSPS(code)
        self.assertEqual(HW5.opPop(), True)
        self.assertEqual(HW5.opPop(), True)
        self.assertEqual(HW5.opPop(), True)

    # Add more test cases for comparison operations

    def test_stack_manipulation(self):
        code = [1, 2, 3, 'dup', 'exch', 'pop', 'copy']
        HW5.interpretSPS(code)
        self.assertEqual(HW5.opPop(), 2)
        self.assertEqual(HW5.opPop(), 1)
        self.assertEqual(HW5.opPop(), 2)
        self.assertEqual(HW5.opPop(), 1)

    # Add more test cases for stack manipulation

    def test_control_structures(self):
        code = [1, 2, 3, 2, 'copy', 'lt', [4, 'add'], [5, 'sub'], 'ifelse']
        HW5.interpretSPS(code)
        self.assertEqual(HW5.opPop(), 6)

        code = [1, 1, 6, [1, 'add'], 'for']
        HW5.interpretSPS(code)
        self.assertEqual(HW5.opPop(), 7)

    # Add more test cases for control structures

    def test_function_definition_and_call(self):
        code = ['/square', ['dup', 'mul'], 'def', 2, 'square']
        HW5.interpretSPS(code)
        self.assertEqual(HW5.opPop(), 4)

    # Add more test cases for function definition and call

    def test_undefined_name(self):
        code = ['undefined_name']
        with self.assertRaises(ValueError):
            HW5.interpretSPS(code)

    # Add more test cases for handling undefined names

    def test_invalid_operands(self):
        code = [1, 'add']
        with self.assertRaises(TypeError):
            HW5.interpretSPS(code)

    # Add more test cases for handling invalid operands

    def test_stack_underflow(self):
        code = ['pop']
        with self.assertRaises(IndexError):
            HW5.interpretSPS(code)

    # Add more test cases for handling stack underflow

    # Add more test cases for stack overflow

if __name__ == '__main__':
    unittest.main()
