from tardis.io.atom_data import AtomData
from tardis.io.configuration.config_internal import get_data_dir
from tardis.opacities.opacity_state import opacity_state_initialize
from tardis.simulation import Simulation

if __name__ == "main":
    data_dir = get_data_dir()
    atomic_data_fname = f"{data_dir}/kurucz_cd23_chianti_H_He.h5"
    atomic_data = AtomData.from_hdf(atomic_data_fname)
    sim = Simulation.from_config(
        "../data/tardis_configv1_verysimple.yml", atom_data=atomic_data
    )
    opacity_state_initialize(sim.plasma, "macroatom")