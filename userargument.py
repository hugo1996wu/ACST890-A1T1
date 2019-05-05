import sys
def writeln(x=''):
    """
    Write x and an end-of-line mark to standard output.
    """
    if sys.hexversion < 0x03000000:
        x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.write('\n')
    sys.stdout.flush()

#-----------------------------------------------------------------------

def write(x=''):
    """
    Write x to standard output.
    """
    if (sys.hexversion < 0x03000000):
        x = unicode(x)
        x = x.encode('utf-8')
    else:
        x = str(x)
    sys.stdout.write(x)
    sys.stdout.flush()

write('Hi, ')
write(sys.argv[1])
writeln('. How are you?')
