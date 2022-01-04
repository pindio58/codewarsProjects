# echo "$1"
if  [[ $1 =~ [a-zA-Z]+$ ]] ; then 
  echo "False";
  exit
fi
read -a ARRAY <<< $(echo "$1" | sed 's/ /k/g' | sed 's/./& /g')
#echo "${ARRAY[*]}"
if [ ${ARRAY[0]} = '(' ] &&  [ ${ARRAY[4]} = ')' ] &&  [ ${ARRAY[5]} = 'k' ] &&  [ ${ARRAY[9]} = '-' ]; then
  echo 'True'
else
  echo 'False'
fi