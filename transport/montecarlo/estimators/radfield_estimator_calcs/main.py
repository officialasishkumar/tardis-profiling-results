import numpy as np
from tardis.transport.montecarlo import RPacket
from tardis.transport.montecarlo.estimators import radfield_mc_estimators
from tardis.transport.montecarlo.estimators.radfield_estimator_calcs import (
    update_line_estimators,
)

if __name__ == "main":
    estimator = radfield_mc_estimators.RadiationFieldMCEstimators(
        j_estimator=np.array([0.0, 0.0], dtype=np.float64),
        nu_bar_estimator=np.array([0.0, 0.0], dtype=np.float64),
        j_blue_estimator=np.array([[0.0, 0.0, 0.0], [0.0, 0.0, 0.0]], dtype=np.float64),
        Edotlu_estimator=np.array([[0.0, 0.0, 1.0], [0.0, 0.0, 1.0]], dtype=np.float64),
        photo_ion_estimator=np.empty((0, 0), dtype=np.float64),
        stim_recomb_estimator=np.empty((0, 0), dtype=np.float64),
        bf_heating_estimator=np.empty((0, 0), dtype=np.float64),
        stim_recomb_cooling_estimator=np.empty((0, 0), dtype=np.float64),
        photo_ion_estimator_statistics=np.empty((0, 0), dtype=np.int64),
    )
    packet = RPacket(
        r=7.5e14,
        nu=0.4,
        mu=0.3,
        energy=0.9,
        seed=1963,
        index=0,
    )
    update_line_estimators(estimator, packet, 1, 1e12, 1e10, True)
