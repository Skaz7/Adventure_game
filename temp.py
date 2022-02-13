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

###################################################

def without_end(str):
    return str[1:-1]

print()
print(without_end('Hello'))
print(without_end('java'))
print(without_end('coding'))

###################################################

def combo_string(a, b):
    if len(a) > len(b):
        return b+a+b
    else:
        return a+b+a

print()
print(combo_string('Hello', 'Hi'))
print(combo_string('hi', 'Hello'))
print(combo_string('aaa', 'b'))

###################################################

def non_start(a, b):
    return a[1:]+b[1:]

print()
print(non_start('Hello', 'There'))
print(non_start('java', 'code'))
print(non_start('shotl', 'java'))

###################################################

def left2(str):
    return str[2:]+str[:2]

print()
print(left2('Hello'))
print(left2('java'))
print(left2('Hi'))

###################################################

def first_last6(nums):
    if nums[0] == 6 or nums[-1] ==6:
        return True
    else:
        return False

print()
print(first_last6([1, 2, 6]))
print(first_last6([6, 1, 2, 3]))
print(first_last6([13, 6, 1, 2, 3]))

###################################################

def same_first_last(nums):
    if nums[0] == nums[-1]:
        return True
    else:
        return False

print()
print(same_first_last([1, 2, 3]))
print(same_first_last([1, 2, 3, 1]))
print(same_first_last([1, 2, 1]))

###################################################

def make_pi():
    return [3, 1, 4]

print()
print(make_pi())
###################################################

def common_end(a, b):
    if a[0] == b[0] or a[-1] == b[-1]:
        return True
    else:
        return False

print()
print(common_end([1, 2, 3], [7, 3]))
print(common_end([1, 2, 3], [7, 3, 2]))
print(common_end([1, 2, 3], [1, 3]))

###################################################

def sum3(nums):
    return sum(nums)

print()
print(sum3([1, 2, 3]))
print(sum3([5, 11, 2]))
print(sum3([7, 0, 0]))

###################################################

def rotate_left3(nums):
    temp = nums.pop(0)
    nums.insert(2, temp)
    return nums

print()
print(rotate_left3([1,2,3]))
print(rotate_left3([5, 11, 9]))
print(rotate_left3([7, 0, 0]))

###################################################

def reverse3(nums):
    nums.reverse()
    return nums

print()
print(reverse3([1,2,3]))
print(reverse3([5, 11, 9]))
print(reverse3([7, 0, 0]))

###################################################

def max_end3(nums):
    if nums[0] > nums[-1]:
        nums = [nums[0] for i in nums]
    else:
        nums = [nums[-1] for i in nums]
    return nums

print()
print(max_end3([1, 2, 3]))
print(max_end3([11, 5, 9]))
print(max_end3([2, 11, 3]))

###################################################

def sum2(nums):
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return sum(nums)
    else:
        return nums[0] + nums[1]

print()
print(sum2([1, 2, 3]))
print(sum2([1, 1]))
print(sum2([1, 1, 1, 1]))
print(sum2([]))
print(sum2([4]))

###################################################

def middle_way(a, b):
    new_list = []
    new_list.append(a[1])
    new_list.append(b[1])
    return new_list

print()
print(middle_way([1, 2, 3], [4, 5, 6]))
print(middle_way([7, 7, 7], [3, 8, 0]))
print(middle_way([5, 2, 9], [1, 4, 5]))

###################################################

def make_ends(nums):
    new_list = [nums[0], nums[-1]]
    return new_list


print()
print(make_ends([1, 2, 3]))
print(make_ends([1, 2, 3, 4]))
print(make_ends([7, 4, 6, 2]))

###################################################

def has23(nums):
    if 2 in nums or 3 in nums:
        return True
    else:
        return False

print()
print(has23([2, 5]))
print(has23([4, 3]))
print(has23([4, 5]))

###################################################

def squirrel_play(temp, is_summer):
    if is_summer == True and 60 <= temp <= 100:
        return True
    elif is_summer == False and 60 <= temp <= 90:
        return True
    else:
        return False

print()
print(squirrel_play(70, False))
print(squirrel_play(95, False))
print(squirrel_play(95, True))

###################################################

def caught_speeding(speed, is_birthday):
    if is_birthday == False:
        if speed <= 60:
            return 0
        elif 60 < speed <= 80:
            return 1
        else:
            return 2
    else:
        if speed <= 65:
            return 0
        elif 65 < speed <= 85:
            return 1
        else:
            return 2

print()
print(caught_speeding(60, False))
print(caught_speeding(65, False))
print(caught_speeding(65, True))

###################################################

def sorta_sum(a, b):
    if 10 <= a + b <= 19:
        return 20
    else:
        return a + b

print()
print(sorta_sum(3, 4))
print(sorta_sum(9, 4))
print(sorta_sum(10, 11))

###################################################

def alarm_clock(day, vacation):
    if vacation == False:
        if day == 0 or day == 6:
            return '10:00'
        else:
            return '7:00'
    else:
        if day == 0 or day == 6:
            return 'off'
        else:
            return "10:00"

print()
print(alarm_clock(1, False))
print(alarm_clock(5, False))
print(alarm_clock(0, False))

###################################################

def love6(a, b):
    if a == 6 or b == 6:
        return True
    else:
        if a + b == 6 or a - b == 6 or b - a == 6:
            return True
        else:
            return False

print()
print(love6(6, 4))
print(love6(4, 5))
print(love6(1, 5))

###################################################

def in1to10(n, outside_mode):
    if outside_mode == False:
        if 1 <= n <= 10:
            return True
        else:
            return False
    else:
        if 1 < n < 10:
            return False
        else:
            return True

print()
print(in1to10(5, False))
print(in1to10(11, False))
print(in1to10(11, True))

###################################################

def near_ten(num):
    if num % 10 <= 2 or num % 10 >= 8:
        return True
    else:
        return False

print()
print(near_ten(12))
print(near_ten(17))
print(near_ten(19))

###################################################

def double_char(str):
    for i in range(len(str)):
        return str[i]*2

print()
print(double_char('The'))
print(double_char('AAbb'))
print(double_char('Hi-There'))

###################################################

def lone_sum(a, b, c):
    if a != b and a != c and b != c:
        return a + b + c
    elif a == b and a != c:
        return c
    elif a == c and a != b:
        return b
    elif b == c and a != b:
        return a
    else:
        return 0

print()
print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))
print(lone_sum(9, 2, 2))

###################################################

def no_teen_sum(a, b, c):
    a = fix_teen(a)
    b = fix_teen(b)
    c = fix_teen(c)
    return a + b + c


def fix_teen(n):
    if 13 <= n <= 19:
        if n in {15, 16}:
            n = n
            return n
        else:
            n = 0
            return n
    return n


print()
print(no_teen_sum(1, 2, 3))
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))

###################################################

