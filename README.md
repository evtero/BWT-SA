# BWT & SA
Different ways to compute Burrows–Wheeler transform (BWT) and Suffix Array (SA).

## Files

- *utils_bwt.py*: all functions needed.
- *bwt_from_bwm.py, bwt_from_sa_bf.py* and *bwt_from_sa_pd.py*: these scripts import all functions, read a given number of characters from a text file and return in an output file the BWT calculated with the corresponding method. The input file and the number of characters are passed by the command line like this example: `python3 bwt_from_bwm.py dna.50MB 10000` 
  
## Alternatives to compute
  
Two ways to obtain BWT:

- **BWT from BWM (Burrows-Wheeler Matrix)**: `get_rotations()`, `get_bwm()`, `bwm2btw()`.

- **BWT from SA**: `sa2bwt()`.

Two ways to obtain SA:

- **Brute force**: `get_sa_bf()`.

- **Memory-efficient SA construction with Prefix Doubling Algorithm**: `get_first_buckets()`, `get_buckets()`, `get_sa()`, `sa_prefix_doubling()`.
