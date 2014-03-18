#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
import os

import mechanize
from lxml import html


def get_grades(username, password):
    br = mechanize.Browser()
    br.open("https://www.tucan.tu-darmstadt.de")
    br.select_form(nr=0)
    br.form["usrname"] = username
    br.form["pass"] = password
    br.submit()

    br.follow_link(text_regex=u"^Prüfungen$")
    br.follow_link(text_regex=u"^Semesterergebnisse$")
    br.follow_link(text_regex=u"^Prüfungsergebnisse$")

    tree = html.fromstring(br.response().read())
    tbody = tree.xpath("//table[@class='nb list']/tbody")[0]

    grades = [[" ".join("".join(c for c in td.text if c.isalnum()
                                or c in (".", " ", "-", ",")).strip().split())
               for td in tr.findall("td")][:-1] for tr in tbody.findall("tr")]
    return grades


def grades2set(grades):
    return set([e[0] + ": " + e[2] for e in grades])


if __name__ == "__main__":
    import sys
    from netrc import netrc

    username, account, password = netrc().authenticators("www.tucan.tu-darmstadt.de")
    grades = grades2set(get_grades(username, password))

    if "-p" in sys.argv:
        print(*grades, sep=os.linesep)
    else:
        import shelve

        data = shelve.open(os.path.expanduser("~/.tucan.grades"))
        if "grades" not in data:
            data["grades"] = set()

        if data["grades"] != grades:
            print("The following new grades are available:",
                  *grades.difference(data["grades"]), sep=os.linesep)

        data["grades"] = grades
        data.close()
