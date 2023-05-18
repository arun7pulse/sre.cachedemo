#!/bin/bash
# To Find Redis TTL and Memory Usage
# Author: ArunSK
REDISHOST=localhost
REDISPORT=6379
DBNO=0
KEYSLIST=`redis-cli -h $REDISHOST -p $REDISPORT -n $DBNO keys  "*"|awk '{print $1}'`
echo "KEY TTL MEMORY_USAGE"
echo "----------------------------- – –  – – --"
while read LINE
do
    TTL=`redis-cli -h $REDISHOST -p $REDISPORT -n $DBNO ttl "$LINE"`;
    MEMUSAGE=`redis-cli -h $REDISHOST -p $REDISPORT -n $DBNO memory usage "$LINE"`;
    echo "$LINE $TTL $MEMUSAGE" | awk '{ printf "%-50s %6s %s\n", $1, $2, $3 }';
done <<< "$KEYSLIST"