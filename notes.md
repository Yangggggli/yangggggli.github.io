---
layout: page
permalink: /notes/index.html
title: Notes
notes:
  - author: "Li Yang"
    title: "Chow's thm"
    month: 
    year: 
    url: Chow's_thm.pdf
    hidden: false
  - author: "Li Yang"
    title: "report for \"Introduction to Topology\""
    month: 
    year: 
    url: report_for_Introduction_to_Topology.pdf
    hidden: false

  - author: "Li Yang"
    title: "李代数上同调"
    month: 
    year: 
    url: 李代数上同调.pdf
    hidden: false
---

# Notes

{% for note in page.notes %}
{% unless note.hidden %}
  - {% if note.url %} [{{note.title}}]({{note.url}}).
    {% else %} {{note.title}}.
    {% endif %}
    {{note.author}}.<br>
    {% if note.month %}
    {{note.month}}, {{note.year}}.
    {% endif %}
{% endunless %}
{% endfor %}



