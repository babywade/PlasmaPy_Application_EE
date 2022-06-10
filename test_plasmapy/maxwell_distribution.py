import matplotlib.pyplot as plt
import numpy as np

from astropy import units as u
from astropy.constants import k_B, m_e

from plasmapy.formulary import Maxwellian_1D # 1
from plasmapy.formulary import Maxwellian_speed_1D # 和1的关系是二分之一
from astropy.visualization import quantity_support

quantity_support() # 使支持带量纲的参数 

# Maxwellian_1D
# Parameters
# ----------
# v : `~astropy.units.Quantity`
#     The velocity in units convertible to m/s. 速度参数

# T : `~astropy.units.Quantity`
#     The temperature in kelvin. 热力学温度

# particle : `str`, optional
#     Representation of the particle species(e.g., ``'p'`` for protons,
#     ``'D+'`` for deuterium, or ``'He-4 +1'`` for singly ionized
#     helium-4), which defaults to electrons.
# 粒子种类：p是protons质子 D+是deuterium氘 e是电子

# v_drift : `~astropy.units.Quantity`, optional
#     The drift velocity in units convertible to m/s. 粒子漂移速度
p_dens = Maxwellian_1D(v=1 * u.m / u.s, T=30000 * u.K, particle="e", v_drift=0 * u.m / u.s)
print(p_dens)

# 画出速度分布的完全图
T = 3e4 * u.K
dv = 10 * u.m / u.s
v = np.arange(-5e6, 5e6, 10) * u.m / u.s

for particle in ["p", "e"]:
    pdf = Maxwellian_1D(v, T=T, particle=particle)
    integral = (pdf).sum() * dv
    print(f"Integral value for {particle}: {integral}")
    plt.plot(v, pdf, label=particle)
plt.legend()
plt.show()

std = np.sqrt((Maxwellian_1D(v, T=T, particle="e") * v ** 2 * dv).sum())
T_theo = (std ** 2 / k_B * m_e).to(u.K)

print(std)
print("T from standard deviation:", T_theo)
print("Initial T:", T)
