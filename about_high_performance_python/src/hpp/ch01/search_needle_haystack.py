def search_fast(haystack: list[int], needle: int) -> bool:
    for item in haystack:
        if item == needle:
            return True

    return False


def search_slow(haystack: list[int], needle: int) -> bool:
    return_value = False
    for item in haystack:
        if item == needle:
            return_value = True

    return return_value


def search_unknown_tuple(haystack: list[int], needle: int) -> bool:
    return any((item == needle for item in haystack))


def search_unknown_list(haystack: list[int], needle: int) -> bool:
    return any([item == needle for item in haystack])
