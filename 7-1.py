from anytree.importer import DictImporter
from anytree.exporter import DotExporter
from anytree import RenderTree
from itertools import chain

a = open('7.txt').read().split('\n')[:-1]
a = [x.split(' -> ') for x in a]
a = [x[0].split() + [x[1].split(', ') if len(x)>1 else []] for x in a]
a = {x[0]: (int(x[1][1:-1]), x[2]) for x in a}

root = (set(x for x in a) - set(chain(*[a[x][1] for x in a]))).pop()

print root