#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 19 13:18:51 2024

@author: zc
"""

from astropy.io import fits
import numpy as np
from astropy.wcs import WCS
from astropy.coordinates import SkyCoord
from astroquery.simbad import Simbad

from SciServer import SkyServer

file='UGC_4591_g.fits'

#premena pixelov - len centralny, zakomentovana cast je pre cely obrazok
def transform_whole_image(file_path):
    
    with fits.open(file_path) as hdul:

        wcs = WCS(hdul[0].header)
        data_chanel=hdul[0].data
        
        #centralny pixel hladame trivialne - vydelenim poctu pixelov 2 na obidvoch osiach
        num_rows, num_columns = data_chanel.shape
        
        centr_x = 0.5 * num_columns
        centr_y = 0.5 * num_rows

        """

        shape = hdul[0].data.shape

        pixel_x, pixel_y = np.meshgrid(np.arange(1, shape[1] + 1), np.arange(1, shape[0] + 1))

        world_coords = wcs.pixel_to_world(pixel_x, pixel_y)

        ra_values = world_coords.ra.deg
        dec_values = world_coords.dec.deg
        """
        
        #central_pixel = np.array([[hdul[0].header['CRPIX1'], hdul[0].header['CRPIX2']]])
        central_pixel = np.array([[centr_x, centr_y]])

        world_coords = wcs.pixel_to_world(central_pixel[:, 0], central_pixel[:, 1])

        ra_values = world_coords.ra.deg[0]
        dec_values = world_coords.dec.deg[0]

        
        central_coords = SkyCoord(ra=ra_values, dec=dec_values, unit='deg', frame='icrs')

        #premena do suradnic hodny/minuty/sekundy co sa vacsinou pouziva v katalogoch
        #central_coords_formatted = central_coords.to_string('hmsdms', sep=' ', precision=2)

    return central_coords

central_coords = transform_whole_image(file)
#print("Central Coordinates (RA2000, DEC2000):", central_coords)

#Prvy sposob hladania galaxie - z databazy SIMBAD
def get_galaxy_name(ra_deg, dec_deg):

    coords = SkyCoord(ra=ra_deg, dec=dec_deg, unit='deg', frame='icrs', equinox='J2000.0')
    result_table = Simbad.query_region(coords, radius='0d0m3s')
    print(result_table['RA'])

    if result_table is not None and len(result_table) > 0:
        galaxy_name = result_table['MAIN_ID'][0]
        return galaxy_name
    else:
        return "Galaxy not found"

#ra=np.round(central_coords.ra.deg,3)
#dec=np.round(central_coords.dec.deg,3)

ra=central_coords.ra.deg
dec=central_coords.dec.deg

galaxy_name = get_galaxy_name(ra, dec)
print("Galaxy Name:", galaxy_name)

query_galaxy="SELECT TOP 10 clean, objID, petroMag_u, petroMag_g, petroMag_r, petroMag_i, petroMag_z, EXPAB_r, ra, " \
             "dec FROM Galaxy " \
             "WHERE ra > %s and ra < %s AND dec > %s AND dec < %s" % (ra-0.001, ra + 0.001, dec-0.001, dec + 0.001)

query_redshift="SELECT TOP 10 bestObjID, z, zErr " \
               "FROM SpecObj " \
               "WHERE ra > %s and ra < %s AND dec > %s AND dec < %s" % (ra-0.001, ra + 0.001, dec-0.001, dec + 0.001)

vysl_gal=SkyServer.sqlSearch(query_galaxy,dataRelease='DR18')
print(vysl_gal)

vysl_red=SkyServer.sqlSearch(query_redshift,dataRelease='DR18')
# niektore galaxie su v katalogu ale nemaju redshift, to nevadi,
# staci tam len doplnit Nan, pokial pre ne nebude redshift
print(vysl_red)

# podmienky - redshift brat len vtedy ked je ID rovnake pri obidvoch tabulkach!!!
# ak najde viacero objektov - najskor pozriet stlpec "clean" - ak je hodnota 1, su to kvalitnejsie data, brat ten objekt
# pokial by viacero objektov malo "clean" rovnaky, tak neostava asi nic ine ako zobrat prvy riadok
# v kazdom pripade treba objekty flagnut ak najde viac objektov pre tie suradice a zvlast flagnut
# ked sa nebude dat vybrat na zaklade stlpca "clean"

# vysledok - tabulka, kde bude galaxy name a vsetky stlpce z vysl_gal a vysl_red
