# what

if found pattern in log file, while tailing, sends email, duplication checking provided by legandary md5
how to notify if certain pattern is found in log file


```
  Usage :  _grepmail.sh [options] <FILE> <PATTERN> <EMAIL>

  Options:
  -v|version    Display script version
```


```
#How i'd use it ;)
_grepmail.sh  /tmp/home_security_system.log unknown_face_detected yourmail@domain.com 2>&1 >> /dev/null &
```