import numpy as np


class ShapeMismatchError(Exception):
    pass


def convert_from_sphere(
    distances: np.ndarray,
    azimuth: np.ndarray,
    inclination: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (distances.shape == azimuth.shape == inclination.shape):
        raise ShapeMismatchError
    
    return (distances * np.sin(inclination)* np.cos(azimuth), 
            distances * np.sin(inclination) * np.sin(azimuth),
            distances * np.cos(inclination))


def convert_to_sphere(
    abscissa: np.ndarray,
    ordinates: np.ndarray,
    applicates: np.ndarray,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    if not (abscissa.shape == ordinates.shape == applicates.shape):
        raise ShapeMismatchError
    
    r = np.sqrt(abscissa**2 + ordinates**2 + applicates**2)
    if np.all(r == 0):
        return False
    if r[r!=0].shape != r.shape:
        mask = r.copy()
        mask[mask!=0] = 1
        mask[mask== 0] = 0
        r[r==0] = 1
        applicates *= mask   
    phi = np.arctan2(ordinates, abscissa)
    teta = np.arccos(applicates / r)
    
    return(r, phi, teta)

print(convert_to_sphere(np.zeros(2), np.zeros(2), np.zeros(2)))