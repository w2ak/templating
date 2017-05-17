#!/usr/bin/env python3
import sys
import matplotlib
import matplotlib.pyplot as pyplot
from matplotlib.backends.backend_pdf import PdfPages

class Graph:
    def __init__ (self):
        self.ndots = 0
        self.nfigs = 0
        self.x = list()
        self.xstr = ''
        self.y = list()
        self.ystr = list()
        self.yfig = list()

    def check (self):
        n = self.ndots
        if (len(self.x) != n):
            return 1
        if (len(self.y) != len(self.ystr)):
            return 1
        for l in self.y:
            if (len(l) != n):
                return 1
        return 0

    def addX (self, x, xstr):
        self.x = x
        self.xstr = xstr
        self.ndots = len(self.x)
        return 0

    def newX (self, xstr):
        return self.addX(list(),xstr)

    def addY (self, y, ystr, yfig=1):
        if (len(y) != self.ndots):
            return 1
        self.y.append(y)
        self.ystr.append(ystr)
        self.yfig.append(yfig)
        self.nfigs = max(self.nfigs, yfig)
        return 0

    def newY (self, ystr, yfig=1):
        return self.addY(list(),ystr,yfig)

    def append (self, vals):
        if (len(vals) != 1 + len(self.y)):
            return 1
        self.x.append(vals.pop(0))
        for l in self.y:
            l.append(vals.pop(0))
        return 0

    def view (self):
        print (':'.join([self.xstr, ','.join(map(str,self.x))]))
        for zstr,z in zip(self.ystr,self.y):
            print (':'.join([zstr, ','.join(map(str,z))]))

    def figure (self,size=None):
        fig = pyplot.figure(figsize=size)
        for zstr,z in zip(self.ystr,self.y):
            pyplot.plot(self.x,z,label=zstr)
        pyplot.legend()
        return fig

    def splitfigure (self,size=None):
        fig = pyplot.figure(figsize=size)
        n = self.nfigs
        for zfig,zstr,z in zip(self.yfig,self.ystr,self.y):
            pyplot.subplot(n,1,zfig)
            pyplot.plot(self.x,z,label=zstr)
            pyplot.legend()
        pyplot.subplot(n,1,n)
        pyplot.xlabel(self.xstr)
        return fig

    def figures (self, size=None):
        n = self.nfigs
        figs = [list() for _ in range(n)]
        for zfig, zstr, z in zip(self.yfig, self.ystr, self.y):
            figs[zfig-1].append((zstr,z))
        for i in range(n):
            fig = pyplot.figure(figsize=size)
            for z in figs[i]:
                pyplot.plot(self.x, z[1], label=z[0].split('(')[0])
                pyplot.ylabel(z[0], fontsize = 14)
                pyplot.legend(fontsize = 14)
            pyplot.xlabel(self.xstr, fontsize = 14)
            yield fig
            pyplot.close()

    def parse (self, source=sys.stdin):
        with open(source,'r+') if (type(source)==type(str())) else source as stream:
            firstline  = list(map(lambda x: int(x.strip()), stream.readline().strip().split(',')))
            secondline = list(map(lambda x: x.strip(), stream.readline().strip().split(',')))
            if (len(firstline) != len(secondline)):
                raise ValueError('Wrong line size.')
            if self.newX (secondline.pop(0)):
                raise ValueError('NewX error.')
            firstline.pop(0)
            while len(firstline):
                if self.newY (secondline.pop(0),firstline.pop(0)):
                    raise ValueError('NewY error.')
            l = stream.readline()
            while l:
                l = list(map(lambda x: float(x.strip()), l.strip().split(',')))
                if self.append(l):
                    raise ValueError('Wrong line size.')
                l = stream.readline()
        return self

if __name__=='__main__':
    g = Graph().parse()
    with PdfPages(sys.argv[1]) as pdf:
        for fig in g.figures(size=(8.3,5)):
            pdf.savefig(fig)

        d = pdf.infodict()
        print(d)
