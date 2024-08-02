import tardis.transport.montecarlo.interaction as interaction
from astropy import units as u
from tardis.io.atom_data import AtomData
from tardis.io.configuration.config_internal import get_data_dir
from tardis.simulation import Simulation
from tardis.transport.montecarlo import RPacket
from tardis.transport.montecarlo.numba_interface import opacity_state_initialize

if __name__ == "main":
    packet = RPacket(
        r=7.5e14,
        nu=0.4,
        mu=0.8599443103322428,
        energy=0.9114437898710559,
        seed=1963,
        index=0,
    )
    data_dir = get_data_dir()
    atomic_data_fname = f"{data_dir}/kurucz_cd23_chianti_H_He.h5"
    atomic_data = AtomData.from_hdf(atomic_data_fname)
    sim = Simulation.from_config(
        "../data/tardis_configv1_verysimple.yml", atom_data=atomic_data
    )
    opacity_state = opacity_state_initialize(
        sim.plasma,
        line_interaction_type="macroatom",
        disable_line_scattering=sim.transport.montecarlo_configuration.DISABLE_LINE_SCATTERING,
    )
    packet.initialize_line_id(opacity_state, 13 * u.day, True)
    interaction.line_emission(packet, 1000, 13 * u.day, opacity_state, True)
