"""
EXPERIMENT 10 (CONTENT BEYOND SYLLABUS)
Title: VISUALIZING GEOGRAPHIC DATA WITH BASEMAP
Aim: To visualizing geographic data with basemap
Overview:
  Demonstrates global and regional cartographic projections using mpl_toolkits.basemap:
  1. Simple Mercator coastline map
  2. Colored continents & graticules on Mercator projection
  3. Mollweide elliptical projection
  4. North American political boundaries and rivers (Albers Equal Area)
  5. Topographic relief map of North America with Seattle pin (Lambert Conformal)
  6. Map Projections Comparison (Cylindrical, Orthographic 3D globe, Conic)
"""

import warnings
from itertools import chain
import numpy as np
import matplotlib.pyplot as plt

try:
    from mpl_toolkits.basemap import Basemap
    import matplotlib.cbook
    warnings.filterwarnings("ignore", category=matplotlib.cbook.mplDeprecation)
    BASEMAP_AVAILABLE = True
except ImportError:
    BASEMAP_AVAILABLE = False
    print("Notice: 'mpl_toolkits.basemap' is not installed in the current environment.")
    print("To install Basemap, run: pip install basemap basemap-data")
    print("Or with conda: conda install -c conda-forge basemap")


if BASEMAP_AVAILABLE:
    # -------------------------------------------------------------------------
    # 1. Simple Mercator Map Outline
    # -------------------------------------------------------------------------
    print("Rendering 1: Simple Mercator Projection...")
    fig = plt.figure(figsize=(12, 8))
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    plt.title("Mercator Projection - Coastlines Only")
    plt.show()

    # -------------------------------------------------------------------------
    # 1a. Colored Continents on Mercator Projection
    # -------------------------------------------------------------------------
    print("Rendering 1a: Colored Continents on Mercator...")
    fig = plt.figure(figsize=(12, 8))
    m = Basemap(projection='merc', llcrnrlat=-80, urcrnrlat=80,
                llcrnrlon=-180, urcrnrlon=180, resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='tan', lake_color='lightblue')
    m.drawparallels(np.arange(-90., 91., 30.), labels=[True, True, False, False], dashes=[2, 2])
    m.drawmeridians(np.arange(-180., 181., 60.), labels=[False, False, False, True], dashes=[2, 2])
    m.drawmapboundary(fill_color='lightblue')
    plt.title("Mercator Projection - Colored Continents and Oceans")
    plt.show()

    # -------------------------------------------------------------------------
    # 1b. Mollweide Projection with Custom Styling
    # -------------------------------------------------------------------------
    print("Rendering 1b: Mollweide Projection...")
    fig = plt.figure(figsize=(12, 8))
    m = Basemap(projection='moll', lon_0=0, resolution='c')
    m.drawcoastlines()
    m.fillcontinents(color='purple', lake_color='lightblue')
    m.drawparallels(np.arange(-90., 91., 30.), labels=[True, True, False, False], dashes=[2, 2])
    m.drawmeridians(np.arange(-180., 181., 60.), labels=[False, False, False, False], dashes=[2, 2])
    m.drawmapboundary(fill_color='lightblue')
    plt.title("Mollweide Projection");
    plt.show()

    # -------------------------------------------------------------------------
    # 2a. North American Map (Albers Equal Area with Boundaries & Rivers)
    # -------------------------------------------------------------------------
    print("Rendering 2a: North America with Boundaries & Rivers (Albers Equal Area)...")
    fig = plt.figure(figsize=(12, 8))
    m = Basemap(width=6000000, height=4500000, resolution='c', projection='aea',
                lat_1=35., lat_2=45, lon_0=-100, lat_0=40)
    m.drawcoastlines(linewidth=0.5)
    m.fillcontinents(color='tan', lake_color='lightblue')
    m.drawparallels(np.arange(-90., 91., 15.), labels=[True, True, False, False], dashes=[2, 2])
    m.drawmeridians(np.arange(-180., 181., 15.), labels=[False, False, False, True], dashes=[2, 2])
    m.drawmapboundary(fill_color='lightblue')
    m.drawcountries(linewidth=2, linestyle='solid', color='k')
    m.drawstates(linewidth=0.5, linestyle='solid', color='k')
    m.drawrivers(linewidth=0.5, linestyle='solid', color='blue')
    plt.title("North America - Albers Equal Area")
    plt.show()

    # -------------------------------------------------------------------------
    # 2b. Zoom-in to North America with Seattle Pin (Lambert Conformal + Etopo)
    # -------------------------------------------------------------------------
    print("Rendering 2b: Topographic Map with Seattle Pin...")
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution=None,
                width=8E6, height=8E6,
                lat_0=45, lon_0=-100)
    m.etopo(scale=0.5, alpha=0.5)
    x, y = m(-122.3, 47.6)
    plt.plot(x, y, 'ok', markersize=6)
    plt.text(x, y, ' Seattle', fontsize=12, fontweight='bold', color='white')
    plt.title("Lambert Conformal Projection - Etopo Relief & Seattle Pin")
    plt.show()

    # -------------------------------------------------------------------------
    # Projections Suite Helper Function
    # -------------------------------------------------------------------------
    def draw_map(m, scale=0.2):
        m.shadedrelief(scale=scale)
        lats = m.drawparallels(np.linspace(-90, 90, 13))
        lons = m.drawmeridians(np.linspace(-180, 180, 13))
        lat_lines = chain(*(tup[1][0] for tup in lats.items()))
        lon_lines = chain(*(tup[1][0] for tup in lons.items()))
        all_lines = chain(lat_lines, lon_lines)
        for line in all_lines:
            line.set(linestyle='-', alpha=0.3, color='w')

    # 2c. Cylindrical Projection
    print("Rendering 2c: Cylindrical Projection...")
    fig = plt.figure(figsize=(8, 6), edgecolor='w')
    m = Basemap(projection='cyl', resolution=None,
                llcrnrlat=-90, urcrnrlat=90,
                llcrnrlon=-180, urcrnrlon=180)
    draw_map(m)
    plt.title("Cylindrical Projection (Equidistant)")
    plt.show()

    # 2d. Orthographic (3D Globe) Projection
    print("Rendering 2d: Orthographic Projection...")
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='ortho', resolution=None,
                lat_0=50, lon_0=0)
    draw_map(m)
    plt.title("Orthographic (3D Globe) Projection")
    plt.show()

    # 2e. Conic Projection (Lambert Conformal)
    print("Rendering 2e: Conic Projection...")
    fig = plt.figure(figsize=(8, 8))
    m = Basemap(projection='lcc', resolution=None,
                lon_0=0, lat_0=50, lat_1=45, lat_2=55,
                width=1.6E7, height=1.2E7)
    draw_map(m)
    plt.title("Lambert Conformal Conic Projection")
    plt.show()

else:
    print("\\n[Basemap Code Ready] Please install Basemap to view the cartographic renderings.")

print("\\nResult: Thus, visualizing geographic data with basemap was implemented and executed successfully.")
