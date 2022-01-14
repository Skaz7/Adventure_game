def pos_neg(a, b, negative):
    if a > 0 and b < 0 and negative == False:
        return True
    elif a < 0 and b > 0 and negative == False:
        return True
    elif a < 0 and b < 0 and negative == True:
        return True
    else:
        return False

print()
print(pos_neg(1, -1, False))
print(pos_neg(-1, 1, False))
print(pos_neg(-4, -5, True))

###################################################
def not_string(str):
    if str.startswith('not') == True:
        return str
    else:
        return 'not '+str

print()
print(not_string('candy'))

###################################################

def missing_char(str, n):
    a = str[0:n]
    b = str[n+1:]
    return a+b

print()
print(missing_char('kitten', 1))

###################################################

def front_back(str):
    if len(str) <= 1:
        return str
    else:
        return str[-1]+str[1:-1]+str[0]

print()
print(front_back('a'))

###################################################

def front3(str):
    if len(str) <= 3:
        return str * 3
    else:
        return str[:3]*3

print()
print(front3('Java'))
print(front3('Chocolate'))
print(front3('abc'))

###################################################

def string_times(str, n):
    return str * n

print()
print(string_times('Hi', 2))
print(string_times('Hi', 3))
print(string_times('Hi', 1))

###################################################

def front_times(str, n):
    return str[0:3] * n

print()
print(front_times('Chocolate', 2))
print(front_times('Chocolate', 3))
print(front_times('Abc', 3))

###################################################

def string_bits(str):
    str = str[::2]
    return str

print()
print(string_bits('Hello'))
print(string_bits('Hi'))
print(string_bits('Heeololeo'))

###################################################

def string_splosion(str):
    a = ''
    for i in range(len(str)+1):
        start = str[0:i]
        a += start
    return a

print()
print(string_splosion('Code'))
print(string_splosion('abc'))
print(string_splosion('ab'))

###################################################

def last2(str):
    if len(str) < 2:
        return 0

    count = 0
    search = str[-2:]
    for i in range(0, len(str)-2):
        if search in str[i:i+2]:
            count += 1
        else:
            count = count
    return count

print()
print(last2('hixxhi'))
print(last2('xaxxaxaxx'))
print(last2('axxxaaxx'))

###################################################

def array_count9(nums):
    count = 0
    for i in nums:
        if i == 9:
            count += 1
    return count

print()
print(array_count9([1, 2, 9]))
print(array_count9([1, 9, 9]))
print(array_count9([1, 9, 9, 3, 9]))

###################################################

def array_front9(nums):
    if 9 in nums[0:4]:
        return True
    else:
        return False

print()
print(array_front9([1, 2, 9]))
print(array_front9([1, 2, 3, 9, 9]))
print(array_front9([1, 2, 3, 4, 5]))

###################################################

def array123(nums):
    count = 0
    for i in range(0, len(nums)-2):
        if nums[i] == 1 and nums[i + 1] == 2 and nums[i + 2] == 3:
            count += 1
        else:
            count == count
    return count>0

print()
print(array123([1, 1, 2, 3, 1]))
print(array123([1, 1, 2, 4, 1]))
print(array123([1, 1, 2, 1, 2, 3]))

###################################################

def string_match(a, b):
    count = 0
    shorter = min(len(a), len(b))
    for i in range(0, shorter - 1):
        if a[i] == b[i] and a[i+1] == b[i+1]:
            count += 1
        else:
            count == count
    return count

print()
print(string_match('xxcaazz', 'xxbaaz'))
print(string_match('abc', 'abc'))
print(string_match('abc', 'axc'))

###################################################

def hello_name(name):
    return f'Hello {name}!'

print()
print(hello_name('Bob'))
print(hello_name('Alice'))
print(hello_name('X'))

###################################################

def make_abba(a, b):
    return a+b+b+a

print()
print(make_abba('Hi', 'Bye'))
print(make_abba('Yo', 'Alice'))
print(make_abba('What', 'Up'))

###################################################

def make_tags(tag, word):
    # return '<'+tag+'>'+word+'</'+tag+'>'
    return f'<{tag}>{word}</{tag}>'

print()
print(make_tags('i', 'Yay'))
print(make_tags('i', 'Hello'))
print(make_tags('cite', 'Yay'))

###################################################

def make_out_word(out, word):
    return out[0:2]+word+out[2:4]

print()
print(make_out_word('<<>>', 'Yay'))
print(make_out_word('<<>>', 'WooHoo'))
print(make_out_word('[[]]', 'word'))

###################################################

def extra_end(str):
    return str[-2:]*3

print()
print(extra_end('Hello'))
print(extra_end('ab'))
print(extra_end('Hi'))

###################################################

def first_two(str):
    if len(str) > 1:
        return str[0:2]
    elif len(str) == 1:
        return str
    else:
        return ""

print()
print(first_two('Hello'))
print(first_two('abcdefg'))
print(first_two('ab'))

###################################################

def first_half(str):
    return str[0 : int(len(str)/2)]

print()
print(first_half('WooHoo'))
print(first_half('HelloThere'))
print(first_half('abcdef'))
