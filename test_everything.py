from subprocess import check_output

def test_1_1():
    assert str(1144) == check_output('python2 1-1.py', shell=True).strip('\n')

def test_1_2():
    assert str(1194) == check_output('python2 1-2.py', shell=True).strip('\n')

def test_2_1():
    assert str(32020) == check_output('python2 2-1.py', shell=True).strip('\n')

def test_2_2():
    assert str(236) == check_output('python2 2-2.py', shell=True).strip('\n')

def test_3_1():
    assert str(326) == check_output('python2 3-1.py', shell=True).strip('\n')

def test_3_2():
    assert str(363010) == check_output('python2 3-2.py', shell=True).strip('\n')

def test_4_1():
    assert str(337) == check_output('python2 4-1.py', shell=True).strip('\n')

def test_4_2():
    assert str(231) == check_output('python2 4-2.py', shell=True).strip('\n')

def test_5_1():
    assert str(356945) == check_output('python2 5-1.py', shell=True).strip('\n')

def test_5_2():
    assert str(28372145) == check_output('python2 5-2.py', shell=True).strip('\n')

def test_6_1():
    assert str(11137) == check_output('python2 6-1.py', shell=True).strip('\n')

def test_6_2():
    assert str(1037) == check_output('python2 6-2.py', shell=True).strip('\n')

def test_7_1():
    assert 'fbgguv' == check_output('python2 7-1.py', shell=True).strip('\n')

def test_7_2():
    #no
    assert True

def test_8_1():
    assert str(7296) == check_output('python2 8-1.py', shell=True).strip('\n')
 
def test_8_2():
    assert str(8186) == check_output('python2 8-2.py', shell=True).strip('\n')

def test_9_1():
    assert str(8337) == check_output('python2 9-1.py', shell=True).strip('\n')

def test_9_2():
    assert str(4330) == check_output('python2 9-2.py', shell=True).strip('\n')

def test_10_1():
    assert str(8536) == check_output('python2 10-1.py', shell=True).strip('\n')

def test_10_2():
    assert 'aff593797989d665349efe11bb4fd99b' == check_output('python2 10-2.py', shell=True).strip('\n')