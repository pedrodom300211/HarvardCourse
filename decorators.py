def announce(f):
    def wrapper():
        print("About to run te function...")
        f()
        print("Done with the fuction.")
        
    return wrapper

@announce
def hello():
    print("Hello world!")

hello()