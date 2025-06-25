class Foo():
    Name = 'Undefined'

    def __init__(self, name=None):
        if name is not None:
            self.Name = str(name)

    def __str__(self):
        return self.Name

    def __repr__(self):
        return "[{0}] {1}.{2}: {3}".format(id(self), self.__class__.__module__, self.__class__.__name__, self.Name)


class FooEqual(Foo):
    def __eq__(self, other):
        if isinstance(other, FooEqual):
            return self.Name == other.Name
        return NotImplemented

    def __ne__(self, other):
        r = self.__eq__(other)
        if r is NotImplemented:
            return r
        return not r

f1 = FooEqual('foo')
f2 = FooEqual('foo')
print str(f1), str(f1.Name)
print "Are f1 and f2 equal? %s" % (f1 == f2 )

a = [1, 2, None, 'a', 'A', '', True, False, Foo(), Foo('foo'), FooEqual(), FooEqual('foo')]
b = [1, 2, 3, 4, None, 'a', 'A', 'b', 'B', '', True, False, Foo(), Foo('foo'), FooEqual(), FooEqual('foo')]

print "A: {0}".format(a)
print "B: {0}".format(b)
print "C: {0}".format([c for c in a if c in b]) ## a references are passed to C