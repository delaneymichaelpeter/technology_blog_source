Title: Useful Linux Commands
Date: 2020-01-12 10:20
Modified: 2011-06-10 19:30
Tags: linux, bash
Slug: useful-linux-commands
Authors: Peter Delaney 
Summary: Commands that are helpful to execute


## Github site containing a lot of Great Unix one-liners
[Github Unix One-Liners](https://github.com/jlevy/the-art-of-command-line)  Excellent Guide on Github showing linux commands

## FIND Command 
**Remove Certain Files in a Search/Find**
```bash
find . -name '*.log' -exec rm -fr {} \;
```
**Search for a class file inside a jar file**
```bash
find . -name '*.jar' -exec bash -c "echo {} && jar tvf {} | grep Name_Searching_For " \;
```

**Find large files over 1 Gig and modified more than 10 days ago**
```bash
find . -size +1G -mtime +10 -type f -print
```


**See if a certain process is listening on a port**
```bash
netstat -tulpn | grep <port>
```

**Find files who size is greater than
```bash
find . -type f -size +1G
```


## Checking open files 

**Shows Files Open Related to Java or ACES **
```bash
echo /proc/`ps -ef | grep java | grep -v grep | awk '{ print $2 }'`/fd | xargs ls -1 | wc -l
```

**Shows Files Open Related to Java or ACES **
```bash
ls /proc/fd | wc -l
```

**Shows All of the Processes and the Tree **
```bash
pstree -A | more
```


## Monitoring processes 
```bash
top -u aces;        // once it comes up….press "1" to see all the cores
top -H -u aces;     // once it comes up….press "1" to see all the cores  [will show you the thread usage as opposed to the CPU usage]
mpstat -P ALL;      // shows overall CPU usage
```

Monitoring Performance 
```bash
/usr/bin/sar 1 20;         //  Run sar command 20 times…with 1 second between it
```


## Monitoring Disk I/O 

**Monitor Input/Output Devices **
```bash
iostat -d -x -N
```
** Columns **
: name of device more /etc/fstab show you the mount point to ACES directory
: number of seconds between each capture of IO
: number of times to run default forever

** Mount Point
```bash
# View Mount Point
more /etc/fstab (file that tells you the names of mount points)

# Add mounts
mount -a

# Remove mount point
umount <directory-where-mount-exists>
```

## Network IO
```bash
iostat output 
```
await: avg. time servicing request (svctm) + avg. time waiting in request queue.
svctm: avg. time servicing request
await should be close to svctm, means all time spent processing io. If wait greater svctm means io requests are waiting in queue a long time and there is a PROBLEM!


## Monitor IO for Each CPU 
```bash
npstat   -P all
```

## Sorting files
```bash
sort a b | uniq > c       # c is a union b
sort a b | uniq -d > c    # c is a intersect b
sort a b b | uniq -u > c  # c is set difference a - b

```


## Java Garbage Collector Monitoring 
```bash
jstat -gc
```

**Options**

1. -gc
2. -gcutil
3. -gcnew
4. -gccapacity

**If want to monitor GC stats on actual server put following in JBoss startup**

* -verbose:gc (print the GC logs) 
* -Xloggc: (for more comprehensive GC logging) 
* -XX:+PrintGCDetails (for more detailed output) 
* -XX:+PrintTenuringDistribution (displays the tenuring thresholds assumed by the JVM)


## Java Stack Dump of Running Process 
```bash
jstack  >; 
```






