Title: Useful AWK Linux Commands
Date: 2020-03-27 10:20
Modified: 2020-03-27 19:30
Tags: linux, bash, awk
Slug: useful-awk-linux-commands
Authors: Peter Delaney 
Summary: awk commands that I've found very useful


## Print fields from a certain field on to end
**Grab fields from a line from 7th postion to the end
```bash
cat <some-file> | awk '{out=$2; for(i=7;i<=NF;i++){out=out" "$i}; print out}'

# Parse AOP for 200 Responses
cat /logs/sdc.log | grep "MFSi Response" | grep "httpStatusCode:200" | awk '{out=$2; for(i=7;i<NF;i++){out=out" "$i}; print "Error\n " out "\n " }'

# Parses for AOPErrorService
cat /logs/sdc.log | grep "AOPErrorService " | awk '{out=$2; for(i=7;i<NF;i++){out=out" "$i}; print "Error\n " out "\n " }'

```

## Command to find the Largest Number
```bash
# List of files find file that is the largest in size
ls -l | awk '$5>m {m=$5;file=$NF} END{print "Max number: "m " File="file}'

```






