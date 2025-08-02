import pytest


@pytest.fixture(scope="session")
def disable_plots():
    # set inactive backend to avoid displaying the plot
    import matplotlib
    matplotlib.use('Agg')
