import numpy as np
from scipy.integrate import dblquad
from functools import cache
from sphere.distribution import fb84

k=68
b=10
n1,n2,n3=0.4,np.sqrt(1-0.4**2),0
m=-1
FB8 = fb84(np.asarray([[1,0,0],[0,1,0],[0,0,1]]),
           k,b,m,np.asarray([n1,n2,n3]))


def normalize():
    return FB8.normalize(cache=dict())


# @cache
def _integrand(th, ph):
    cth = np.cos(th)
    sth = np.sin(th)
    cph = np.cos(ph)
    sph = np.sin(ph)
    return sth*np.exp(k*(n1*cth+n2*sth*cph+n3*sth*sph)+b*sth**2*(cph**2-m*sph**2))


def _integrand2(th, ph):
    return np.sin(th)*np.exp(k*(n1*np.cos(th)+n2*np.sin(th)*np.cos(ph)+n3*np.sin(th)*np.sin(ph))+b*np.sin(th)**2*(np.cos(ph)**2-m*np.sin(ph)**2))


def integral(integrandfn):
    return dblquad(integrandfn,
                   0., 2.*np.pi, lambda x: 0., lambda x: np.pi,
                   epsabs=1e-3, epsrel=1e-3)[0]


def integral_lambda():
    return dblquad(
        lambda th, ph: np.sin(th)*\
        np.exp(k*(n1*np.cos(th)+n2*np.sin(th)*np.cos(ph)+n3*np.sin(th)*np.sin(ph))+\
               b*np.sin(th)**2*(np.cos(ph)**2-m*np.sin(ph)**2)),
               0., 2.*np.pi, lambda x: 0., lambda x: np.pi,
               epsabs=1e-3, epsrel=1e-3)[0]
