def make_repeater(n):
    return lambda a:a*n
twice =make_repeater(6)

print twice('word')
print twice(8)
