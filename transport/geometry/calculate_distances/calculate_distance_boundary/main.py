import numpy as np
import tardis.transport.geometry.calculate_distances as calculate_distances
from tardis.model.geometry.radial1d import NumbaRadial1DGeometry

if __name__ == "main":
    geometry = NumbaRadial1DGeometry(
        r_inner=np.array([6.912e14, 8.64e14], dtype=np.float64),
        r_outer=np.array([8.64e14, 1.0368e15], dtype=np.float64),
        v_inner=np.array([-1, -1], dtype=np.float64),
        v_outer=np.array([-1, -1], dtype=np.float64),
    )
    calculate_distances.calculate_distance_boundary(
        0.3, 7.5e14, geometry.r_inner[0], geometry.r_outer[0]
    )
