a=$1
b=$2
c=$3
# your code here
num1=$(( $a*$b+$c ))
num2=$(( $a+$b+$c ))
num3=$(( $a*$b*$c ))
num4=$(( $a*($b+$c) ))
num5=$(( $a+($b*$c) ))
num6=$(( ($a+$b)*$c ))
ar=( $num1 $num2 $num3 $num4 $num5 $num6)
IFS=$'\n'

echo "${ar[*]}" | sort -nr | head -1