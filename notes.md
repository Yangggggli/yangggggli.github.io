---
layout: page
permalink: /notes/index.html
title: Notes
notes:
  - author: "Li Yang"
    title: ""
    date: ""
    url: .pdf
    hidden: true

  - author: "Li Yang"
    title: "Notes on Connections on vector bundles"
    date: "2018.9.27-2018.10.17"
    url: Notes on Connections on vector bundles.pdf
    hidden: false

  - author: "Li Yang"
    title: "Notes on Chern connection on holomorphic vector bundles and Chern class"
    date: "2018.10.19-2018.11.2"
    url: Notes on Chern connection on holomorphic vector bundles and Chern class.pdf
    hidden: false

  - author: "Li Yang"
    title: "Notes on Connections on principal bundle and Chern-Weil theory"
    date: "2018.11.07-2018.11.23"
    url: Notes on Connections on principal bundle and Chern-Weil theory.pdf
    hidden: false

  - author: "Li Yang"
    title: "Supplements on computations of curvature on Kähler manifold"
    date: "2018.11.28-2018.11.30"
    url: Supplements on computations of curvature on Kähler manifold.pdf
    hidden: false

  - author: "Li Yang"
    title: "unfinished notes on divisors and sheaves of modules"
    date: "2018.12.5"
    url: unfinished notes on divisors and sheaves of modules.pdf
    hidden: false

  - author: "Li Yang"
    title: "Riemann surface1"
    date: "2018.3-2018.6"
    url: Riemann surface1.pdf
    hidden: false

  - author: "Li Yang"
    title: "Chow's thm and GAGA"
    date: "2018.10.28"
    url: Chow's thm and GAGA.pdf
    hidden: false

  - author: "Li Yang"
    title: "李代数上同调"
    date: "2018.05.03"
    url: 李代数上同调.pdf
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



