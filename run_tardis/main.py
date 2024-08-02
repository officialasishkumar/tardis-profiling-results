from tardis import run_tardis
from tardis.io.configuration.config_reader import Configuration
from tardis.io.atom_data import AtomData
from tardis.io.configuration.config_internal import get_data_dir


if __name__ == "__main__":
    config = Configuration.from_yaml("../data/tardis_configv1_verysimple.yml")
    config.montecarlo.tracking.track_rpacket = True
    data_dir = get_data_dir()
    atomic_data_fname = (
        f"{data_dir}/kurucz_cd23_chianti_H_He.h5"
    )
    atom_data = AtomData.from_hdf(atomic_data_fname)
    run_tardis(config, atom_data)