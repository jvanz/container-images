FROM opensuse/leap:15

RUN zypper -n update
RUN zypper -n install tar gzip gcc pcre-devel zlib-devel make python3

#COPY lighttpd-1.4.29.tar.gz /
COPY http://download.lighttpd.net/lighttpd/releases-1.4.x/lighttpd-1.4.29.tar.gz /

RUN gzip -cd lighttpd-1.4.29.tar.gz | tar xf -
WORKDIR lighttpd-1.4.29
RUN ./configure --without-bzip2
RUN make
RUN make install

EXPOSE 8080
WORKDIR /

RUN mkdir -p /var/www/cgi-bin
RUN mkdir -p /var/cache/lighttpd/uploads
COPY upload.py /var/www/cgi-bin/upload.py
RUN chmod 0755 /var/www/cgi-bin/upload.py

COPY lighttpd.conf /etc/lighttpd/lighttpd.conf
COPY entrypoint.sh /

RUN mkdir -p /var/log/lighttpd
RUN chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
