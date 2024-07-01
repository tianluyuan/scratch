import numpy as np
from matplotlib import pyplot as plt

RR = 1
RZ = 2

def intersect(rr, rz, opos, odir, dpos):
    pos = dpos - opos
    pos[2] *= rr/rz
    dir = np.copy(odir)
    dir[2] *= rr/rz
    dr2 = np.dot(pos, pos)
    urdot = np.dot(pos, dir/np.linalg.norm(dir))

    discr = urdot**2 - dr2 + rr**2
    if discr < 0:
        return None

    discr = np.sqrt(discr)

    if urdot + discr < 0:
        return None

    smin1 = urdot - discr
    smin1 /= np.linalg.norm(dir)
    return opos + odir * smin1


if __name__ == '__main__':
    fig, axs = plt.subplots(2, 2)
    for _ in axs:
        for ax in _:
            ax.axis('equal')
    axs[1, 1].remove()
    axs[1, 1] = fig.add_subplot(2, 2, 4, projection='3d')

    dompos = np.random.uniform(-5, 5, 3)
    for i in range(5000):
        pos = np.random.uniform(-5, 5, 3)
        dir = np.random.uniform(-1, 1, 3)
        dir /= np.linalg.norm(dir)
        assert np.abs(np.linalg.norm(dir)-1.) < 1e-8
        isc = intersect(RR, RZ, pos, dir, dompos)
        if isc is None:
            continue
        axs[0, 0].scatter(isc[0], isc[1], marker='.', s=1, c=isc[2], cmap='coolwarm', vmin=-RZ+dompos[2], vmax=RZ+dompos[2])
        axs[0, 1].scatter(isc[0], isc[2], marker='.', s=1, c=isc[1], cmap='coolwarm', vmin=-RR+dompos[1], vmax=RR+dompos[1])
        axs[1, 0].scatter(isc[1], isc[2], marker='.', s=1, c=isc[0], cmap='coolwarm', vmin=-RR+dompos[0], vmax=RR+dompos[0])
        axs[1, 1].scatter(*isc, marker='.', color='k', s=1)
        rmax = max(RR, RZ)
        axs[1, 1].set_xlim((-rmax+dompos[0])*1.1, (rmax+dompos[0])*1.1)
        axs[1, 1].set_ylim((-rmax+dompos[1])*1.1, (rmax+dompos[1])*1.1)
        axs[1, 1].set_zlim((-rmax+dompos[2])*1.1, (rmax+dompos[2])*1.1)

    plt.show()
