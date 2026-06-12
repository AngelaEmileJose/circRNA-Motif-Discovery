# Motif Comparison Report

**Course:** Introduction to Bioinformatics (MBIO0402), 2026  
**Project:** circRNA Flanking Intron Motif Discovery  

---

## 1. Upstream Introns (I1) Comparison Summary (`up_I1` vs `down_I1`)

* **Query Motif Set:** `up_I1_meme.txt` (10 motifs)
* **Target Motif Set:** `down_I1_meme.txt` (10 motifs)
* **Threshold:** E-value < 0.01

### Overlapping (Common) Motifs
Six out of the ten discovered motifs in `up_I1` matched corresponding motifs in `down_I1` below the significance threshold:

| Upstream (UP) Motif ID | Downstream (DOWN) Motif ID | E-value | Best Alignment Consensus | Splicing Factor / Candidate |
| :---: | :---: | :---: | :---: | :---: |
| MEME-3 (`ARMCCTGKCT`) | MEME-6 (`AGMCAGGGYT`) | 9.51e-07 | `ARMCCTGKCT` vs `AGMCAGGGYT` | GC-rich element (hnRNP / SR protein) |
| MEME-1 (`ACACACACAC`) | MEME-2 (`TGKGTGTGTG`) | 7.38e-05 | `ACACACACAC` vs `TGKGTGTGTG` | CA/GT-repeats (CELF / MBNL family) |
| MEME-2 (`YTYTYTYTCY`) | MEME-5 (`TCTYTCTYYC`) | 2.16e-04 | `YTYTYTYTCY` vs `TCTYTCTYYC` | Pyrimidine-rich tract (PTBP1 / hnRNP I) |
| MEME-5 (`TTTDTTTDTT`) | MEME-1 (`TTTCTTTTTT`) | 2.26e-04 | `TTTDTTTDTT` vs `TTTCTTTTTT` | Poly-T tract (TDP-43 / hnRNP family) |
| MEME-7 (`CAGARGVCAG`) | MEME-7 (`CTGRBCWCTS`) | 3.82e-03 | `CAGARGVCAG` vs `CTGRBCWCTS` | Purine-rich element (SRSF binding) |
| MEME-10 (`TGSYCTKCCW`) | MEME-9 (`CTKCTCTTCY`) | 6.13e-03 | `TGSYCTKCCW` vs `CTKCTCTTCY` | Pyrimidine-rich motif (splicing regulator) |

### Group-Specific Motifs
Four motifs in `up_I1` did not match any motif in `down_I1` under the E-value threshold:
* **UP-regulated specific motifs:**
  * MEME-4 (`YCCCAGCACY`)
  * MEME-6 (`TKGAACTCAS`)
  * MEME-8 (`CCAGRAGAGG`)
  * MEME-9 (`GCCACCATGT`)

### Visual Alignment (I1)
*Refer to the uploaded alignment report:* [I1_motif_comparison.png.pdf](file:///c:/Users/angel/Downloads/Bioinfo2026_ProjectData/I1_motif_comparison.png.pdf)

---

## 2. Downstream Introns (I2) Comparison Summary (`up_I2` vs `down_I2`)

* **Query Motif Set:** `up_I2_meme.txt` (10 motifs)
* **Target Motif Set:** `down_I2_meme.txt` (10 motifs)
* **Threshold:** E-value < 0.01

### Overlapping (Common) Motifs
Only two motifs (forming three matching pairs) in `up_I2` matched corresponding motifs in `down_I2` below the significance threshold:

| Upstream (UP) Motif ID | Downstream (DOWN) Motif ID | E-value | Best Alignment Consensus | Splicing Factor / Candidate |
| :---: | :---: | :---: | :---: | :---: |
| MEME-2 (`CAMAMAMAMA`) | MEME-1 (`TGTGTGTGTG`) | 2.70e-04 | `CAAACAAAAA` vs `TGTGTGTGTG` | CA/GT-repeats (CELF / MBNL family) |
| MEME-2 (`CAMAMAMAMA`) | MEME-4 (`TTTTGTTTTT`) | 1.34e-03 | `CAAACAAAAA` vs `TTTTGTTTTT` | CA/T-rich elements (hnRNP family) |
| MEME-5 (`RAGTTCCAGG`) | MEME-9 (`TBCTGGRAYT`) | 1.39e-03 | `GAGTTCCAGG` vs `TBCTGGRAYT` | Purine/Pyrimidine element (SRSF binding) |

### Group-Specific Motifs
Eight motifs in `up_I2` did not match any motif in `down_I2` under the E-value threshold:
* **UP-regulated specific motifs:**
  * MEME-1 (`RGAGGMAGRG`)
  * MEME-3 (`AGCCWGGGCT`)
  * MEME-4 (`CCCAGCACHB`)
  * MEME-6 (`CAGCCTCCAG`)
  * MEME-7 (`SAGARGRMAG`)
  * MEME-8 (`GCABGCCTTT`)
  * MEME-9 (`GMAGGCAGAT`)
  * MEME-10 (`GCTTTGCCTT`)

### Visual Alignment (I2)
*Refer to the uploaded alignment report:* [I2_motif_comparison.png.pdf](file:///c:/Users/angel/Downloads/Bioinfo2026_ProjectData/I2_motif_comparison.png.pdf)

---

## 3. Biological Conclusion
1. **Core Splicing Machinery Recognition:** The overlapping motifs in both I1 and I2 regions are dominated by simple sequence repeats (SSRs), specifically **CA-rich/GT-rich repeats** (complementary to each other), **pyrimidine-rich tracts (CT repeats)**, and **poly-T tracts**. These repeats serve as highly conserved binding platforms for core splicing regulators (such as CELF, PTBP1, and TDP-43 families). Their conservation across both UP and DOWN groups suggests they represent general structural elements required to bring flanking introns close together for back-splicing.
2. **Dynamic Regulation via Group-Specific Motifs:** The presence of numerous group-specific motifs (especially the 8 UP-regulated specific motifs in downstream introns) suggest that differential circRNA expression during cardiac pressure overload (TAC) is dynamically tuned by specific splicing enhancers or silencers (like SRSF proteins binding to purine-rich elements), rather than just the default back-splicing machinery.
