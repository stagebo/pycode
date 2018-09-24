
def run_child():
    raise Exception('my exception')

def run():
    try:
        run_child()
    except:
        raise
        print('run exception')
def run0():
    try:
        run()
        print('right')
    except:
        print('exception')

run0()