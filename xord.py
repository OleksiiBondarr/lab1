import func


def xo(a, b, r):
    n_file = open('res.txt', 'a')
    n_file.write("xord\n")
    i = 0
    c = 1
    buf = 2.
    while abs(buf - c) > func.e or abs(func.f(c)) > func.e:
        buf = c
        c = (a * func.f(b) - b * func.f(a)) / (func.f(b) - func.f(a))
        i += 1
        if func.f(c) == 0.:
            break
        if func.f(a) * func.f(c) < 0.:
            b = c
        else:
            a = c
        n_file.write(" a=" + str(a) + ' f(a)=' + str(func.f(a)) + ' b=' + str(b) + ' f(b)=' + str(func.f(b)) + "\n")
    n_file.write(str(r) + " answer: " + str(c) + " " + str(i) + "iterations\n")
    n_file.close()
    return c
