read num
cnt=0

for ((i=1; i<=$num; i++)); do
	if [ $i -lt 100 ]
	then
		((cnt++))
	else
		a=${i:0:1}
		b=${i:1:1}
		c=${i:2:1}

		if [ $(($a - $b)) -eq $(($b - $c)) ]
		then
			((cnt++))
		fi

	fi
done

echo $cnt
