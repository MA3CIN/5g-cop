./app ue-latency-interval -n 10 > results.txt
cat results.txt | grep LATENCY
cat results.txt  | grep LATENCY | cut --complement -c1-87 | cut --complement -c6-9