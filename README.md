# Spectral-Analysis-for-Chandra-Deep-Field-South 

Nearly all scripts are stored under /raid2/dxb/xmm/analysis/CDFS/hsc/mapfiles
===========================================================================================================================================================================
1. Create spectra for dxb:
run run_xmm_el.sh:
    make_bkg_region_sky_el.py creates pnS005-bkg_region-sky.fits for chandra sources and extended sources
    make_bkg_region_withradec_el.py converts X,Y coordinates to RA DEC and arcmin, files porduced will be used to create pnS005-bkg_region-det.fits for chandra sources and extended sources
    append_bkg_region.py combines files for xmm sources with chandra sources and extended sources
    poly_input contains the RA DEC coords of Chandra FOV for CDFS, which is a polygon
    poly_output contains the DETX DETY coords of Chandra FOV for CDFS, which is a polygon
    chandra_reg.py creates chandra.reg, which can be used in spectra extraction

Spectra files are pnS005-obj-full.pi, pnS005-full.rmf, pnS005-full.arf, pnS005-back-full.pi, which are group in /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/xspec as pnS005-obj-full-grp.pi by using grppha

copy and run the content of backscale.sh to modify the BACKSCAL keyword and normalize the spectra(make normalized count rates go to 0 for between 10 kev and 14 kev)

===========================================================================================================================================================================

#Create spectra for galaxies:
region_sky.py gives pnS005-bkg_region-sky-type.fits
galaxy_el.py gives GALAXY_CAT1, which contains X, Y, Radius, Flux, Type of galaxies inside the chandra FOV, excluding those inside the XMM sources and extended sources.
run GalaxySpectra:
    each galaxy spectrum will be copied to /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/Galaxy/$i under each folder for different pointings.
    spectra files include #galaxy.pi, #galaxy.rmf, #galaxy.arf. #galaxy.txt records the ra, dec, flux for each galaxy selected.
Copy and modify Weight.py on line 18,76,98,99,101,102,103,105,106 in each folder then run:
    exp.lis contains exposure times for 14 first combine spectra, 2 second combined spectra and 1 final combined spectra
    #-galaxypi.lis contains expression for first mathpha
    #-galaxyrmf.lis contains weighing factor for 14 rmf groups
    #-galaxyarf.lis contains weighing factor for 14 arf groups
    2-1-galaxypi.lis contains expression for second mathpha
    2-2-galaxypi.lis contains expression for second mathpha
    2-1-galaxyrmf.lis contains weighing factor for second rmf groups
    2-2-galaxyrmf.lis contains weighing factor for second rmf groups
    2-1-galaxyarf.lis contains weighing factor for second arf groups
    2-2-galaxyarf.lis contains weighing factor for second arf groups
    3-1-galaxypi.lis contains expression for final mathpha
    3-1-galaxyrmf.lis contains weighing factor for final rmf groups
    3-1-galaxyarf.lis contains weighing factor for final arf groups
run mathpha:

mathpha expr='0galaxy.pi + 1galaxy.pi + 2galaxy.pi + 3galaxy.pi + 4galaxy.pi + 5galaxy.pi + 6galaxy.pi + 7galaxy.pi + 8galaxy.pi + 9galaxy.pi  ' units='c' outfil='first1.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='10galaxy.pi + 11galaxy.pi + 12galaxy.pi + 13galaxy.pi + 14galaxy.pi + 15galaxy.pi + 16galaxy.pi + 17galaxy.pi + 18galaxy.pi + 19galaxy.pi  ' units='c' outfil='first2.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='20galaxy.pi + 21galaxy.pi + 22galaxy.pi + 23galaxy.pi + 24galaxy.pi + 25galaxy.pi + 26galaxy.pi + 27galaxy.pi + 28galaxy.pi + 29galaxy.pi  ' units='c' outfil='first3.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='30galaxy.pi + 31galaxy.pi + 32galaxy.pi + 33galaxy.pi + 34galaxy.pi + 35galaxy.pi + 36galaxy.pi + 37galaxy.pi + 38galaxy.pi + 39galaxy.pi ' units='c' outfil='first4.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='40galaxy.pi + 41galaxy.pi + 42galaxy.pi + 43galaxy.pi + 44galaxy.pi + 45galaxy.pi + 46galaxy.pi + 47galaxy.pi + 48galaxy.pi + 49galaxy.pi  ' units='c' outfil='first5.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='50galaxy.pi + 51galaxy.pi + 52galaxy.pi + 53galaxy.pi + 54galaxy.pi + 55galaxy.pi + 56galaxy.pi + 57galaxy.pi + 58galaxy.pi + 59galaxy.pi  ' units='c' outfil='first6.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='60galaxy.pi + 61galaxy.pi + 62galaxy.pi + 63galaxy.pi + 64galaxy.pi + 65galaxy.pi + 66galaxy.pi + 67galaxy.pi + 68galaxy.pi + 69galaxy.pi  ' units='c' outfil='first7.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='70galaxy.pi + 71galaxy.pi + 72galaxy.pi + 73galaxy.pi + 74galaxy.pi + 75galaxy.pi + 76galaxy.pi + 77galaxy.pi + 78galaxy.pi + 79galaxy.pi  ' units='c' outfil='first8.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='80galaxy.pi + 81galaxy.pi + 82galaxy.pi + 83galaxy.pi + 84galaxy.pi + 85galaxy.pi + 86galaxy.pi + 87galaxy.pi + 88galaxy.pi + 89galaxy.pi  ' units='c' outfil='first9.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='90galaxy.pi + 91galaxy.pi + 92galaxy.pi + 93galaxy.pi + 94galaxy.pi + 95galaxy.pi + 96galaxy.pi + 97galaxy.pi + 98galaxy.pi + 99galaxy.pi  ' units='c' outfil='first10.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='100galaxy.pi + 101galaxy.pi + 102galaxy.pi + 103galaxy.pi + 104galaxy.pi + 105galaxy.pi + 106galaxy.pi + 107galaxy.pi + 108galaxy.pi + 109galaxy.pi  ' units='c' outfil='first11.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='110galaxy.pi + 111galaxy.pi + 112galaxy.pi + 113galaxy.pi + 114galaxy.pi + 115galaxy.pi + 116galaxy.pi + 117galaxy.pi + 118galaxy.pi + 119galaxy.pi  ' units='c' outfil='first12.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='120galaxy.pi + 121galaxy.pi + 122galaxy.pi + 123galaxy.pi + 124galaxy.pi + 125galaxy.pi + 126galaxy.pi + 127galaxy.pi + 128galaxy.pi + 129galaxy.pi ' units='c' outfil='first13.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='130galaxy.pi + 131galaxy.pi + 132galaxy.pi + 133galaxy.pi + 134galaxy.pi + 135galaxy.pi + 136galaxy.pi + 137galaxy.pi + 138galaxy.pi + 139galaxy.pi ' units='c' outfil='first14.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='first1.pi + first2.pi + first3.pi + first4.pi + first5.pi + first6.pi + first7.pi  ' units='c' outfil='second1.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='first8.pi + first9.pi + first10.pi + first11.pi + first12.pi + first13.pi + first14.pi  ' units='c' outfil='second2.pi' exposure='calc' areascal='%' ncomments=0
mathpha expr='second1.pi + second2.pi  ' units='c' outfil='final.pi' exposure='calc' areascal='%' ncomments=0

