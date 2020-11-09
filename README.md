# Classification_Knn_algorithm
Code to implement the Knn algorithm, classifying between 10 classes according to the dataset I used. To compare,
the accuracy obtained with a random forest model using random forest function on Rstudio is 0.87. We can deduce that
this model is correct since random forest is a good model for classification.


The data.csv file contains the training dataset, data_eval.csv is the testing dataset to evaluate the accuracy.
Here I did not use particular heuristic. The formula for the distance between points is the Euclidian one but
we could use another one.
We could take into account the frequency of each class in the training set when we look at the class the most 
present around the individual to classify. 
We could also weight with the distance of the nearest points. (line 46)


Code pour implémenter le Knn, avec 10 classes différentes possibles comme réponse. On obtient une précision
de 0.87 avec la fonction random forest sur Rstudio, ce qui est autant que ce modèle. On peut en déduire que
ce modèle est plutôt précis.

Le fichier data.csvcontient les données d'entrainement, le fichier data_eval.csv contient les données test 
dont on connait la classe, afin d'évaluer la précision du modèle .
Aucune heuristique particulière n'a été utilisée. On utilise ici la distance euclidienne pour le calcul 
des distances mais on pourrait en utiliser d'autres.
On pourrait aussi regarder la fréquence de chacune des classes dans les données d'entrainement et ponderer 
la somme du nombre de points proches de chaque classe par cette fréquence.
On pourrait également pondérer par l'inverse de la distance de points proches comme proposé en commentaire
dans le code (ligne 46)

