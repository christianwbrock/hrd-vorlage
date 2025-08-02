from scripts import plot_hrd


def test_plot_empty(disable_plots):
    plot_hrd.empty()


def test_plot_full(disable_plots):
    plot_hrd.full()
