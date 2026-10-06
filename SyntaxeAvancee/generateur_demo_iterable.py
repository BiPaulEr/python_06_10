def generator():
    yield "1"
    yield "2"

    for a in 'abc':
        yield a
    print("end")


gen = generator()

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))

print(next(gen))
print(next(gen))
