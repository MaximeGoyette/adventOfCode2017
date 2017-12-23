a = open('18.txt').read()
a = a.split('\n')

class Program:

    def __init__(self):
        self._reg = {}
        self._sound = None
        self._reveived = []
        self._i = 0
        
    def _arg_value(self, arg):
        if arg.replace('-', '').isdigit():
            return int(arg)
        elif arg in self._reg:
            return self._reg[arg]
        else:
            return 0
    
    def _validate_reg(self, reg):
        if not reg in self._reg:
            self._reg[reg] = 0

    def _set(self, args):
        X = args[0]
        Y = self._arg_value(args[1])
        self._reg[X] = Y

    def _snd(self, args):
        X = self._arg_value(args[0])
        self._sound = X

    def _add(self, args):
        X = args[0]
        Y = self._arg_value(args[1])
        self._validate_reg(X)
        self._reg[X] += Y

    def _mul(self, args):
        X = args[0]
        Y = self._arg_value(args[1])
        self._validate_reg(X)
        self._reg[X] *= Y

    def _mod(self, args):
        X = args[0]
        Y = self._arg_value(args[1])
        self._validate_reg(X)
        self._reg[X] %= Y

    def _rcv(self, args):
        X = self._arg_value(args[0])
        if X != 0:
            self._reveived.append(self._sound)
            print self._sound
            exit(0)

    def _jgz(self, args):
        X = self._arg_value(args[0])
        Y = self._arg_value(args[1])
        if X > 0:
            self._i += (Y - 1)

    def _execute(self, line):
        cmd = line[:3]
        args = line[4:].split()
        if cmd == 'set':
            self._set(args)
        elif cmd == 'snd':
            self._snd(args)
        elif cmd == 'add':
            self._add(args)
        elif cmd == 'mul':
            self._mul(args)
        elif cmd == 'mod':
            self._mod(args)
        elif cmd == 'rcv':
            self._rcv(args)
        elif cmd == 'jgz':
            self._jgz(args)

p0 = Program()

while p0._i < len(a):
    p0._execute(a[p0._i])
    p0._i += 1