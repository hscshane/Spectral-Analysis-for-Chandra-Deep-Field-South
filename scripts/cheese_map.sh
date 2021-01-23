#!/bin/sh

. /usr/local/xmmsas_20160201_1833/setsas.sh 
echo $SAS_DIR
echo $SAS_PATH

#for i in 0108060401 0108060501 0108060601 0108060701 0108061801 0108061901 0108062101 0108062301 0555780101 0555780201 0555780301 0555780401 0555780501 0555780601 0555780701 0555780801 0555780901 0555781001 0555782301 0604960101 0604960201 0604960301 0604960401 0604960501 0604960601 0604960701 0604960801 0604960901 0604961001 0604961101 0604961201 0604961301 0604961801
for i in 0108060401
do
SAS_ODF=/raid2/dxb/xmm/downloads/CDFS/$i/ODF/summary.sas;export SAS_ODF
echo $SAS_ODF
SAS_CCFPATH=/raid2/dxb/xmm/analysis/hsc/ccf; export SAS_CCFPATH
echo $SAS_CCFPATH
cd /raid2/dxb/xmm/analysis/CDFS/hsc/cheese
mkdir $i
cd /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i
mkdir analysis 
mkdir logs
cd /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
SAS_CCF=/raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/ccf.cif; export SAS_CCF
echo $SAS_CCF
echo "$i" > obs_id
echo "working on" $i

cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-clean.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-clean-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-gti.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-gti-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-gti-oot.txt /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-gti.txt /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-hist-oot.qdp /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-hist.qdp /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
#cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-ratec.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
#cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-ratec-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-rate.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-rate-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-obj-image-det.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
#cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-obj-image-det-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-obj-image-det-unfilt-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-obj-image-sky.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-obj-image-sky-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-oot.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis
cp /raid2/dxb/xmm/analysis/CDFS/hsc/ellipse/$i/analysis/pnS005-ori.fits /raid2/dxb/xmm/analysis/CDFS/hsc/cheese/$i/analysis


echo "Start cheese"
echo "cheese prefixp=S005 scale=0.2 rate=0.1 dist=5.0 clobber=1 elow=400 ehigh=7200 >& ../logs/"$i"-cheese.log"
cheese prefixp=S005 scale=1 rate=0.1 dist=5.0 clobber=1 elow=100 ehigh=100 >& ../logs/$i-cheese.log
echo "end cheese .."
echo "done" $i

done























