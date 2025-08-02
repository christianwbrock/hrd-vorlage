import math

import matplotlib.pyplot as plt

from scripts.stars import get_star_list, sun_mag, sun_temp


def empty():
    fig, ax = plt.subplots(figsize=(175 / 25, 250 / 25))
    _plot_empty(ax)
    plt.savefig("hrd_empty.png", dpi=300, bbox_inches='tight')


def full():
    fig, ax = plt.subplots(figsize=(175 / 25, 250 / 25))
    _plot_empty(ax)
    _plot_stars(ax, get_star_list())

    plt.savefig("hrd_with_stars.png", dpi=300, bbox_inches='tight')


def _plot_stars(ax, stars):
    size_of_smallest = 5  # smallest marker size
    base = 2
    smallest_star = min(star.diameter for star in stars)
    thres = size_of_smallest - math.log(smallest_star, base)

    for star in stars:
        ax.plot(star.temp, star.mag, 'o', markeredgecolor='black', markerfacecolor=star.color,
                label=star.description, markersize=thres + math.log(star.diameter, base))

    # Plot the sun
    ax.axhline(y=sun_mag, color='orange', linestyle='--', label='Sonne')
    ax.axvline(x=sun_temp, color='orange', linestyle='--')


def _plot_empty(ax):
    ax.set_title("Hertzsprung-Russell Diagram")
    ax.set_xlabel("Temperature (K)")
    ax.set_ylabel("Absolute brightness (magnitude)")

    ax.set_xscale('log')
    ax.set_xlim(35000, 2800)
    temps = [30000, 20000, 15000, 10000, 7000, 6000, 5000, 4000, 3000]
    ax.set_xticks(temps, labels=[f"{t}" for t in temps])
    plt.setp(ax.get_xticklabels(), rotation=45)

    ax.set_ylim((16.5, -9.5))
    mags = list(range(16, -9, -2))
    ax.set_yticks(mags, labels=[f"{m}" for m in mags])
    ax.grid()
