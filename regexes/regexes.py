import re

# CONSTANTS
URL_PATTERN = (
    r"(?i)^https?://(.*@)?(\w+|\w[\w-]*\w)(\.(\w{1,2}|\w[\w-]*\w))*(:[0-9]+)?(/.*)?$"
)

test_urls = [
    (
        True,
        "https://stackoverflow.com/questions/6718633/python-regular-expression-again-match-url",
    ),
    (True, "http://localhost:8080"),
    (True, "http://localhost"),
    (True, "http://127.0.0.1:8080"),
    (True, "http://127.0.0.1"),
    (False, "file:///localhost:8080/mnt/c/hello.world.txt"),
    (
        True,
        "http://jpjofre:ABCdef123!@www.MY-Lucky_web_place.doc:10403/first/second/resource?&arg1=2345#somewhereelse",
    ),
    (True, "http://foo.com/blah_blah"),
    (True, "http://foo.com/blah_blah/"),
    (True, "http://foo.com/blah_blah_(wikipedia)"),
    (True, "http://foo.com/blah_blah_(wikipedia)_(again)"),
    (True, "http://www.example.com/wpstyle/?p=364"),
    (True, "https://www.example.com/foo/?bar=baz&inga=42&quux"),
    (False, "http://✪df.ws/123"),
    (True, "http://userid:password@example.com:8080"),
    (True, "http://userid:password@example.com:8080/"),
    (True, "http://userid@example.com"),
    (True, "http://userid@example.com/"),
    (True, "http://userid@example.com:8080"),
    (True, "http://userid@example.com:8080/"),
    (True, "http://userid:password@example.com"),
    (True, "http://userid:password@example.com/"),
    (True, "http://142.42.1.1/"),
    (True, "http://142.42.1.1:8080/"),
    (False, "http://➡.ws/䨹"),
    (False, "http://⌘.ws"),
    (False, "http://⌘.ws/"),
    (True, "http://foo.com/blah_(wikipedia)#cite-1"),
    (True, "http://foo.com/blah_(wikipedia)_blah#cite-1"),
    (True, "http://foo.com/unicode_(✪)_in_parens"),
    (True, "http://foo.com/(something)?after=parens"),
    (False, "http://☺.damowmow.com/"),
    (True, "http://code.google.com/events/#&product=browser"),
    (True, "http://j.mp"),
    (True, "http://foo.bar/?q=Test%20URL-encoded%20stuff"),
    (True, "http://مثال.إختبار"),
    (True, "http://例子.测试"),
    (False, "http://उदाहरण.परीक्षा"),
    (True, "http://-.~_!$&'()*+,;=:%40:80%2f::::::@example.com"),
    (True, "http://1337.net"),
    (True, "http://a.b-c.de"),
    (True, "http://223.255.255.254"),
    (False, "http:// "),
    (False, "http://."),
    (False, "http://.."),
    (False, "http://../"),
    (False, "http://?"),
    (False, "http://??"),
    (False, "http://??/"),
    (False, "http://#"),
    (False, "http://##"),
    (False, "http://##/"),
    (False, "http://foo.bar?q=   "),
    (False, "ftp://foo.bar/baz"),
    (False, "//"),
    (False, "//a"),
    (False, "///a"),
    (False, "///"),
    (False, "http:///a"),
    (False, "foo.com"),
    (False, "rdar://1234"),
    (False, "h://test"),
    (False, "http:// shouldfail.com"),
    (False, ":// should fail"),
    (True, "http://foo.bar/foo(bar)baz quux"),
    (False, "ftps://foo.bar/"),
    (False, "http://-error-.invalid/"),
    (True, "http://a.b--c.de/"),
    (False, "http://-a.b.co"),
    (False, "http://a.b-.co"),
    (False, "http://.www.foo.bar/"),
    (False, "http://www.foo.bar./"),
    (False, "http://.www.foo.bar./"),
]
if __name__ == "__main__":
    for valid, url in test_urls:
        url = url.strip()
        m = re.match(URL_PATTERN, url)
        if not m:
            if valid:
                print(f"[ERROR] Expected match (valid is True) not true for '{url}'")
                for c in url:
                    print(
                        f"{c}: {c.isalpha()=}, {c.isdecimal()=}, {c.isdigit()=}, {c.isnumeric()=}"
                    )
        else:
            if not valid:
                print(f"[ERROR] Unexpected match for '{url}'")
                print(URL_PATTERN)
                print(m.groups())
