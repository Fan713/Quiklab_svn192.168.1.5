file=/home/cl/usage.txt
result=/home/cl/result.txt

if [ -f $result ]
then
	rm $result
fi
echo "Start time: `date`"| tee -a $result
while [ 1 ]
do
	top -n 1 >$file
	idle=`cat $file | grep Cpu | awk '{print $5}' | sed 's/id,/ /g'`
	Target_usage=`cat $file | grep TargetApp | awk '{ print $10 }'`
	Target_mem=`cat $file | grep TargetApp | awk '{ print $11 }'`
        echo "Cpu idle is: $idle "| tee -a $result
        echo "Target_usge is: $Target_usage"| tee -a $result
	echo "Target_mem is: $Target_mem"| tee -a $result
	echo "------------------------------------"| tee -a $result
	sleep 1
done