run addarf:
addarf @1-galaxyarf.lis out_ARF='first1.arf'
addarf @2-galaxyarf.lis out_ARF='first2.arf'
addarf @3-galaxyarf.lis out_ARF='first3.arf'
addarf @4-galaxyarf.lis out_ARF='first4.arf'
addarf @5-galaxyarf.lis out_ARF='first5.arf'
addarf @6-galaxyarf.lis out_ARF='first6.arf'
addarf @7-galaxyarf.lis out_ARF='first7.arf'
addarf @8-galaxyarf.lis out_ARF='first8.arf'
addarf @9-galaxyarf.lis out_ARF='first9.arf'
addarf @10-galaxyarf.lis out_ARF='first10.arf'
addarf @11-galaxyarf.lis out_ARF='first11.arf'
addarf @12-galaxyarf.lis out_ARF='first12.arf'
addarf @13-galaxyarf.lis out_ARF='first13.arf'
addarf @14-galaxyarf.lis out_ARF='first14.arf'
addarf @2-1-galaxyarf.lis out_ARF='second1.arf'
addarf @2-2-galaxyarf.lis out_ARF='second2.arf'
addarf @3-1-galaxyarf.lis out_ARF='final.arf'

run addrmf:
addrmf @1-galaxyrmf.lis rmffile='first1.rmf'
addrmf @2-galaxyrmf.lis rmffile='first2.rmf'
addrmf @3-galaxyrmf.lis rmffile='first3.rmf'
addrmf @4-galaxyrmf.lis rmffile='first4.rmf'
addrmf @5-galaxyrmf.lis rmffile='first5.rmf'
addrmf @6-galaxyrmf.lis rmffile='first6.rmf'
addrmf @7-galaxyrmf.lis rmffile='first7.rmf'
addrmf @8-galaxyrmf.lis rmffile='first8.rmf'
addrmf @9-galaxyrmf.lis rmffile='first9.rmf'
addrmf @10-galaxyrmf.lis rmffile='first10.rmf'
addrmf @11-galaxyrmf.lis rmffile='first11.rmf'
addrmf @12-galaxyrmf.lis rmffile='first12.rmf'
addrmf @13-galaxyrmf.lis rmffile='first13.rmf'
addrmf @14-galaxyrmf.lis rmffile='first14.rmf'
addrmf @2-1-galaxyrmf.lis rmffile='second1.rmf'
addrmf @2-2-galaxyrmf.lis rmffile='second2.rmf'
addrmf @3-1-galaxyrmf.lis rmffile='final.rmf'

rename and group:
grppha infile="$i-galaxy.pi" outfile="$i-galaxy-grp.pi" comm="group min 25&chkey RESPFILE $i-galaxy.rmf&chkey ANCRFILE $i-galaxy.arf&chkey BACKFILE $i-pnS005-back.pi&exit"

Spectra files are galaxy.pi, galaxy.rmf, galaxy.arf, pnS005-back.pi, which are group in /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/xspec as galaxy-grp.pi by using grppha

copy and run the content of backscale_el.sh to modify the BACKSCAL keyword and normalize the spectra(make normalized count rates go to 0 for between 10 kev and 14 kev)

===========================================================================================================================================================================



    
    


    
    
    
    
    
