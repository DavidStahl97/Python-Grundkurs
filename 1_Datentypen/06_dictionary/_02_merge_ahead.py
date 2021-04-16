# ############ merging dictionaries #############
#
# Overview:
# Often we have multiple dictionaries and want to combine
# them. For example, we have separate dictionaries
# that hold query string data, route data, and POST data. Merging
# these makes access form data easier. That's just one example.
#

route = {'id': 271, 'title': 'Fast apps'}
query = {'id': 1, 'render_fast': True}
post = {'email': 'j@j.com', 'name': 'Jeff'}

print("Individual dictionaries: ")
print("route: {}".format(route))
print("query: {}".format(query))
print("post:  {}".format(post))

# Non-pythonic procedural way


# Classic pythonic way:


# Via dictionary comprehensions:


# Python 3.5+ pythonic way, warning crashes on Python <= 3.4:

