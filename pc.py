from numpy import zeros, linspace

import matplotlib.pyplot as plt





def s(beta,s,i):
        return -beta*s*i

def i(beta,gama,s,i):
        return beta*s*i-gama*i;

def r(gama,i):
        return gama*i;

beta = 0.001;
gamma = 0.003;
dt = 0.1  # 6 min
D = 30  # Simulate for D days
N_t = int(D * 24 / dt)  # Corresponding no of hours
t = linspace(0, N_t*dt, N_t+1)
S = zeros(N_t + 1)
I = zeros(N_t + 1)
R = zeros(N_t + 1)
h=0.1
# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0
s1 = s2 = s3 = 0
i1 = i2 = i3 = 0
r1 = r2 = r3 = 0

for j in range(N_t):
    k1 = h * s(beta, S[j], I[j])
    k2 = h * s(beta, S[j] + 0.5 * k1, I[j])
    k3 = h * s(beta, S[j] + 0.5 * k2, I[j])
    k4 = h * s(beta, S[j] + k3, I[j])
    S[j + 1] = S[j] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0

    k1 = h * i(beta, gamma, S[j], I[j])
    k2 = h * i(beta, gamma, S[j], I[j] + 0.5 * k1)
    k3 = h * i(beta, gamma, S[j], I[j] + 0.5 * k2)
    k4 = h * i(beta, gamma, S[j], I[j] + k3)
    I[j + 1] = I[j] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0

    k1 = h * r(gamma, I[j])
    k2 = h * r(gamma, I[j])
    k3 = h * r(gamma, I[j])
    k4 = h * r(gamma, I[j])
    R[j + 1] = R[j] + (k1 + 2.0 * (k2 + k3) + k4) / 6.0



for j in range(min(3, N_t)):
        s0 = s(beta, S[j], I[j]);
        w = S[j] + h * (55.0 * s0 - 59.0 * s1 + 37.0 * s2 - 9.0 * s3) / 24.0
        sw = s(beta,w,I[j])
        S[j + 1] = S[j] + h * (9.0 * sw + 19.0 * s0 - 5.0 * s1 + s2) / 24.0
        s1, s2, s3 = (s0, s1, s2)

        i0 = s(beta, S[j], I[j]);
        i0 = i(beta, gamma, S[j], I[j]);
        w = I[j] + h * (55.0 * i0 - 59.0 * i1 + 37.0 * i2 - 9.0 * i3) / 24.0
        iw = i(beta,gamma,S[j],w)
        I[j + 1] = I[j] + h * (9.0 * iw + 19.0 * i0 - 5.0 * i1 + i2) / 24.0
        i1, i2, i3 = (i0, i1, i2)

        r0 = r(gamma, I[j])
        w = R[j] + h * (55.0 * r0 - 59.0 * r1 + 37.0 * r2 - 9.0 * r3) / 24.0
        rw = r(gamma,I[j])
        R[j + 1] = R[j] + h * (9.0 * rw + 19.0 * r0 - 5.0 * r1 + r2) / 24.0
        r1, r2, r3 = (r0, r1, r2)

fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'upper left')
plt.xlabel('horas')
plt.show()
plt.savefig('tmp.pdf'); plt.savefig('tmp.png')



















































