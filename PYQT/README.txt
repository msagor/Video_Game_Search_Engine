this is the video game search engine app.
youll need solr 2.7.2, python 2.7, and pyqt4

Setup:
download the entire folder and paste on desktop.

then open the windows command prompt, 
then execute search.py, it will start the application.(python 2.7 needed)

for the application to work on solr server, you need solr server setup on 
your windows machine, data indexed in the solr server. other wise, the app
just wont return anything because it is not tied to a solr server yet.

The app assumes:
- that the solr server is running on 192.168.56.1 host ip at 8983 port. 
- the solr core is named "task3".
- a data that is indexed in solr server is .json format. an example of a data would be:
[{"title": ["NHL 2003"], "platform": ["Playstation 2"], "genre": ["Sports"], "release": ["2003-02-06"], "rating": ["3"]}]


