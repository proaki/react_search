FROM docker.elastic.co/elasticsearch/elasticsearch:7.11.0

RUN echo "discovery.type: single-node" >> /usr/share/elasticsearch/config/elasticsearch.yml
RUN echo "http.cors.enabled: true" >> /usr/share/elasticsearch/config/elasticsearch.yml
RUN echo "http.cors.allow-credentials: true" >> /usr/share/elasticsearch/config/elasticsearch.yml
RUN echo 'http.cors.allow-origin: "*"' >> /usr/share/elasticsearch/config/elasticsearch.yml
RUN echo "http.cors.allow-headers: X-Requested-With, X-Auth-Token, Content-Type, Content-Length, Authorization, Access-Control-Allow-Headers, Accept" >> /usr/share/elasticsearch/config/elasticsearch.yml

EXPOSE 9200