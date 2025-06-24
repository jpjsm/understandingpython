from decorators09 import timer, debug

DebugMode = False
CacheEnabled = True
ParenthesesGroups = {}


@timer
@debug
def generatebalancedparentheses(n: int):
    if n < 0:
        raise ArithmeticError(
            "Argument '{0}' must be greater or equal to zero".format(n)
        )

    if n == 0:
        return [""]

    if n == 1:
        return ["()"]

    if CacheEnabled and n in ParenthesesGroups:
        return ParenthesesGroups[n]

    result = []
    for i in range(0, n):
        for left in generatebalancedparentheses(i):
            for right in generatebalancedparentheses(n - 1 - i):
                item = "(" + left + ")" + right
                result.append(item)

    if CacheEnabled:
        ParenthesesGroups[n] = result

    return result


if __name__ == "__main__":
    n = 4

    generatebalancedparentheses(n)
