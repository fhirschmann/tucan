tucanwatch
----------

Notifies you via email when there are new grades available in
the campus management system of Technische Universität Darmstadt.

Installation
````````````

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

    tucan

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

    */60 * * * * /home/user/bin/tucanwatch.py -m me@email.com 2>&1 >>/dev/null
