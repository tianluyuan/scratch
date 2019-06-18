import timeit
import numpy as np
from mpmath import hyp2f1 as mph2f1
from scipy.special import hyp2f1, gammaln, poch, gamma, eval_jacobi


def trans_15_3_3(a,b,c,z):
    return np.exp((c-a-b) * np.log(1-z) +np.log(hyp2f1(c-a, c-b, c, z)))


def trans_15_3_4(a,b,c,z):
    return (1-z)**(-a)*hyp2f1(a,c-b,c,z/(z-1))


def trans_15_3_6(a,b,c,z):
    return (np.exp(gammaln(c)+gammaln(c-a-b)-gammaln(c-b)-gammaln(c-a))*hyp2f1(a,b,a+b-c+1, 1-z)+
                np.exp((c-a-b) * np.log(1-z)+gammaln(c)+gammaln(a+b-c)-gammaln(a)-gammaln(b))*hyp2f1(c-a,c-b,c-a-b+1,1-z))


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


def poch_sum_15_4_1(a,b,c,z):
    m = -a
    n = np.arange(m+1)
    return np.sum(poch(-m,n)*poch(b,n)*z**n/(poch(c,n)*gamma(n+1)))


def poch_sum_ln_15_4_1(a,b,c,z):
    m = -a
    n = np.arange(m+1)
    return np.exp(pochln(-m,n)+pochln(b,n)+n*np.log(z)-pochln(c,n)-gammaln(n+1)).sum()


def jacobi_15_4_6(a,b,c,z):
    n = -a
    alpha = c-1
    beta = b-n-alpha-1

    return np.exp(gammaln(n+1)-pochln(alpha+1,n))*eval_jacobi(n,alpha,beta,1-2*z)


b=36.5
z = -1/2.
st = 120
en = 160

start = timeit.default_timer()
mpout = [mph2f1(-_, b, -_-1/2., z) for _ in range(st, en,2)]
end = timeit.default_timer()
print 'mpmath took', end-start

start = timeit.default_timer()
spout = [hyp2f1(-_, b, -_-1/2., z) for _ in range(st, en,2)]
end = timeit.default_timer()
print 'scipy took', end-start

start = timeit.default_timer()
tfout = [trans_15_3_7(-_, b, -_-1/2., z) for _ in range(st, en,2)]
end = timeit.default_timer()
print 'scipy transformed took', end-start

start = timeit.default_timer()
jbout = [jacobi_15_4_6(-_, b, -_-1/2., z) for _ in range(st, en,2)]
end = timeit.default_timer()
print 'scipy jacobi took', end-start


print 'mpmath    scipy    transformed    jacobi'
for m, s, t, j in zip(mpout, spout, tfout, jbout):
    print m, s, t, j
