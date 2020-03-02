echo -e "过去一周代码统计:\n"
startDate=$(date -d last-week +%Y-%m-%d-%a)
endDate=$(date +%Y-%m-%d-%a)
echo -e "From $startDate \nTo   $endDate\n"
data=$(git log --since="$startDate" --until="$endDate" --numstat --pretty=tformat: --no-merges | awk '{ add += $1; subs += $2; loc += $1 - $2 } END { printf "Added lines: %s \nRemoved lines: %s \nTotal lines: %s\n", add, subs, loc }')
echo "$data"
read