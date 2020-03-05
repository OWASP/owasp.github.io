{% assign pleaders = site.data.leaders | where: 'group-type','project' %}
{% for leader in pleaders %}
{{ leader.name }} : {{ leader.group }}
{% endfor %}
