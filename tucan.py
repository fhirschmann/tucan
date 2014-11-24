#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function

import mechanize
from lxml import html


def get_grades(username, password):
    br = mechanize.Browser()
    br.open("https://www.tucan.tu-darmstadt.de/scripts/mgrqcgi?APPNAME=CampusNet&PRGNAME=STARTPAGE_DISPATCH&ARGUMENTS=-N000000000000001")
    br.select_form(nr=0)
    br.form["usrname"] = username
    br.form["pass"] = password
    br.submit()

    br.follow_link(text_regex=u"^Prüfungen$")
    br.follow_link(text_regex=u"^Semesterergebnisse$")
    br.follow_link(text_regex=u"^Prüfungsergebnisse$")

    tree = html.fromstring(br.response().read())
    tbody = tree.xpath("//table[@class='nb list']/tbody")[0]

    grades = [[" ".join(unicode(td.text).strip().split())
               for td in tr.findall("td")][:-1]
              for tr in tbody.findall("tr")]
    return grades
