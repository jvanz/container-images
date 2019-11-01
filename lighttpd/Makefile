all:
	sudo podman build -f Dockerfile -t lighttpd:1.4.29 .

run: 
	sudo podman run --network host -d  lighttpd:1.4.29

update:
	sudo cp $(PWD)/upload.py $(shell sudo podman mount $(container))/var/www/cgi-bin/upload.py
	sudo podman unmount $(container)

check:
	sudo podman exec $(container) cat /var/www/cgi-bin/upload.py

check-file:
	sudo tail $(shell sudo podman mount $(container))/tmp/file
	sudo podman unmount $(container)

send:
	curl --request POST -k -v --form file=@$(PWD)/file --form press=OK http://localhost:8080/cgi-bin/upload.py

test: update send check-file
restart: clean all run

stop:
	sudo podman stop --all

clean: stop
	sudo podman rm --all

play:
	sudo podman run -ti --entrypoint bash lighttpd:1.4.29
