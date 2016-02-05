#sorts list of files by number of lines
#be sure to input files
wc -l "$@" | sort -n
