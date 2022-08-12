def run():
    while True:
        text =(yield)
        print(text)

x= run()
next(x)
x.send("Hello")
x.send("ffff")