#!/usr/bin/env python
# -*- coding: utf-8 -*-

class TestScopes(object):
    ClassStaticAttribute = "This is a class level static attribute"
    def __init__(self, arg1, num1=1, num2=2):
        self.InstanceAttributeFromArg1 = arg1
        self.n1 = num1 if not num1 is None else 1
        self.n2 = num2 if not num2 is None else 2

    @staticmethod
    def suma(a,b):
        return a + b

    def InstanceMethod(self, parameter_list):
        InstanceResult = 'instance method called'
        return InstanceResult, self, parameter_list, self.InstanceAttributeFromArg1, TestScopes.suma(self.n1, self.n2)

    @staticmethod
    def StaticMethod(parameter_list):
        StaticResult = 'static method called'
        return StaticResult, parameter_list, TestScopes.ClassStaticAttribute

    @classmethod
    def ClassMethod(cls):
        ClassResult = 'class method called'
        return ClassResult, cls, TestScopes.ClassStaticAttribute

    @classmethod
    def ClassMethod2(foo):
        ClassResult = 'class2 method called'
        return ClassResult, foo.suma(1,2), TestScopes.ClassStaticAttribute

if __name__ == "__main__":
    print TestScopes.ClassMethod()
    print TestScopes.ClassMethod2()
    print TestScopes.StaticMethod("hello static")
    foo = TestScopes('value1')
    print foo.InstanceMethod(['param1', 'param2'])
    print foo.ClassMethod()
    print foo.StaticMethod(['param1', 'param2'])
    print TestScopes.ClassStaticAttribute
    # The following statements should fail, as the mentioned attributes are defined at function scope
    print TestScopes.InstanceResult
    print TestScopes.StaticResult
    print TestScopes.ClassResult
