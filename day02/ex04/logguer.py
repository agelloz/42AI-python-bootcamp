import time

def log(function):
    def wrapper(*argc):
        time_milli = lambda x: round(x * 1000, 3)
        start = time.time()
        if function(*argc):
            return True
        delta = time.time() - start
        f = open('log.txt', 'a+')
        fstr = '(agelloz)Running: {:25}[ exec-time = {} {} ]\n'.format(function.__name__, round(delta, 3) if delta >= 1. else time_milli(delta), 's' if delta >= 1. else 'ms' ) 
        f.write(fstr)
        f.close()
    return wrapper
