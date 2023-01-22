import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm

from astropy.io import fits
from astropy.visualization import make_lupton_rgb

import astropy as ap

"""
FITS (Flexible Image Transport System) dosyası, 
astronomi ve havacılık gibi uygulamalarda kullanılan bir görüntü ve veri dosyası formatıdır. 
FITS dosyaları, görüntülerin ve verilerin kaydedilmesi ve taşınması için kullanılan standart bir biçimdir. 
Bu dosyalar, çok sayıda veri tablosu ve metadatayı içerebilir ve genellikle 32 bit veya 64 bit olarak kaydedilir.
"""

NGC5866 = fits.open(r"/NGC5866/frame-u-006122-1-0013.fits.bz2")

NGC5866.info()

type(NGC5866)

NGC5866[0].header

NGC5866[1].header

header.header

NGC5866[3].header

for i in range(4):
    display(NGC5866[i].header)

dir(NGC5866)
help(NGC5866)
?NGC5866

ap.online_help("online_help")

NGC5866_data = NGC5866[0].data

type(NGC5866_data)
# numpy.ndarray

NGC5866_data.dtype.name
# float32

(1489, 2048).shape
# (1489, 2048)

NGC5866_data.min()
# -0.20483398
NGC5866_data.max()
# 312.5
NGC5866_data.mean()
# 0.008740974
NGC5866_data.std()
# 0.423594

plt.imshow(NGC5866_data, cmap="gray")
plt.colorbar()
plt.show()

plt.hist(NGC5866_data.flat)
plt.show()

plt.hist(NGC5866_data)
plt.show()

plt.imshow(NGC5866_data, cmap='gray', norm=LogNorm())
cbar = plt.colorbar(ticks=[4.e3,1.e4,2.e4])
cbar.ax.set_yticklabels(['5,000','10,000','20,000'])
plt.show()

NGC5866u = fits.open(r"/NGC5866/frame-u-006122-1-0013.fits.bz2")
NGC5866i = fits.open(r"/NGC5866/frame-i-006122-1-0013.fits.bz2")
NGC5866g = fits.open(r"/NGC5866/frame-g-006122-1-0013.fits.bz2")

g = NGC5866g[0].data
i = NGC5866i[0].data
u = NGC5866u[0].data

rgb_default = make_lupton_rgb(i, g, u,stretch=1.5,Q=10)

plt.imshow(rgb_default, origin='lower')
plt.show()

plt.savefig("NGC5866.jpg")

# pip freeze