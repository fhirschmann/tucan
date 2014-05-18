tucanwatch
----------

Notifies you via email when there are new grades available in
the campus management system of Technische Universität Darmstadt.

Installation
````````````

It might be better to use your system's package manager to install
the required dependencies:

.. code:: bash

    apt-get install python-mechanize python-lxml python-pip

Then install tucanwatch via pip:

.. code:: bash

    pip install git+git://github.com/fhirschmann/tucanwatch.git

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

    tucan -a

to print all grades in the current semester or

.. code:: bash

    tucan

to print only new grades.

Periodic checking
`````````````````

Edit your crontab

.. code:: bash

    crontab -e

And add this in order to check every 60 minutes:

.. code:: bash

    */60 * * * * /usr/local/bin/tucan -m me@email.com

If tucan is down and you don't want to receive errors, run

    */60 * * * * /usr/local/bin/tucan -q -m me@email.com
