# Gestion de l'execution du programme demo Docker - App flask

all : 


build: 
	docker build -t demo1 .

run : 
	docker run --name app1 -p 9090:9090 demo1 

stop :
	 docker stop app1

start : 
	docker start app1

clean :
	docker rm app1

curl :
	curl http://0.0.0.0:9090/
		

