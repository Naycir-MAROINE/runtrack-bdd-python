 Pour ajouter à ma table “etudiant” un élève nommé Martin Dupuis, j'ai utiliser :
 INSERT INTO etidiant (nom,prenom,age,email) VALUES('Dupuis', 'Martin',18,'Dupuis.Martin@laplateforme.io');

 Pour recuperer les membres de la meme famille j'ai utiliser :
 SELECT * FROM etidiant WHERE nom = 'Dupuis'