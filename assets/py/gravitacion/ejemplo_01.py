import matplotlib.pyplot as plt
from matplotlib.patches import Arc

plt.rcParams['text.usetex'] = True

DPI = 1000
BACKGROUND_COLOR = "#27262b"
IMAGE_PATH = "assets/images/gravitacion/"


fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(4.0, 3.0))

ax.spines[['right', 'top', "left", "bottom"]].set_visible(False)
ax.set_xticks([])
ax.set_yticks([])

c1 = plt.Circle((2, 0), 0.05, color="white")
ax.add_patch(c1)
ax.annotate("", xy=(1.5, -0.5), xytext=(2, 0),
            arrowprops=dict(arrowstyle="-|>", color="white", lw=0.5))
ax.text(1.4, -0.4, r"$v_0$", color="white", fontsize=6,
        ha="center", va="center")
ax.text(2.2, 0, r"$m$", color="white", fontsize=6,
        ha="center", va="center")

c2 = plt.Circle((-2, 0), 0.05, color="white")
ax.add_patch(c2)
ax.annotate("", xy=(-1.5, 0.5), xytext=(-2, 0),
            arrowprops=dict(arrowstyle="-|>", color="white", lw=0.5))
ax.text(-1.4, 0.4, r"$v_0$", color="white", fontsize=6,
        ha="center", va="center")
ax.text(-2.2, 0, r"$m$", color="white", fontsize=6,
        ha="center", va="center")

ax.plot([-2, 2], [0, 0], c="white", ls="--", lw=0.5)
ax.annotate("", xy=(-2.05, 1), xytext=(2.05, 1),
            arrowprops=dict(arrowstyle="<|-|>", color="white", lw=0.5))
ax.plot([-2, -2], [0, 1], c="white", ls="--", lw=0.5)
ax.plot([2, 2], [0, 1], c="white", ls="--", lw=0.5)
ax.text(0, 1.1, r"$d$", color="white", fontsize=6, ha="center", va="center")

ax.add_patch(Arc(xy=(-2, 0), width=0.75, height=0.75,
                 theta1=0, theta2=45, color="white", lw=0.5))
ax.text(-1.75, 0.1, r"$\alpha$", color="white", fontsize=6,
        ha="center", va="center")

ax.add_patch(Arc(xy=(2, 0), width=0.75, height=0.75,
                 theta1=180, theta2=180 + 45, color="white", lw=0.5))
ax.text(1.75, -0.1, r"$\alpha$", color="white", fontsize=6,
        ha="center", va="center")

ax.set_xlim(-2.5, 2.5)
ax.set_ylim(-1.0, 1.5)
ax.set_aspect("equal")

plt.savefig(f"{IMAGE_PATH}fig_01.png", pad_inches=0.02, dpi=DPI,
            transparent=True)
plt.close(fig)
