__author__ = 'weizheng'

from twisted.internet import reactor, defer

def getDummyData(x):
    d = defer.Deferred()
    reactor.callLater(2, d.callback, x * 3)
    return d

def printData(d):
    print(d)

def printError(failure):
    import sys
    sys.stderr.write(str(failure))

#d = getDummyData(3)
#d.addCallback(printData)

class Getter:
    def __init__(self):
        self.d = None

    def gotResults(self, x):
        if self.d is None:
            print "Nowhere to put results"
            return

        d = self.d
        self.d = None

        if x % 2 == 0:
            d.callback(x * 3)
        else:
            d.errback(ValueError("You used an odd number"))

    def _toHTML(self, r):
        return "Result is %s" % r

    def getDummyData(self, x):
        self.d = defer.Deferred()
        reactor.callLater(2, self.gotResults, x)
        self.d.addCallback(self._toHTML)
        return self.d

g = Getter()
d = g.getDummyData(3)
d.addCallback(printData)
d.addErrback(printError)

g = Getter()
d = g.getDummyData(4)
d.addCallback(printData)
d.addErrback(printError)

reactor.callLater(4, reactor.stop)
reactor.run()