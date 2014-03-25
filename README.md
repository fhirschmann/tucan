# tucanwatch

Notifies you via email when there are new grades available in
the campus management system of Technische Universität Darmstadt.

## Installation

```
[ ! -d ~/bin ] && mkdir ~/bin
curl -o ~/bin/tucanwatch.py https://raw.githubusercontent.com/fhirschmann/tucanwatch/master/tucanwatch.py
chmod 755 ~/bin/tucanwatch.py
```

## Setup

Set your username and password:

```
cat << EOF >> ~/.netrc
machine www.tucan.tu-darmstadt.de
    login ab34abab
    password secret
EOF
```

## Manual checking

Run

```bash
tucanwatch.py -a
```

to print all grades in the current semester or

```bash
tucanwatch.py
```

to print only new grades.

## Periodic checking

Edit your crontab

```bash
crontab -e
```
And add this in order to check every 60 minutes:

```bash
*/60 * * * * /home/user/bin/tucanwatch.py -m me@email.com 2>&1 >>/dev/null
```
