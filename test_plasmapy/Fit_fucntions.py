import matplotlib.pyplot as plt
import numpy as np

from pathlib import Path

from plasmapy.analysis import fit_functions as ffuncs

plt.rcParams["figure.figsize"] = [10.5, 0.56 * 10.5]

# basic instantiation
explin = ffuncs.ExponentialPlusLinear()

# fit parameters are not set yet
(explin.params, explin.param_errors)

explin.param_names

(explin, explin.__str__(), explin.latex_str)

params = (5.0, 0.1, -0.5, -8.0)  # (a, alpha, m, b)
xdata = np.linspace(-20, 15, num=100)
ydata = explin.func(xdata, *params) + np.random.normal(0.0, 0.6, xdata.size)

explin.curve_fit(xdata, ydata)
(explin.params, explin.params.a, explin.params.alpha)
(explin.param_errors, explin.param_errors.a, explin.param_errors.alpha)
explin.rsq

# plot original data
plt.plot(xdata, ydata, marker="o", linestyle=" ", label="Data")
ax = plt.gca()
ax.set_xlabel("X", fontsize=14)
ax.set_ylabel("Y", fontsize=14)

ax.axhline(0.0, color="r", linestyle="--")

# plot fitted curve + error
yfit, yfit_err = explin(xdata, reterr=True)
ax.plot(xdata, yfit, color="orange", label="Fit")
ax.fill_between(
    xdata,
    yfit + yfit_err,
    yfit - yfit_err,
    color="orange",
    alpha=0.12,
    zorder=0,
    label="Fit Error",
)

# plot annotations
plt.legend(fontsize=14, loc="upper left")

txt = f"$f(x) = {explin.latex_str}$\n" f"$r^2 = {explin.rsq:.3f}$\n"
for name, param, err in zip(explin.param_names, explin.params, explin.param_errors):
    txt += f"{name} = {param:.3f} $\\pm$ {err:.3f}\n"
txt_loc = [-13.0, ax.get_ylim()[1]]
txt_loc = ax.transAxes.inverted().transform(ax.transData.transform(txt_loc))
txt_loc[0] -= 0.02
txt_loc[1] -= 0.05
ax.text(
    txt_loc[0],
    txt_loc[1],
    txt,
    fontsize="large",
    transform=ax.transAxes,
    va="top",
    linespacing=1.5,
)

plt.show()

