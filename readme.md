# Grid of Tries  
This implements a packet classification algorithm for IPv4 using Grid-of-Tries for 2D matching.  
### To execute:
- `./grt -p rulefile -i inputaddrfile -o outputfile`  
### Notes:
- Number of bits in the prefix W=16
- Minimum number of bits in the prefix is 8.
- Maximum number of entries in the `rulefile` is 100000
- Maximum number of entries in `inputaddrfile` is 10000
- `rulefile`: In each line, the first entry is the rule number. This is followed by two prefix entries, each of which has two fields - IP address prefix (in IP dotted decimal format, 2 decimal numbers separated by a dot) and prefix length (in bits). One has to convert the IP prefix into binary and truncate it to the prefix length.  
Eg: 1 128.16 12 130.205 16  
- `inputaddrfile`: Two entries per line. Each entry has a prefix value in IP dotted decimal format with two decimal numbers.  
Eg: 128.18 130.205  
- `outputfile`: Address1 Address2 NumOfMatches RulesMatched SearchTime(microseconds)
Eg: 128.18 130.205 1 1 45  
Average search time is reported at the end of the file.  
- References: Algorithms for Packet Classification <http://yuba.stanford.edu/~nickm/papers/classification_tutorial_01.pdf> Fast and Scalable layer four switching <http://www.utdallas.edu/~kxs028100/Papers/fast-and-scalable-layer-four-switching.pdf>
