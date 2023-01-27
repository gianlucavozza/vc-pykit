## vc-pykit
vc-pykit is a python module specific for ion torrent genrated VCF files that allows users to split multi-allelic variants, to scan and retain non-zero AF 
and to detect multiple variants at the same position and to create multiple VCFs for each variant to comply with funcotator.

## Installation and setup
Once downloaded the repository, user has to import the module
```
from ion_vc-pykit import *
```
## Manual
**split_vcf()** splits multi-allelic site variants 
**scan_af()** detects and retains non-zero AF 
**funco_vcf()** creates multiple VCF files for each multi-allelic sites

## Info and comments
If you need help or you have comments and tips for improving vc-pykit, please send a mail to drgianluca.vozza@gmail.com or emab992@gmail.com
