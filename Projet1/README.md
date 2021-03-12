
                         --- PROJETS DOCKER ---



Objectifs : Créer des projets autours de Docker
----------

Sujet 
------

Projet n°1 : On souhaite faire tourner une application Python Flask dans un container Docker. 

Pour se faire, on suit les étapes suivantes :

- Créer un script Python en important le framwork Flask avec une apllication que l'on nomme app : "script1.py" 
  
  Flask fonctionne par défault sur le port 5000 , on fait le choix de faire fonctionner cette application sur le port 9090.


- Ecrire un Dockerfile qui comportera les caractéristques suivantes :

	- Choix de l'OS pour l'image Debian 9, (on pourra choisir une autre distrtibution Linux)
	- Installation de Python et de des packages Flask 
	- Copie du script Python-Flask fichier "script1.py" dans l'image futur container Docker 
	- Exécution le script 

Pour pouvoir bien observer le résultat , c'est à dire que l'application tourne correctement , 
il faudra s'assurer le mappage de ports a bien été effectué , pour cela , il est précisé dans la commande 
docker run du fichier Makefile avec l'option -p : 

port container 9090 -> port machine hote 9090 

- Créer un fichier Makefile pour le lancement de l'éxécution des commandes Docker.
 	
 	make build -> construit l'image "demo1"
 	make run -> génère le container nommer "app1"  


Exécution du programme :
-----------------------



