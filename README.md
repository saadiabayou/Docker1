
                                                        --- PROJETS DOCKER ---
                                                        ----------------------



Objectifs : Créer des projets autours de Docker
----------

Sujet 
------

Projet n°1 : Faire tourner une application Python Flask dans un container Docker. 

- Pour se faire , les éléments suivants sont crées :


- Un script Python , importation du framwork Flask et une apllication que l'on nomme app dans "script1.py" 
  
  Flask fonctionne par défault sur le port 5000 , on fait le choix de faire fonctionner cette application sur le port 9090.


- Un fichier Dockerfile qui comportera les caractéristques suivantes :

	- Choix de l'OS pour l'image Debian 9, (on pourra choisir une autre distrtibution Linux)
	- Installation de Python et de des packages Flask 
	- Copie du script Python-Flask fichier "script1.py" dans l'image futur container Docker 
	- Exécution le script 

Pour pouvoir observer le résultat , c'est à dire que l'application tourne correctement , 
il faudra s'assurer le mappage de ports a bien été effectué , pour cela , il est précisé dans la commande 
docker run du fichier Makefile avec l'option -p : 

port container 9090 -> port machine hote 9090 

- Un fichier Makefile pour le lancement de l'éxécution du programme.
 	
 	make build -> construit l'image "demo1"
 	make run -> génère le container nommer "app1"  


Exécution du programme :
-----------------------










