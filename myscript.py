print("this line is printed")
ip = '192.168.12.42'
print(ip)

def run():
    prepare("this is a duplicate")  # Noncompliant - "this is a duplicate" is duplicated 3 times
    execute("this is a duplicate")
    release("this is a duplicate")
