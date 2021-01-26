from numpy import zeros, linspace

import matplotlib.pyplot as plt





def s(beta,s,i):
        return -beta*s*i

def i(beta,gama,s,i):
        return beta*s*i-gama*i;

def r(gama,i):
        return gama*i;

        # Time unit: 1 h


beta = 0.001;
gamma = 0.003;
dt = 0.1  # 6 min
D = 30  # Simulate for D days
N_t = int(D * 24 / dt)  # Corresponding no of hours
t = linspace(0, N_t*dt, N_t+1)
t = linspace(0, N_t * dt, N_t + 1)
S = zeros(N_t + 1)
I = zeros(N_t + 1)
R = zeros(N_t + 1)
h=0.1
# Initial condition
S[0] = 50
I[0] = 1
R[0] = 0

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
fig = plt.figure()
l1, l2, l3 = plt.plot(t, S, t, I, t, R)
fig.legend((l1, l2, l3), ('S', 'I', 'R'), 'upper left')
plt.xlabel('horas')
plt.show()
plt.savefig('tmp.pdf'); plt.savefig('tmp.png')
