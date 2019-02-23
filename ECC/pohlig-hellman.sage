M = <prime field>
A = <a coefficient>
B = <b coefficient>
F = FiniteField(M)
E = EllipticCurve(F,[A,B])

P = (x, y)
Q = (x, y)

P = E.point(P)
Q = E.point(Q)

factor(E.order())

primes = [eval(x.strip().replace('^',"**")) for x in str(factor(E.order())).split('*')]
dlogs = []
for fac in primes:
    t = int(P.order()) / int(fac)
    dlog = discrete_log(t*aQ,t*P,operation="+")
    dlogs += [dlog]

l = crt(dlogs, primes)

# Should be true
Q = l*P
