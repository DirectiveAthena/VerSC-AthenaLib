# ----------------------------------------------------------------------------------------------------------------------
# - Package Imports -
# ----------------------------------------------------------------------------------------------------------------------
# General Packages
import unittest

# Custom Library
from AthenaLib.StrictAnnotated.StrictAnnotated import *

# Custom Packages

# ----------------------------------------------------------------------------------------------------------------------
# - Support Code -
# ----------------------------------------------------------------------------------------------------------------------
@StrictAnnotated
def AnnotatedTest_1(a:str):
    return a

@StrictAnnotated
def AnnotatedTest_2(a:str) -> str:
    return a

@StrictAnnotated
def AnnotatedTest_3(a:str, b:str):
    return a,b

@StrictAnnotated
def AnnotatedTest_4(a:str, b:str) -> tuple[str,str]:
    return a,b


# ----------------------------------------------------------------------------------------------------------------------
# - Code -
# ----------------------------------------------------------------------------------------------------------------------
class Test(unittest.TestCase):
    def test_Fail(self):
        with self.assertRaises(StrictError):
            AnnotatedTest_1(1)
        with self.assertRaises(StrictError):
            AnnotatedTest_2(1)
        with self.assertRaises(StrictError):
            AnnotatedTest_3(1,1)
        with self.assertRaises(StrictError):
            AnnotatedTest_4(1,1)