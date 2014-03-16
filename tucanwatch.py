#!/usr/bin/env python
# -*- coding: utf-8 -*-

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
        print("\n".join(grades))
    else:
        import subprocess
        from time import sleep

        while True:
            sleep(60 * 60)

            grades2 = grades2set(get_grades(username, password))
            diff = grades2.difference(grades)

            if len(diff) > 0:
                proc = subprocess.Popen(["mail", "-s", "New Grade in TuCaN", "fabian@0x0b.de"],
                                        stdin=subprocess.PIPE)
                proc.stdin.write("\n".join(diff))
                proc.stdin.close()
                proc.terminate()

                grades = grades2
