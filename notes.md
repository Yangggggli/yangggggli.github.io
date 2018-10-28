---
layout: page
permalink: /notes/index.html
title: Notes
notes:
  - author: "Li Yang"
    title: "Chow's thm"
    date: "2018.10.28"
    url: Chow's_thm.pdf
    hidden: false

  - author: "Li Yang"
    title: "李代数上同调"
    date: "2018.05.03"
    url: 李代数上同调.pdf
    hidden: false

  - author: "Li Yang"
    title: "report for \"Introduction to Topology\""
    date: "2018.02.20"
    url: report_for_Introduction_to_Topology.pdf
    hidden: false
---

# Notes

{% for note in page.notes %}
{% unless note.hidden %}
  - {% if note.url %} [{{note.title}}]({{note.url}}).
    {% else %} {{note.title}}.
    {% endif %}<br>
    {{note.author}}.<br>
    {{note.date}}.<br>
{% endunless %}
{% endfor %}



