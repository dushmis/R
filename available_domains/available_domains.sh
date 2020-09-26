x=$(cat /usr/share/dict/words  | \
awk '{if(length($0)<10 && length($0)>4){print "tech"$0}}' | \
tr '[:upper:]' '[:lower:]' | \
sort | \
awk '{if(length($0)<10 && length($0)>4){print $0".com"}}')

for k in $x;
do
  h=$(host $k 2>&1);
  for l in "$h";
  do
    grep -q "dushyant" <<< "$l" 2>&1
    if [[ $? -eq 0 ]]; then
      echo "not found $k"
    # else
    #   echo "vvv found $k"
    fi
  done;
  sleep 1;
done;
