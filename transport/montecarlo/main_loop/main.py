import tardis.transport.montecarlo.interaction as interaction
from astropy import units as u
from tardis.io.atom_data import AtomData
from tardis.io.configuration.config_internal import get_data_dir
from tardis.simulation import Simulation
from tardis.transport.montecarlo import RPacket, packet_trackers
from tardis.transport.montecarlo.configuration.base import MonteCarloConfiguration
from tardis.transport.montecarlo.montecarlo_main_loop import montecarlo_main_loop
from tardis.transport.montecarlo.numba_interface import opacity_state_initialize

if __name__ == "main":
    data_dir = get_data_dir()
    atomic_data_fname = f"{data_dir}/kurucz_cd23_chianti_H_He.h5"
    atomic_data = AtomData.from_hdf(atomic_data_fname)
    sim = Simulation.from_config(
        "../data/tardis_configv1_verysimple.yml", atom_data=atomic_data
    )
    transport_state = sim.transport.transport_state
    packet_collection = transport_state.packet_collection
    geometry_state = transport_state.geometry_state
    time_explosion = 13 * u.day
    opacity_state = transport_state.opacity_state
    estimator = transport_state.radfield_mc_estimators
    rpacket_tracker_list = (
        packet_trackers.generate_rpacket_last_interaction_tracker_list(
            len(transport_state.packet_collection.initial_nus)
        )
    )
    montecarlo_config = MonteCarloConfiguration()

    montecarlo_main_loop(
        packet_collection,
        geometry_state,
        time_explosion,
        opacity_state,
        montecarlo_config,
        estimator,
        sim.transport.spectrum_frequency_grid.value,
        montecarlo_config.NUMBER_OF_VPACKETS,
        iteration=0,
        show_progress_bars=False,
        total_iterations=0,
    )
