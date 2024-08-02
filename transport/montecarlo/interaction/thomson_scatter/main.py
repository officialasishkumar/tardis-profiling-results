import tardis.transport.montecarlo.interaction as interaction
from tardis.transport.montecarlo import RPacket
from astropy import units as u

if __name__ == "main":
    packet = RPacket(
        r=7.5e14,
        nu=0.4,
        mu=0.3,
        energy=0.9,
        seed=1963,
        index=0,
    )
    interaction.thomson_scatter(packet, 13*u.day, True)
