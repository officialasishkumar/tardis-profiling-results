import numpy as np
import tardis.transport.montecarlo.interaction as interaction
from astropy import units as u
from numba.np.ufunc.parallel import get_num_threads, get_thread_id
from tardis.io.atom_data import AtomData
from tardis.io.configuration.config_internal import get_data_dir
from tardis.simulation import Simulation
from tardis.transport.montecarlo import RPacket, single_packet_loop
from tardis.transport.montecarlo.configuration.base import MonteCarloConfiguration
from tardis.transport.montecarlo.numba_interface import opacity_state_initialize
from tardis.transport.montecarlo.packet_collections import VPacketCollection
from tardis.transport.montecarlo.packet_trackers import RPacketTracker

if __name__ == "main":
    packet = RPacket(
        r=7.5e14,
        nu=0.4,
        mu=0.3,
        energy=0.9,
        seed=1963,
        index=0,
    )

    data_dir = get_data_dir()
    atomic_data_fname = f"{data_dir}/kurucz_cd23_chianti_H_He.h5"
    atomic_data = AtomData.from_hdf(atomic_data_fname)
    sim = Simulation.from_config(
        "../data/tardis_configv1_verysimple.yml", atom_data=atomic_data
    )

    numba_radial_1d_geometry = sim.simulation_state.geometry.to_numba()

    opacity_state = opacity_state_initialize(
        sim.plasma,
        line_interaction_type="macroatom",
        disable_line_scattering=sim.transport.montecarlo_configuration.DISABLE_LINE_SCATTERING,
    )

    spectrum_frequency_grid = sim.transport.spectrum_frequency_grid.value

    rpacket_tracker = RPacketTracker(0)

    montecarlo_config = MonteCarloConfiguration

    estimator = (
        sim.transport.transport_state.radfield_mc_estimators.create_estimator_list(
            get_num_threads()
        )[get_thread_id()]
    )

    vpacket_collection = VPacketCollection(
        source_rpacket_index=0,
        spectrum_frequency_grid=spectrum_frequency_grid,
        number_of_vpackets=3,
        v_packet_spawn_start_frequency=0,
        v_packet_spawn_end_frequency=np.inf,
        temporary_v_packet_bins=0,
    )

    single_packet_loop.single_packet_loop(
        packet,
        numba_radial_1d_geometry,
        13 * u.day,
        opacity_state,
        estimator,
        vpacket_collection,
        rpacket_tracker,
        montecarlo_config,
    )
