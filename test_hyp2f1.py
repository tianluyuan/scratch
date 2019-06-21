import timeit
import numpy as np
from mpmath import hyp2f1 as mph2f1
from mpmath import mp
from scipy.special import hyp2f1, gammaln, poch, gamma, eval_jacobi
import tqdm


def trans_15_3_3(a,b,c,z):
    return np.exp((c-a-b) * np.log(1-z) +np.log(hyp2f1(c-a, c-b, c, z)))


def trans_15_3_4(a,b,c,z):
    return (1-z)**(-a)*hyp2f1(a,c-b,c,z/(z-1))


def trans_15_3_6(a,b,c,z):
    # print a,b,a+b-c+1, 1-z, hyp2f1(a,b,a+b-c+1, 1-z), mph2f1(a,b,a+b-c+1, 1-z)
    return np.exp(pochln2(c-b, -a)+gammaln(c)-gammaln(c-a))*hyp2f1(a,b,a+b-c+1, 1-z)# +
                # np.exp((c-a-b) * np.log(1-z)+gammaln(c)+gammaln(a+b-c)-gammaln(a)-gammaln(b))*hyp2f1(c-a,c-b,c-a-b+1,1-z))


def trans_15_3_7(a,b,c,z):
    return (np.exp(-a * np.log(-z)+gammaln(c)+gammaln(b-a)-gammaln(b)-gammaln(c-a))*hyp2f1(a,1-c+a,1-b+a,1/z)+
                np.exp(-b * np.log(-z)+gammaln(c)+gammaln(a-b)-gammaln(a)-gammaln(c-b))*hyp2f1(b,1-c+b,1-a+b,1/z))


def trans_15_3_8(a,b,c,z):
    return (np.exp(-a * np.log(1-z)+gammaln(c)+gammaln(b-a)-gammaln(b)-gammaln(c-a))*hyp2f1(a,c-b,a-b+1,1/(1-z))+
                np.exp(-b * np.log(1-z)+gammaln(c)+gammaln(a-b)-gammaln(a)-gammaln(c-b))*hyp2f1(b,c-a,b-a+1,1/(1-z)))


def trans_15_3_9(a,b,c,z):
    return (np.exp(-a * np.log(z)+gammaln(c)+gammaln(c-b-a)-gammaln(c-b)-gammaln(c-a))*hyp2f1(a,a-c+1,a+b-c+1,1-1/z)+
                np.float_power(z,a-c)*np.exp((c-a-b) * np.log(1-z)+gammaln(c)+gammaln(a+b-c)-gammaln(a)-gammaln(b))*hyp2f1(c-a,1-a,c-a-b+1,1-1/z))


def pochln(z,m):
    return gammaln(z+m)-gammaln(z)


def pochln2(z,m):
    assert z<0 and z+m <0
    return gammaln(-z+1)-gammaln(-z-m+1)


def poch_sum_15_4_1(a,b,c,z):
    m = -a
    n = np.arange(m+1)
    return np.sum(poch(-m,n)*poch(b,n)*z**n/(poch(c,n)*gamma(n+1)))


def poch_sum_ln_15_4_1(a,b,c,z):
    m = -a
    n = np.arange(m+1)
    return np.sum(poch(-m,n)*z**n*np.exp(pochln(b,n)-gammaln(n+1))/poch(c,n))


def jacobi_15_4_6(a,b,c,z):
    n = -a
    alpha = c-1
    beta = b-n-alpha-1

    return np.exp(gammaln(n+1)-pochln(alpha+1,n))*eval_jacobi(n,alpha,beta,1-2*z)


from functools32 import lru_cache

@lru_cache(maxsize=None)
def recura(a,b,c,z):
    if not z < 0:
        return hyp2f1(a,b,c,z)
    if a>-39:
        return hyp2f1(a,b,c,z)

    a += 1
    return ((a*(1-z))*recura(a+1,b,c,z)-(2*a-c+(b-a)*z) * recura(a,b,c,z))/(c-a)

b=36.5
ll=0
z = -0.5
st = 40
en = 160
step = 2

start = timeit.default_timer()
mpout = [mph2f1(-_, b, -_-ll-1/2., z) for _ in range(st, en,step)]
end = timeit.default_timer()
print 'mpmath took', end-start

start = timeit.default_timer()
spout = [hyp2f1(-_, b, -_-ll-1/2., z) for _ in range(st, en,step)]
end = timeit.default_timer()
print 'scipy took', end-start

start = timeit.default_timer()
tfout = [trans_15_3_6(-_, b, -_-ll-1/2., z) for _ in range(st, en,step)]
end = timeit.default_timer()
print 'scipy transformed took', end-start

start = timeit.default_timer()
psout = [poch_sum_ln_15_4_1(-_, b, -_-ll-1/2., z) for _ in range(st, en,step)]
end = timeit.default_timer()
print 'scipy pochsum took', end-start

start = timeit.default_timer()
rrout = [recura(-_, b, -_-ll-1/2., z) for _ in range(st, en,step)]
end = timeit.default_timer()
print 'scipy recura took', end-start


print 'mpmath    scipy    transformed    pochsum    recura'
for m, s, t, p, j in zip(mpout, spout, tfout, psout, rrout):
    print m, s, t, p, j


from itertools import product
lls = range(0,200,4)
kks = range(0,200,4)
jjs = range(30, 41, 1)
ms = np.linspace(-0.99,0.99,51)
# mp.dps = 80
for jj, kk, ll, m in tqdm.tqdm(product(jjs, kks, lls, ms), total=len(lls)*len(kks)*len(jjs)*len(ms)):
    mh = mph2f1(-jj, kk+0.5, 0.5-jj-ll, -m)
    relerr = (mh-hyp2f1(-jj, kk+0.5, 0.5-jj-ll, -m))/mh
    if relerr > 0.05:
        print -jj, kk+0.5, 0.5-jj-ll, -m, relerr
        # break
