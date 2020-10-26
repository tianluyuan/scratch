"""
A collection of solutions to common interview problems.
"""

def permute_string(string):
    """ Returns a list of all possible permutations of string
    """
    if len(string) == 1:
        return [string]

    permuted = []
    used_chars = []
    for idx, char in enumerate(string):
        # skip if dupe
        if char in used_chars:
            continue
        used_chars.append(char)

        substring = string[0:idx]+string[idx+1:]
        for permuted_substring in permute_string(substring):
            permuted.append(char+permuted_substring)

    return permuted


def rand7_optimized():
    """ Given rand5 implement rand7 using bitvector
    """
    from random import randint

    bitvect = (int(randint(0,5) < 3),
               int(randint(0,5) < 3),
               int(randint(0,5) < 3))

    return(int('{}{}{}'.format(*bitvect),2))


def rand7():
    """ Given rand5 implement rand7
    """
    from random import randint

    count = 0
    rand7_dict = {}
    for i in range(6):
        for j in range(6):
            rand7_dict[(i, j)] = count
            count += 1

    rand5_tup = (randint(0,5), randint(0,5))
    while rand7_dict[rand5_tup] >= 32:
        rand5_tup = (randint(0,5), randint(0,5))

    return rand7_dict[rand5_tup] % 8


class bst(object):
    """ Implementation of bst
    """
    @staticmethod
    def min_node(node):
        while node.left is not None:
            node = node.left
        return node
    

    @staticmethod
    def search(node, number):
        if number == node.value:
            return node
        elif number < node.value and node.left is not None:
            return bst.search(node.left, number)
        elif number > node.value and node.right is not None:
            return bst.search(node.right, number)            
        else:
            return


    def __init__(self, num):
        self.left = None
        self.right = None
        self.parent = None
        
        self.value = num

        
    def add(self, number):
        if self.value is None:
            self.value = number
        elif number <= self.value:
            if self.left is None:
                self.left = bst(number)
                self.left.parent = self
            else:
                self.left.add(number)
        else:
            if self.right is None:
                self.right = bst(number)
                self.left.parent = self
            else:
                self.right.add(number)

                
    def remove(self, node):
        if node.parent:
            if node.parent.value > node.value:
                node.parent.left = None
            else:
                node.parent.right = None
        else:
            node.value = None


    def update_parent(self, parent, node):
        if parent.value < node.value:
            parent.right = node
        else:
            parent.left = node

            
    def delete(self, number):
        node = bst.search(self, number)
        if node is not None:
            if node.left is None and node.right is None:
                self.remove(node)
            elif node.left is not None and node.right is not None:
                min_node = bst.min_node(node.right)
                node.value = min_node.value
                self.remove(min_node)
            elif node.left is None:
                self.update_parent(node.parent, node.right)
            elif node.right is None:
                self.update_parent(node.parent, node.left)


# Carbon1
def memoize(func):
    import functools
    dd = {}
    @functools.wraps(func)
    def func_wrapped(*args, **kwargs):
        if args not in dd:
            dd[args] = func(*args, **kwargs)
        return dd[args]

    return func_wrapped


@memoize
def evens(x):
    """ returns true if int x has even number of 1s in binary
    """
    if not x:
        return True
    return bool(x % 2 ^ evens(x/2))


# Carbon2
@memoize
def sieve(upto):
    """ The sieve algorithm to get all primes less than 'upto'
    """
    from math import sqrt
    primes = [2]
    possibles = list(range(3, upto, 2))
    while primes[-1] < sqrt(upto):
        primes.append(possibles[0])
        possibles = [x for x in possibles if x % primes[-1]]

    return primes + possibles


def mod_exp(m, e, n):
    """ 
    m (int): base
    e (int): exponent
    n (int): modulo

    Perform modulo exponentiation

    Returns m**e (mod n)
    """
    c = 1
    for i in range(e):
        c = (c*m) % n
    return c


def encrypt(msg):
    """
    msg (str): string to be encrypted

    Encrypts a string *msg* using RSA-based approach

    Returns tuple with public modulo, private key, and encrypted message array
    """
    import random
    lmsg = list(map(ord, msg))
    primes = sieve(1000)[1:]
    
    p = primes[random.randint(0, len(primes)-1)]
    primes.remove(p)
    q = primes[random.randint(0, len(primes)-1)]
    n = p*q
    phi = (p-1)*(q-1)
    e = max(q,p)
    for pr in primes:
        if phi % pr:
            e = pr
            break
    for d in range(e, phi, 2):
        if (e*d) % phi == 1:
            break
    return n, d, [mod_exp(imsg, e, n) for imsg in lmsg]


def decrypt(enc):
    """
    enc (tuple): first element is public key, second element is
    private key, third element the encrypted message array

    Returns decrypted message (str)
    """
    return ''.join([chr(mod_exp(ienc, enc[1], enc[0])) for ienc in enc[2]])
