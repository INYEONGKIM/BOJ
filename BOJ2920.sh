read s;
case $s in
	"1 2 3 4 5 6 7 8") echo "ascending";;
	"8 7 6 5 4 3 2 1") echo "descending";;
	*) echo "mixed";;
esac
