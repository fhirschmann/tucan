tucan
-----

Notifies you via email when there are new grades available in
the campus management system of Technische Universität Darmstadt.

Installation
````````````

It might be better to use your system's package manager to install
the required dependencies:

.. code:: bash

    apt-get install python-mechanize python-lxml python-pip

Then install tucan CLI via pip:

.. code:: bash

    pip install git+git://github.com/fhirschmann/tucan.git

Setup
`````

Set your username and password:

.. code:: bash

    cat << EOF >> ~/.netrc
    machine www.tucan.tu-darmstadt.de
        login ab34abab
        password secret
    EOF

Manual checking
```````````````

Run

.. code:: bash

    tucan

to print all grades in the current semester:

.. code:: bash

    tucan -n

to print only new grades.

Periodic checking
`````````````````

Edit your crontab

.. code:: bash

    crontab -e

And add this in order to check every 60 minutes:

.. code:: bash

    */60 * * * * /usr/local/bin/tucan -m me@email.com

This utility can also send notifications on Linux systems:

.. code:: bash

    */60 * * * * /usr/local/bin/tucan -n

Help
````

.. code:: text

    usage: tucan [-h] [--mail MAIL] [--db DB] [--new] [--notify] [--json]

    TUCaN CLI

    optional arguments:
      -h, --help            show this help message and exit
      --mail MAIL, -m MAIL  send email to this address on changes (default: None)
      --db DB               database file (default: /home/fabian/.tucandb)
      --new                 print only new grades (default: False)
      --notify, -n          send desktop notification on new grades (default:
                            False)
      --json, -j            output json (default: False)
