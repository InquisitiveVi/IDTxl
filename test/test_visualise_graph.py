"""Provide unit tests for plotting functionality.

Created on Thu Jun  8 07:58:02 2017

@author: patricia
"""
from idtxl.multivariate_te import MultivariateTE
from idtxl.data import Data
from idtxl.visualise_graph import print_res_to_console


def test_console_output():
    dat = Data()
    dat.generate_mute_data(n_samples=10, n_replications=5)
    nw = MultivariateTE(max_lag_sources=5,
                        min_lag_sources=4,
                        options={'cmi_estimator': 'JidtKraskovCMI'},
                        max_lag_target=5)

    # Test all to all analysis
    r = nw.analyse_network(dat, targets='all', sources='all')

    print_res_to_console(r, fdr=False)


if __name__ == '__main__':
    test_console_output()

