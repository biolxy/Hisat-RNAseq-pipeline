##################################################
# File Name: Hisat2_Mapping.sh
# Author: biolxy
# E-mail: biolxy@aliyun.com
# Created Time: Fri 13 Oct 2017 05:57:03 PM CST
##################################################
#!/bin/bash
starttime=$(date +%s)
# 双端测序
Hisat='/home/lixiangyong/soft/HISAT2-2.0.4'
samtools='/home/lixiangyong/soft/samtools/samtools'
Gtf='TAIR10.gtf'
Genome='TAIR10.genome'
mkdir index
python2.7 $Hisat/extract_exons.py $Gtf > species.exon &&
python2.7 $Hisat/extract_splice_sites.py $Gtf > species.ss &&
python2.7 $Hisat/hisat2-build -a -q -p 16 --ss species.ss --exon species.exon $Genome index/species &&
function pairend()
{
    $Hisat/hisat2 -p 16 --dta -x ./index/species -1 $1 -2 $2 -S ${3}.sam
    # $Hisat/hisat2 -p 4 --dta -x ./index/species -1 Samples/LjA_R1.fastq -2 Samples/LjA_R2.fastq -S LjA.sam &
}
function singlend()
{
    $Hisat/hisat2 -p 16 --dta -x ./index/species -q $1 -S ${2}.sam
    #$Hisat/hisat2 -p 16 --dta -x ./index/species -q $id -S ${id%.*}.sam
}
ls *.fastq | cut -b 1-7 | sort -u > list1  # 获得 samplename
for id in $(cat list1)
do
    fq1=${id}_R1.fastq
    fq2=${id}_R2.fastq
    pairend $fq1 $fq2 $id
done
rm list1
endtime=$(date +%s)
echo -e  "\e[31mThe script executes the $(expr $endtime - $starttime) s\e[0m" 
