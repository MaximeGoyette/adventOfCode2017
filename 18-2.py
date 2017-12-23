a = open('18.txt').read()
a = a.split('\n')

class Program:

    queues = {'0': [], '1': []}
    states = {'0': 'working', '1': 'working'}

    def __init__(self, no):
        self._no = str(no)
        self._reg = {'p': no}
        self._i = 0
        self._running = True
        self._nb_sent_values = 0
        
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
        self._nb_sent_values += 1
        if self._no == '0':
            Program.queues['1'].append(X)
        elif self._no == '1':
            Program.queues['0'].append(X)

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
        Program.states[self._no] = 'waiting'
        if len(Program.queues[self._no]) == 0:
            self._i -= 1
            return
        X = args[0]
        self._reg[X] = Program.queues[self._no].pop(0)
        Program.states[self._no] = 'working'

    def _jgz(self, args):
        X = self._arg_value(args[0])
        Y = self._arg_value(args[1])
        if X > 0:
            self._i += (Y-1)

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

p0 = Program(0)
p1 = Program(1)

while any([Program.states[x] == 'working' for x in Program.states]):
    p0._execute(a[p0._i])
    p1._execute(a[p1._i])
    p0._i += 1
    p1._i += 1

print p1._nb_sent_values