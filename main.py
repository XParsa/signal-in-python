import signal

def main(x,y):
    print("you can't kill me")


signal.signal(signal.SIGINT,main)

while true:
    pass

