import func


def do(c, r):
    n_file = open('res.txt', 'a')
    n_file.write("dotuch\n")
    i = 0
    buf = 2.
    while abs(func.f(c)) > func.e or abs(buf - c) > func.e:
        buf = c
        if func.df(c) == 0.:
            break
        c = c - func.f(c)/func.df(c)
        i += 1
        n_file.write('nabluzh=' + str(c) + ' f(x)=' + str(func.f(c)) + "\n")
    n_file.write(str(r) + " answer: " + str(c) + " " + str(i) + "iterations\n")
    n_file.close()
    return c
