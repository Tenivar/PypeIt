# Module to run tests on WaveImage class
#   Requires files in Development suite and an Environmental variable
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

# TEST_UNICODE_LITERALS

import os

import pytest
import glob
import numpy as np

from pypeit.tests.tstutils import dev_suite_required, load_kast_blue_masters
from pypeit import waveimage


def data_path(filename):
    data_dir = os.path.join(os.path.dirname(__file__), 'files')
    return os.path.join(data_dir, filename)


@dev_suite_required
def test_build_me():
    # Masters
    spectrograph, tslits_dict, tilts_dict, wv_calib \
            = load_kast_blue_masters(get_spectrograph=True, tslits=True, tilts=True, wvcalib=True)
    # Instantiate
    setup = 'A_01_aa'
    root_path = data_path('MF') if os.getenv('PYPEIT_DEV') is None \
                    else os.path.join(os.getenv('PYPEIT_DEV'), 'Cooked', 'MF')
    master_dir = root_path+'_'+spectrograph.spectrograph
    mode = 'reuse'
    nslits = tslits_dict['lcen'].shape[1]
    maskslits = np.zeros(nslits, dtype=bool)
    slitmask = spectrograph.slitmask(tslits_dict)
    pytest.set_trace()
    wvImg = waveimage.WaveImage(tilts_dict['tilts'], wv_calib, spectrograph, setup=setup,
                                maskslits=maskslits, master_dir=master_dir, mode=mode)
    # Build
    wave = wvImg._build_wave()
    assert int(np.max(wave)) == 5516

