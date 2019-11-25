
all: build run

build:
	docker build . -t java_crash:latest

run:
	docker run --memory=150m --rm -ti java_crash MainClass 70 1
