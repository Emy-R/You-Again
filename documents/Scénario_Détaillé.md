# Scénario détaillé du projet : "Patate Carnivore"

Ce document sert à ce que toute l'équipe sache exactement quel est le scénario du jeu, comment accéder à quelle scènes, quoi rédiger sur les images/scènes de victoires/scènes de morts (etc...) au moment de les implémenter dans le projet. Ce document montre exacement comment les scènes doivent être reliées les unes avec les autres afin que tout le monde puisse les implémenter. 

## Comment lire ce document :

### Les différentes scènes se présentent comme ceci :
**X. Description de la scène**\
*Choix amenant à la scène Y -> Y (manière d'accéder à la scène)*\
***OU*** *(facultatif)*\
*Choix amenant à la scène Z -> Z (manière d'accéder à la scène)*\
***OU*** *(facultatif)*\
etc....

### Important à noter :

* X, Y, Z etc… Ne sont pas forcément des nombres, ils représentent simplement le nom du fichier png associé, par exemple :
    * Menu. fait référence à Menu.png
    * 1. fait référence à i1.png
    * 2. fait référence à i2.png
    * 3. fait référence à i3.png

* Dans certaines scènes, le passage à la scène suivante se fait à l’aide d’un click du joueur, ce sont les scènes “cliquables” et ce cas de figure est représenté par le (click), dans d’autres, c’est simplement le temps qui fait passer à une scène suivante (les scènes “Animation”) et ce cas de figure, lui, est représenté par le (auto)

* Pendant la rédaction de ce document, certaines scènes n’étaient pas prêtes donc des numérotation temporaires sont susceptibles d’être présentes, par exemple : x1, x2, x3, y1 etc… (Certaines informations sur ces numérotations spéciales se trouvent en fin de document)

## Scènes :

**Menu. Écran titre**\
*Bouton Quitter -> 1 (click)*\
***OU***\
*Bouton Commencer -> 2 (click)*

1. **Retour au menu avec des "non"**\
*Bouton Quitter -> 1 (click)*\
***OU*** \
*Bouton Commencer -> 2 (click)*

2. **Tu viens de te réveiller, tu es dans ton lit et il y a un sorcier effrayant à ta fenêtre, que fais-tu ?**\
*Tu vas fermer à clé ta fenêtre -> 3 (click)*\
***OU***\
*Tu retournes dormir -> 4 (click)*

3. **Tu te lèves pour aller fermer la fenêtre mais tu meurs, tué par une patate carnivore**\
*Passage à l’écran de mort correspondant -> x1 (auto)*

4. **Tu dors**\
*Passage à la scène suivante -> 5 (auto)*

5. **Tu te réveilles plus tard et tu remarques que le sorcier est parti, que fais-tu ?**\
*Tu vas prendre une douche -> 6 (click)*\
***OU***\
*Tu vas te raser -> 9 (click)*

6. **Tu es dans la douche, comment veux-tu te laver ?**\
*à l'eau chaude -> 8 (click)*\
***OU***\
*à l'eau froide -> 7 (click)*

7. **Des fourmis en feu sortent à la place de l'eau et tu meurs**\
*Passage à l'écran de mort correspondant -> x2 (auto)*

8. **De l'eau normale et bien bleue coule, tout se passe bien**\
*Passage à la scène suivante -> 12 (auto)*

9. **Tu vas maintenant devant ton miroir dans ta salle de bain pour te raser, que fais-tu maintenant ?**\
*Tu te rases -> 10 (click)*\
***OU***\
*Tu manges le miroir comme un idiot -> 11 (click)*

10. **Animation : Tu prends le rasoir en main**\
*Passage à la scène suivante -> 17 (auto)*

11. **Animation :Tu manges le miroir**\
*Passage à l'écran de mort correspondant -> x3 (auto)*

12. **Tu es super propre ! Que fais-tu maintenant ?**\
*Tu descend les escaliers -> 18 (click)*\
***OU***\
*Tu te jettes par la fenêtre -> 13 (click)*

13. **Scène juste après que le joueur ait décidé de se jeter par la fenêtre**\
*Passage à la scène suivante -> 14 (auto)*

14. **Animation du perso qui se jette par la fenêtre (frame 1)**\
*Passage à la scène suivante -> 15 (auto)*

15. **Animation du perso qui se jette par la fenêtre (frame 2)**\
*Passage à la scène suivante -> 16 (auto)*

16. **Animation du perso qui se jette par la fenêtre (frame 3) (on ne voit plus le perso)**\
*Passage à la scène suivante -> 20 (auto)*

17. **Tu te rends compte que tu n'as pas de barbe, que fais-tu maintenant ?**\
*Tu vas te laver -> 6 (click)*\
***OU***\
*Tu manges ton miroir -> 11 (click)*

18. **Animation du perso qui descend les escaliers (frame 1)**\
*Passage à la scène suivante -> 77 (auto)*

19. **Tu es maintenant en bas de tes escaliers, que décides-tu de faire ?**\
*Prendre ton petit déjeuner -> 22 (click)*\
***OU***\
*Aller regarder la télé -> 28 (click)*

20. **Le perso a sauté par la fenêtre et il est maintenant devant sa porte (au sol)**\
*Passage à la scène suivante -> 21 (auto)*

21. **Tu tombes devant ta maison et tu te relèves, que décides-tu de faire maintenant ?**\
*Passage à la scène suivante -> 21 (auto)*

22. **Tu es à table ! Que veux-tu manger à présent ?**\
*Un petit déjeuner au chocolat -> 23 (click)*\
***OU***\
*Du dentifrice -> 24 (click)*

23. **Animation : Le petit dej au chocolat apparaît sur la table**\
*Passage à la scène suivante -> 38 (auto)*

24. **Le dentifrice apparaît sur la table**\
*Passage à la scène suivante -> 25 (auto)

25. **Le perso a mangé le dentifrice et il est content (il en a sur la bouche)**\
*Passage à la scène suivante -> 26 (auto)*

26. **Zoom sur l'arrière du dentifrice**\
*Passage à la scène suivante -> 27 (auto)*

27. **Le perso réalise ce qu'il vient de faire, La patate débarque puis on enchaine sur un écran de mort**
*Passage à l'écran de mort correspondant -> x4*

28. **Tu es confortablement installé sur ton fauteuil, que veux-tu regarder ?**\
*Food Network (une émission sur de la bouffe) -> 29 (click)*\
***OU***\
*Judge Judy (Une émission sur des juges) -> 40 (click)*

29. **L'émission parle de pommes de terre aujourd'hui**\
*Passage à la scène suivante -> 30 (auto)*

30. **La patate carnivore débarque en brisant la télé en deux et te tue**\
*Passage à l'écran de mort correspondant -> x5 (auto)*


31. **Tu arrives devant ta boîte aux lettres, que décides-tu de faire ?**\
*Prendre le courrier -> 32 (click)*\
***OU***\
*Ne pas prendre le courrier -> 34 (click)*

32. **Tu as récupéré une lettre !**\
*Passage à la scène suivante -> 33 (auto)*

33. **La mamie débarque !**\
*Passage à la scène suivante -> 44 (auto)*

34. **Tu décides de ne pas prendre la lettre, la patate carnivore débarque**\
*Passage à l’écran de mort correspondant -> x6 (auto)*

35. **Tu es à présent dans ton jardin, que fais-tu maintenant ?**\
*Tu touches le buisson -> 37 (click)*\
***OU***\
*Tu manges l’herbe -> 36 (click)*

36. **Le perso prend de l'herbe dans sa main**\
*Passage à la scène suivante -> 45 (auto)*

37. **Le perso touche le buisson et le roi Charles sort et le lèche (le faire glisser derrière le buisson en superposant les sprites)**\
*Passage à la scène suivante -> 83 (auto)*

38. **Le petit déjeuner au chocolat est délicieux ! Que veux-tu faire à présent ?**\
*Continuer de manger -> 39 (click)*\
***OU***\
*Arrêter de manger -> 46 (click)*

39. **Le roi Charles sort de sous la table et le lèche (il lèche classiquement ou carrément on switch direct à l’ecran de mort après le eye contact)**\
*Passage à l’écran de mort correspondant -> x7 (auto)*

40. **Tu regardes cette émission qui est plutôt intéressante, que décides tu de faire maintenant ?**\
*Continuer à regarder l’émission -> 41 (click)*\
***OU***\
*Arrêter de regarder -> 42 (click)*

41. **Le perso continue de regarder l'émission sur les juges pendant environ 1 seconde**\
*Passage à la scène suivante -> 30 (auto)*

42. **Le roi Charles sort derrière la télé**\
*Passage à la scène suivante -> 43 (auto)*

43. **Scène hyper épique d'action où le roi Charles troisième du nom course le perso**\
*Passage à la scène suivante -> 47 (auto)*

44. **Tu as récupéré une lettre ! Mais une grand mère folle débarque et essaye de te voler ton courrier, que fais-tu ?**\
*Se battre -> 237(click)*\
***OU***\
*Fuir -> 52 (click)*

45. **L’herbe est délicieuse, que décides-tu de faire maintenant ?**\
*Tu touches le buisson -> 37 (click)*\
***OU***\
*Tu gagnes le jeu -> 53 (click)*

46. **Tu as arrêté de manger, que fais-tu maintenant ?**\
*Tu vas dehors -> 96 (click)*\
***OU***\
*Tu décides de ne plus rien faire -> 95 (click)*\
***OU***\
*Tu vas regarder la télé -> 59 (click)*

47. **Le chat sur un tapis volant t'as sauvé au dernier moment. Il te demande 5$ en dédommagement**\
*Tu le payes -> 48 (click)*\
***OU***\
*Tu refuses de le payer -> 50 (click)*

48. **Le perso prend la pièce dans sa main pour la donner au chat**\
*Passage à la scène suivante -> 49 (auto)*

49. **Le perso et le chat débarquent en tapis volant, le chat dépose le perso devant chez lui**\
*Passage à la scène suivante -> 60 (auto)*

50. **Gros blanc bien gênant**\
*Passage à l’écran de mort correspondant -> x8 (auto)*

51. **Mini jeu où le joueur doit cliquer sur la mamie**\
*Il gagne -> 61*\
***OU***\
*Il perd, passage à l’écran de mort correspondant -> x9*

52. **Le perso court sur le gazon puis se rend compte que le gazon est mouillé**\
*Passage à l’écran de mort correspondant -> x10 (auto)*

53. **Un trophée tombe du ciel, si tu le touches, tu gagnes le jeu, que décides-tu de faire ?**\
*Tu touches le buisson -> 56 (click)*\
***OU***\
*Tu manges de l’herbe -> 57 (click)*\
***OU***\
*Tu touches le trophée -> 54 (click)*

54. **Animation : le perso glisse avec la main tendue vers la gauche pour toucher le trophée**\
*Passage à la scène suivante -> 55 (auto)*

55. **Animation : Patate qui descend diagonale droite sur perso**\
*Passage à l’écran de mort correspondant -> x11 (auto)*

56. **Le roi Charles sort de derrière le buisson**\
*Passage à la scène suivante -> 89 (auto)*

57. **Animation : Prend l’herbe dans sa main**\
*Passage à la scène suivante -> 58 (auto)*

57c. **Animation : Prend l’herbe dans sa main**\
*Passage à la scène suivante -> 58c (auto)*

57d. **Animation : Prend l’herbe dans sa main**\
*Passage à la scène suivante -> 58d (auto)*

57e. **Animation : Prend l’herbe dans sa main**\
*Passage à la scène suivante -> 58e (auto)*

57f. **Animation : Prend l’herbe dans sa main**\
*Passage à la scène suivante -> 63 (auto)*

58. **Un trophée tombe du ciel, si tu le touches, tu gagnes le jeu, que décides-tu de faire ?**\
*Tu touches le buisson -> 56 (click)*\
***OU***\
*Tu manges de l’herbe -> 57c (click)*\
***OU***\
*Tu touches le trophée -> 54 (click)*

58c. **Un trophée tombe du ciel, si tu le touches, tu gagnes le jeu, que décides-tu de faire ?**\
*Tu touches le buisson -> 56 (click)*\
***OU***\
*Tu manges de l’herbe -> 57d (click)*\
***OU***\
*Tu touches le trophée -> 54 (click)*

58d. **Un trophée tombe du ciel, si tu le touches, tu gagnes le jeu, que décides-tu de faire ?**\
*Tu touches le buisson -> 56 (click)*\
***OU***\
*Tu manges de l’herbe -> 57e (click)*\
***OU***\
*Tu touches le trophée -> 54 (click)*

58e. **Un trophée tombe du ciel, si tu le touches, tu gagnes le jeu, que décides-tu de faire ?**\
*Tu touches le buisson -> 56 (click)*\
***OU***\
*Tu manges de l’herbe -> 57f (click)*\
***OU***\
*Tu touches le trophée -> 54 (click)*

59. **Tu es confortablement installé sur ton fauteuil, que veux-tu regarder ?**\
*Food Network (une émission sur de la bouffe) -> 29 (click)*\
***OU***\
*Judge Judy (Une émission sur des juges) -> 40 (click)*\
***OU***\
*Chaîne mystérieuse -> 68 (click)*

60. **Le chat te ramène devant chez toi, que fais-tu maintenant ?**\
*Tondre le gazon -> 97 (click)*\
***OU***\
*Aller dans le parking -> 98 (click)*

61. **La mamie est au sol, tu es victorieux. Que fais-tu ?**\
*Tu retourner chez toi -> 62 (click)*\
***OU***\
*Tu manges la lettre -> 70 (click)*

62. **Animation : Le perso rentre chez lui, la patate surgit et tue le perso**\
*Passage à l’écran de mort correspondant -> x12 (auto)*

63. **Tu remarques après avoir dévoré à de nombreuses reprises l’herbe qu’il y a un trou dans ton jardin, que décides-tu de faire ?**\
*Tu touches le trophée -> 54 (click)*\
***OU***\
*Tu sautes dans le trou -> 64 (click)*\
***OU***\
*Tu touches le buisson -> 56 (click)*

64. **Animation : Le perso saute dans le trou (frame 1)**\
*Passage à la scène suivante -> 65 (auto)*

65. **Animation : Le perso saute dans le trou (frame 2)**\
*Passage à la scène suivante -> 66 (auto)*

66. **Animation : Le perso saute dans le trou (frame 2)**\
*Passage à la scène suivante -> 67 (auto)*

67. **Animation : Le perso arrive dans le souterrain et les taupes débarquent**\
*Passage à la scène suivante -> 72 (auto)*

68. **Animation : Affichage du code secret (random)**\
*Passage à la scène suivante -> 28 (auto)*

69. **Mini jeux : snake**\
*Se cogne contre un mur -> x13*\
***OU***\
*Écraser les patates -> x14*\
***OU***\
*Foncer dans la boite au lettre -> 31*

70. **Tu as mangé la lettre. Que fais-tu maintenant ?**\
*Tu fouilles la mamie -> 71 (click)*\
***OU***\
*Tu retournes chez toi -> 74 (click)*

71. **Animation : Le sandwich apparaît avec un bruit angélique**\
*Passage à la scène suivante -> 76 (auto)*

72. **Tu te retrouves dans des souterrains, soudain des taupes surgissent et te demandent de partir. Que fais-tu ?**\
*Tu pars -> 99 (click)*\
***OU***\
*Tu restes -> 73 (click)*

73. **Animation : Les taupes sont énervées**\
*Passage à l’écran de mort correspondant -> x15 (auto)*

74. **Tu es de retour devant ta maison mais Burger man débarque en brandissant son épée et te demandé un sandwich. Que fais-tu ?**\
*Tu ne lui donne rien -> 75 (click)*

75. **Animation : Burger Man saute sur le perso**\
*Passage à l’écran de mort correspondant -> x16 (auto)*

76. **En fouillant la mamie tu trouves un sandwich, que décides-tu de faire ?**\
*Tu manges le sandwich -> 100 (click)*\
***OU***\
*Tu reviens à la maison -> 101 (click)*

77. **Animation du perso qui descend les escaliers (frame 2)**\
*Passage à la scène suivante -> 78 (auto)*

78. **Animation du perso qui descend les escaliers (frame 3)**\
*Passage à la scène suivante -> 79 (auto)*

79. **Animation du perso qui descend les escaliers (frame 4)**\
*Passage à la scène suivante -> 80 (auto)*

80. **Animation du perso qui descend les escaliers (frame 5)**\
*Passage à la scène suivante -> 81 (auto)*

81. **Animation du perso qui descend les escaliers (frame 6)**\
*Passage à la scène suivante -> 82 (auto)*

82. **Animation du perso qui descend les escaliers (frame 7)**\
*Passage à la scène suivante -> 19 (auto)*

83. **Roi Charles te lèche après le buisson (sans le trophée) (frame 1)**\
*Passage à la scène suivante -> 84 (auto)*

84. **Roi Charles te lèche après le buisson (sans le trophée) (frame 2)**\
*Passage à la scène suivante -> 85 (auto)*

85. **Roi Charles te lèche après le buisson (sans le trophée) (frame 3)**\
*Passage à la scène suivante -> 86 (auto)*

86. **Roi Charles te lèche après le buisson (sans le trophée) (frame 4)**\
*Passage à la scène suivante -> 87 (auto)*

87. **Roi Charles te lèche après le buisson (sans le trophée) (frame 5)**\
*Passage à la scène suivante -> 88 (auto)*

88. **Roi Charles te lèche après le buisson (sans le trophée) (frame 6)**\
*Passage à l’écran de mort correspondant -> x17 (auto)*

89. **Roi Charles te lèche après le buisson (avec le trophée) (frame 1)**\
*Passage à la scène suivante -> 90 (auto)*

90. **Roi Charles te lèche après le buisson (avec le trophée) (frame 2)**\
*Passage à la scène suivante -> 91 (auto)*

91. **Roi Charles te lèche après le buisson (avec le trophée) (frame 3)**\
*Passage à la scène suivante -> 92 (auto)*

92. **Roi Charles te lèche après le buisson (avec le trophée) (frame 4)**\
*Passage à la scène suivante -> 93 (auto)*

93. **Roi Charles te lèche après le buisson (avec le trophée) (frame 5)**\
*Passage à la scène suivante -> 94 (auto)*

94. **Roi Charles te lèche après le buisson (avec le trophée) (frame 6)**\
*Passage à l’écran de mort correspondant -> x17 (auto)*

95. **Le jeu freeze**\
*Quitter avec escape*

96. **Tu es devant ta maison, que décides-tu de faire maintenant ?**\
*Tu vas chercher ton courrier -> 31 (auto)*\
***OU***\
*Tu vas dans ton jardin -> 35 (auto)*

97. **Animation : Burger man débarque et dit au perso qu’il DOIT écraser 3 patates**\
*Passage au mini-jeu snake -> 69 (auto)*

98. **Tu arrives dans le parking et tu vois deux véhicules en face de toi, lequel décides-tu d’emprunter ?**\
*La golfette -> 102 (click)*\
***OU***\
*La fusée -> 103 (click)*

99. **Tu as réussi à semer les taupes, que fais-tu maintenant ?**\
*Tu t’enfonces dans les souterrains -> 104 (click)*\
***OU***\
*Tu sors des souterrains -> 105 (click)*

100. **Tu entends les sirènes d’une voiture de police. Que fais-tu ?**\
*Tu restes immobile -> 106 (click)*\
***OU***\
*Tu te jettes sur la voiture de police -> 107(click)*


101. **Tu es de retour devant ta maison mais Burger man débarque en brandissant son épée et te demandé un sandwich. Que fais-tu ?**  
*Tu ne lui donne rien -> 75 (click)*  
***OU***  
*Tu lui donne le sandwich -> 118 (click)*  

102. **Animation : le perso entre dans la golfette puis commence à rouler sur la route puis se fait percuter par la voiture de policier**  
*Passage à l’écran de mort correspondant -> x18 (auto)*  

103. **Tu es à présent dans l’espace et tu vois que 3 planètes sont accessibles, sur laquelle tu décides d'atterrir ?**  
*Planète dauphinoise -> 108 (click)*  
***OU***  
*Planète zgu -> 109 (click)*  
***OU***  
*Planète h0kbcdX4H7DH -> 110 (click)*  

104. **Tu arrives dans un embranchement à deux chemins, lequel décides-tu d’emprunter ?**  
*Celui de gauche -> 111 (click)*  
***OU***  
*Celui de droite -> 112 (click)*  

105. **Tu es de retour dans ton jardin mais un papillon louche surgit. Que fais-tu ?**  
*Tu le laisses en vie -> 113 (click)*  
***OU***  
*Tu le tue -> 134 (click)*  

106. **Trois policiers débarquent et te voient à côté d’une mamie assommée. Ils te demandent si c’est de ta faute.**  
*Tu dis oui -> 114 (click)*  
***OU***  
*Tu frappes l’un des policiers -> 115 (click)*  

107. **Animation : Le perso fonce sur la voiture en mouvement et se fait renverser**  
*Passage à l'écran de mort correspondant -> x19 (auto)*  

108. **Animation : Le perso arrive sur la planète dauphinoise et la patate le tue**  
*Passage à l’écran de mort correspondant -> x20 (auto)*  

109. **Animation : Le perso arrive sur la planète zgu et zgublux le tue**  
*Passage à l’écran de mort correspondant -> x21 (auto)*  

110. **Tu arrives sur la planète mystérieuse et un blob interdimensionnel menaçant débarque, que fais-tu ?**  
*Tu t’enfuis dans ta fusée -> 103 (click)*  
***OU***  
*Tu suis le blob -> expli_4 (click)*  

111. **Tu arrives devant un coffre impressionnant, que veux-tu faire ?**  
*L’ouvrir -> 116 (click)*  
***OU***  
*Le laisser fermé -> 117 (click)*  

112. **Animation : Les fourmies arrivent de la gauche de l’image pour tuer le perso**  
*Passage à l’écran de mort correspondant -> x22 (auto)*  

113. **Tu es de retour dans ton jardin, que veux-tu faire ?**  
*Tu touches le trophée -> 121 (click)*  
***OU***  
*Tu sautes dans le trou -> 64 (click)*  
***OU***  
*Tu touches le buisson -> 228 (click)*  

114. **La police t’embarque. Dans la voiture, ils te demandent si tu aimes les pommes de terre, que fais-tu ?**  
*Tu réponds non -> 122 (click)*  
***OU***  
*Tu fais une sieste -> 123 (click)*  

115. **Quel policier veux-tu frapper ?**  
*Lui -> 124 (click)*  
***OU***  
*Jo -> 125 (click)*  
***OU***  
*Lui -> 126 (click)*  

116. **Animation : Le coffre s’ouvre**  
*Passage à la scène suivante -> 127 (auto)*  

117. **Animation : Les taupes énervées arrivent et percutent le perso**  
*Passage à l’écran de mort correspondant -> x23 (auto)*  

118. **Animation : Un portail interdimensionnel apparaît devant la maison**  
*Passage à la scène suivante -> 128 (auto)*  

119. **Animation : La fenêtre se brise, la patate tente de buter le perso mais le papillon s’interpose**  
*Passage à la scène suivante -> 129 (auto)*  

120. **Victoire : Blob party**  
*Passage à la scène de victoire suivante -> y1*  

121. **Animation : Le perso tend la main vers le trophée**  
*Passage à la scène suivante -> 119 (auto)*  

122. **Animation : La patate carnivore fonce sur la voiture**  
*Passage à l’écran de mort correspondant -> x24 (auto)*  

123. **Animation : Le perso ferme les yeux**  
*Passage à la scène suivante -> 130 (auto)*  

124. **Animation : Le perso frappe Tsvetelin Mitov**  
*Passage à la scène suivante -> 131 (auto)*  

125. **Animation : Le perso frappe Joe**  
*Passage à la scène suivante -> 132 (auto)*  

126. **Animation : Le perso frappe Zgublux3000**  
*Passage à la scène suivante -> 133 (auto)*  

127. **Animation : La potion apparaît comme dans Zelda avec un bruit angélique**  
*Passage à la scène suivante -> 135 (auto)*  

128. **Animation : Le perso est amené à Burger-land (le portail interdimensionnel est toujours là)**  
*Passage à la scène suivante -> 136 (auto)*  

129. **Victoire : Le perso prend le trophée en main**  
*Passage à l’écran de victoire correspondant -> y2*  

130. **Tu te réveilles et tu vois le sorcier en scooter, que décides-tu de faire ?**  
*Baisser la vitre -> 137 (click)*  
***OU***  
*Tirer la langue -> 138 (click)*  

131. **Animation : Tsvetelin pointe le flingue sur le perso**  
*Passage à l’écran de mort correspondant -> x25 (auto)*  

132. **Animation : Joe dit “aie mec”**  
*Passage à la scène suivante -> 106 (auto)*  

133. **Animation : Zgublux3000 prend sa forme d’alien**  
*Passage à la scène suivante -> 139 (auto)*  

134. **Tu as vaincu le papillon, que veux-tu faire maintenant ?**  
*Tu touches le trophée -> 54 (click)*  
***OU***  
*Tu sautes dans le trou -> 64 (click)*  
***OU***  
*Tu touches le buisson -> 56 (click)*  

135. **Une potion mystique se trouvait dans le coffre, que décides-tu de faire à présent ?**  
*La boire -> 140 (click)*  
***OU***  
*Ne pas la boire -> 141 (click)*  

136. **Tu es arrivé à “Burger-land” que veux-tu faire à présent ?**  
*Parler à un Burger -> 154 (click)*  
***OU***  
*Rentrer chez toi -> 155 (click)*  

137. **Animation : Le perso baisse la vitre**  
*Passage à la scène suivante -> 142 (auto)*  

138. **Animation : Le perso tire la langue**  
*Passage à la scène suivante -> 143 (auto)*  

139. **Animation : Zgublux3000 passe en vaisseau spatial de la gauche vers la droite puis de la droite avec la gauche avec le perso**  
*Passage à l’écran de mort correspondant -> x26 (auto)*  

140. **Le Dieu des maths apparaît et te demande combien font 2+2, que réponds-tu ?**  
*Tu réponds 3 -> 145 (click)*  
***OU***  
*Tu réponds 4 -> 146 (click)*  

141. **Tu as décidé de ne pas boire la potion, que fais-tu maintenant ?**  
*Tu dors -> 147 (click)*  
***OU***  
*Tu manges des cailloux -> 148 (click)*  

142. **Animation : Le sorcier dit “Salut”**  
*Passage à la scène suivante -> 149 (auto)*  

143. **Animation : On voit le perso regarder le sorcier depuis l’extérieur de la voiture, petit moment gênant**  
*Passage à la scène suivante -> 150 (auto)*  

144. **Animation : Le perso prend une pierre dans la main (avec la potion)**  
*Passage à la scène suivante -> 156 (auto)*  

145. **Bravo, bonne réponse ! Que fais-tu maintenant ?**  
*Tu dors -> 147 (click)*  
***OU***  
*Tu manges des cailloux -> 148 (click)*  

146. **Aie aie aie, mauvaise réponse, tu as froissé le Dieu des maths, que fais-tu maintenant ?**  
*Tu dors -> 144 (click)*  
***OU***  
*Tu manges des cailloux -> 151 (click)*  

147. **Animation : Le perso dort au sol (il n’est pas sous l’emprise de la potion)**  
*Passage à la scène suivante -> 152 (auto)*  

148. **Animation : Le perso prend une pierre dans sa main (sans la potion)**  
*Passage à la scène suivante -> 153 (auto)*  

149. **Animation : La voiture de police arrive devant le commissariat**  
*Passage à la scène suivante -> 157 (auto)*  

150. **Animation : Explosion google image sur la voiture**  
*Passage à l’écran de mort correspondant -> x27 (auto)*  

151. **Animation : Le perso dort au sol (avec la potion)**  
*Passage à la scène suivante -> r2 (auto)*  

152. **Animation : Tunnel vide avec les taupes qui transportent**  
*Passage à la scène suivante -> 160 (auto)*  

153. **Animation : Le perso a un grand sourire (sans la potion)**  
*Passage à l’écran de mort correspondant -> x28 (auto)*  

154. **Le burger te dit “Salade Tomate”, qu’est-ce que tu lui réponds ?**  
*Salade -> 161 (click)*  
***OU***  
*Tomate -> 162 (click)*  

155. **Tu te rends compte que le portail s’est refermé, tu es piégé pour l’instant, que décides-tu de faire ?**  
*Tu vas parler à un burger -> 154 (click)*  
***OU***  
*Tu pars explorer -> 163 (click)*  

156. **Animation : Le perso a un grand sourire (avec la potion)**  
*Passage à l’écran de mort correspondant -> x28 (auto)*  

157. **Tu es devant le commissariat, que décides-tu de faire ?**  
*Tu te laisses faire -> 164 (click)*  
***OU***  
*Tu pars en courant -> 165 (click)*  

158. **Tu viens de te réveiller, que décides-tu de faire ?**  
*Tu bois le chocolat chaud -> 159 (click)*  
***OU***  
*Tu sors explorer -> 166 (click)*  

159. **Animation : Le perso a du chocolat sur la bouche et commence à brûler**  
*Passage à l’écran de mort correspondant -> x29 (auto)*  

160. **Animation : Le perso dort sur le canapé**  
*Passage à la scène suivante -> 158 (auto)*  


161. **Le burger te pointe vers une rivière de mayonnaise, où souhaites-tu aller ?**\
*à la rivière -> 167* (click)\
***OU***\
*Tu vas ailleurs -> 163 (click)*

162. **Animation : Moment gênant entre le perso et le burger**\
*Passage à l’écran de mort correspondant -> x30 (auto)*

163. **Tu rencontres Cacahuète ! Que décides-tu de faire ?**\
*Partir en date -> expli_2 (click)*\
***OU***\
*Ignorer Cacahuète -> 167 (click)*

164. **La police t’a mis en garde-à-vue, dans la même cellule qu’un individu mystérieux, il te demande le code, que fais-tu ? [Le joueur peut écrire le code]**\
*Bon code -> 169*\
***OU***\
*Mauvais code -> 170*

165. **Animation : Le perso fuit (on ne voit probablement pas ses jambes) une bulle apparaît avec Joe qui dit “non mec”, puis Tsvetelin Mitov poursuit le perso avec son flingue puis le tue**\
*Passage à l'écran de mort correspondant -> x31 (auto)*

166. **Brrrrrr il fait super froid ! Que veux-tu prendre pour accéder au sommet de la montagne ?**\
*Le tir-fesse -> 185 (click)*\
***OU***\
*Le télésiège -> 186 (click)*

167. **Tu arrives devant la rivière de mayonnaise mais des frites carnivores débarquent, que fais-tu ?**\
*Se cacher dans la rivière -> 182 (click)*\
***OU***\
*Affronter les frites -> 183 (click)*

168. **[Mini-jeu date cacahuète]**\
*Gagner le mini-jeu -> 173*\
***OU***\
*Perdre le mini-jeu -> 174*

169. **Animation : Téléportation laser au dessus de la tête du mec**\
*Passage à la scène suivante -> 184 (auto)*

170. **La police t’amène en salle d’interrogatoire et te demande si tu as tué ou assommé la mamie, que réponds-tu ?**\
*Tu l’as tué -> 176 (click)*\
***OU***\
*Tu l’as assommé -> 177 (click)*

171. **Victoire : Tu rencontres le père Noël, vous faites du ski ensemble en pure légende**\
_Passage à l’écran de victoire correspondant -> y4_

172. **Animation : piste vide le perso arrive en ski et se fait chasser par l’ours polaire en ski**\
_Passage à l’écran de mort correspondant -> x32 (auto)_

173. **Vous partez en balade avec Cacahuète et vous vous retrouvez devant un temple mystique, que décidez-vous de faire ?**\
*Continuer votre chemin -> 178 (click)*\
***OU***\
*Visiter le temple -> 213 (click)*

174. **Animation : Le perso a la larme à l’oeil**\
*Passage à l’écran de mort correspondant -> x33 (auto)*

175. **Tu es à présent sur les nuages ! Que décides-tu de faire ?**\
*Se balader -> 180 (click)*\
***OU***\
*Toucher un nuage -> 181 (click)*

176. **Animation : perso dans une prison**\
*Passage à l’écran de mort correspondant -> x34 (auto)*

177. **Les policiers te demandent “Pourquoi ?” Que réponds-tu ?**\
*“Elle voulait ma lettre” -> 192 (click)*\
***OU***\
*“Elle était moche” -> 193 (click)*

178. **Un groupe de frites hostiles débarque et veut vous attaquer, que fais-tu ?**\
*Tu te sacrifie -> x37 (click)*\
***OU***\
*Tu sacrifie Cacahuète -> 212 (click)*

179. **Tu te rapproche de la statue en or, elle semble te demander un code**\
*Code bon -> 195*\
***OU***\
*Code erroné -> 178*

180. **Tu arrives devant le chat sur un nuage, il te propose un article contre 10$, que lui donnes-tu ?**\
*Rien (choix unique) -> 196 (click)*

181. **Animation : perso touche le nuage**\
*Passage à la scène suivante -> 187 (auto)*

182. **Animation : perso dans la rivière de mayo**\
*Passage à l’écran de mort correspondant -> x35 (auto)*

183. **Animation : blanc génant**\
*Passage à l’écran de mort correspondant -> x36 (auto)*

184. **Animation : Garde à vue toujours avec laser mais sans mec**\
*Passage à la scène suivante -> 188 (auto)*

185. **Animation : tire fesse**\
*Passage à la scène suivante -> 189 (auto)*

186. **Animation : télé siège**\
*Passage à la scène suivante -> 172 (auto)*

187. **Animation : aaaah angélique avec le billet**\
*Passage à la scène suivante -> 190 (auto)*

188. **Animation : Ciel avec laser mais sans mec**\
*Passage à la scène suivante -> 191 (auto)*

189. **Animation : piste vide le perso arrive en ski derrière lui père noël en ski**\
*Passage au mini jeux pere Noel -> expli_3 (auto)*

190. **Tu as récupéré 10$ ! Que fais-tu maintenant ?**
*Toucher encore le buisson -> 197 (click)*\
***OU***\
*Se balader -> 198 (click)*

191. **Animation : Ciel avec laser avec mec**\
*Passage à la scène suivante -> 175 (auto)*

192. **Les policiers te demandent maintenant où se trouve la lettre, que réponds-tu maintenant ?**\
*“Je l’ai mangé” -> 199 (click)*\
***OU***\
*Tu fais la sieste -> 200 (click)*

193. **Animation : Jo dit “pas cool mec” dans une bulle**\
*Passage à l’écran de mort correspondant -> x31 (auto)*

194. **Tu as maintenant le choix entre deux articles, lequel achètes-tu ?**\
*Le téléphone -> 214 (click)*\
***OU***\
*Le pistolet -> 202 (click)*

195. **Découverte du lore dans le temple (qui dcp explique notamment que le joueur ne doit pas écraser les patates pendant le snake)**\
*Passage à la scène suivante -> 178 (auto)*

196. **Animation : Blanc gênant entre le chat et le perso**\
*Passage à l’écran de mort correspondant -> x39 (auto)*

197. **Animation : Le roi charles sort de derrière le nuage**\
*Passage à la scène de mort correspondante -> x38 (auto)*

198. **Tu arrives devant le chat sur un nuage, il te propose un article contre 10\$, que lui donnes-tu ?**
*Rien -> 196 (click)*\
***OU***\
*Les 10$ -> 215 (click)*

199. **Animation : Tsvetelin frappe le perso dans le bide**\
*Passage à la scène suivante -> 203 (auto)*

200. **Animation : Le perso ferme les yeux**\
*Passage à la scène suivante -> 216 (auto)*

201. **Qui souhaites-tu appeler ?**\
*Le Roi Charles -> 205 (click)*\
***OU***\
*Le Sorcier -> 206 (click)*\
***OU***\
*Burger-man -> 207 (click)*\
***OU***\
*Le grand mère -> 207 (click)*\
***OU***\
*La patate carnivore -> 207 (click)*\
***OU***
*Clavier numérique -> 208 (click)*

202. **Animation : La patate débarque devant le perso**\
*Passage à la scène de mort correspondante -> x41 (auto)*

203. **Animation : On voit la lettre dans le vomi avec le numéro de la patate carnivore**\
*Passage à l’écran de mort correspondant (avec un fondu noir je pense que c’est un banger) -> x40 (auto)*

204. **Au réveil, le sorcier a tué tout le monde, il te demande où est la lettre, que lui réponds-tu ?**\
*“Je l’ai mangé” -> 209 (click)*\
***OU***\
*Tu lui tires la langue -> 210 (click)*

205. **Animation : le perso appelle (Roi Charles)**\
*Passage à la scène suivante -> 217 (auto)*

206. **Animation : le perso appelle (Sorcier)**\
*Passage à la scène suivante -> 218 (auto)*

207. **Animation : le perso appelle (les gens injoignables)**\
*Passage à la scène suivante -> 219 (auto)*

208. **Qui souhaites-tu appeler ? (le joueur doit rentrer le bon num)**\
*911 -> 220 (click)*\
***OU***\
*06 36 05 24 81 67 -> 221 (click)*\
***OU***\
*il appuie sur le bouton arrière  -> 201 (click)*\
***OU***\
*mauvais num-> 236 (click)*

209. **Animation : Le roi charles sort de derrière la table**\
*Passage à la scène de mort correspondante -> x43 (auto)*

210. **Animation : Le perso tire la langue, moment de blanc**\
*Passage à la scène de mort correspondante -> x44 (auto)*

211. **Animation : La patate carnivore débarque**\
*Passage à la scène de mort correspondante -> x46 (auto)*

212. **Animation : Le perso a la larme à l’oeil**\
*Passage à l’écran de mort correspondant -> x42 (auto)*

213. **Vous arrivez tous les deux devant une statue de patate en or magnifique. Que décides-tu de faire ?**\
*Regarder la statue de près -> 179 (click)*\
***OU***\
*Retourner dehors -> 178 (click)*

214. **Animation : le perso tient le téléphone dans sa main**\
*Passage à la scène suivante -> 201 (auto)*

215. **Animation : le perso tient les 10 euros dans sa main**\
*Passage à la scène suivante -> 194 (auto)*

216. **Animation : le perso à les yeux ouvert**\
*Passage à la scène suivante ->  204 (auto)*

217. **Animation : Le roi charles sort de derrière le nuage**\
*Passage à la scène de mort correspondante -> x45 (auto)*

218. **Animation : Le sorcier répond**\
*Passage à la scène suivante -> 238 (auto)*

219. **Animation : Le tel montre injoignable écrit dessus**\
*Passage à la scène suivante -> 211 (auto)*

220. **Animation : le perso appelle (Jo)**\
*Passage à la scène suivante -> 222 (auto)*

221. **Animation : le perso appelle (patate arc-en-ciel)**\
*Passage à la scène suivante -> 223 (auto)*

222. **Animation : Jo répond au tél et dit “Allo mec”**\
*Passage à la scène suivante -> 211 (auto)*

223. **Animation : La patate arc-en-ciel est émue**\
*Passage à la scène suivante -> 224 (auto)*

224. **Animation : La patate arc-en-ciel et la patate carnivore débarquent**\
*Passage à la scène suivante -> 225 (auto)*

225. **Animation : La patate arc-en-ciel dit à la patate carnivore qu’elle l’aime**\
*Passage à la scène suivante -> 226 (auto)*

226. **Victoire : La patate arc-en-ciel, la patate carnivore et le perso se font un câlin. Tout est bien qui finit bien.**\
*Passage à l’écran de victoire correspondant -> y5*

227. **Mini jeu fruit ninja**\
*Il gagne -> 235*\
***OU***\
*Il perd, passage à l’écran de mort correspondant -> x49*

228. **Animation : Le perso touche le buisson et le roi Charles sort et le lèche**\
*Passage à la scène suivante -> 229 (auto)*

229. **Animation : Le roi charles te lèche alors que le papillon est toujours là en vie (frame 1)**\
*Passage à la scène suivante -> 230 (auto)*

230. **Animation : Le roi charles te lèche alors que le papillon est toujours là en vie (frame 2)**\
*Passage à la scène suivante -> 231 (auto)*

231. **Animation : Le roi charles te lèche alors que le papillon est toujours là en vie (frame 3)**\
*Passage à la scène suivante -> 232 (auto)*

232. **Animation : Le roi charles te lèche alors que le papillon est toujours là en vie (frame 4)**\
*Passage à la scène suivante -> 233 (auto)*

233. **Animation : Le roi charles te lèche alors que le papillon est toujours là en vie (frame 5)**\
*Passage à la scène suivante -> 234 (auto)*

234. **Animation : Le roi charles te lèche alors que le papillon est toujours là en vie (frame 6)**\
*Passage à l’écran de mort correspondant -> x17 (auto)*

235. **Victoire : Tu as réussi à vaincre la patate carnivore en la transformant en frites**\
*Passage à l’écran de victoire correspondant -> y3*

236. **Animation : Mauvais numéro**\
*Passage à la scène suivante -> 208 (auto)*

237. **Animation : Zoom sur la tête du mec avant de combattre mamie**\
*Passage à la scène suivante -> 51 (auto)*

238. **Animation : Le sorcier débarque dans son petit outfit de cuistot/maid**\
*Passage à la scène suivante -> expli_1 (auto)*




110_mg. **Mini jeu : Blob party**\
*victoire -> 120*\
***OU***\
*échec, passage à l'écran de mort correspondant -> x48*

189_mg. **Mini jeu : Ski**\
*victoire -> 171*\
***OU***\
*échec, passage à l'écran de mort correspondant -> x48*

### Scènes explicatives pour les consignes des mini-jeux :

expli_1. **Déplace la souris pour couper les patates ! Ne sarcifie surtout pas Cacahuète.**\
*Début du mini-jeu -> 227*

expli_2. **Surveille la bulle de pensée. Clique quand Cacahuète pense à toi... mais ne te trompe pas !**\
*Début du mini-jeu -> 168*

expli_3. **Aide le père Noël à descendre la piste. Esquive les patates en te déplaçant avec les flèches !**\
*Début du mini-jeu -> 189_mg*

expli_4. **Utilise la souris pour écraser les patates spatiales. Protège le Blob et ne les laisse pas passer !**\
*Début du mini-jeu -> 110_mg*

expli_5. **Clique vite pour battre mamie ! Ne la laisse pas gagner !**\
*Début du mini-jeu -> 51*

### Scènes de mort :


x1 . **Tu te lèves pour aller fermer la fenêtre mais tu meurs, tué par une patate carnivore**

x2. **Tu est mort brûlé par des fourmies enflammées qui sortent à la place de l’eau**

x3. **Tu as mangé le miroir, tu meurt d’une indigestion**

x4. **Tu es mort tué par la patate carnivore**

x5. **La patate carnivore débarque, brise la télé en deux et te tue**

x6. **Tu décides de ne pas prendre la lettre, la patate carnivore débarque et te tue.**

x7. **Le Roi Charles troisième du nom sort de sous la table et te lèche. Tu es mort léché par le Roi Charles**

x8. **Le chat attend toujours que tu le payes…**\
**Le chat te regarde.**\
**Longtemps.\
Très longtemps.\
Il note quelque chose dans un carnet.\
Où est l’argent ?\
La dette grandit.\
Il te pousse.\
La chute est … définitive.**


x9. **Tu as perdu le combat contre la grand-mère, elle t’as mis KO**

x10. **Tu te rends compte trop tard que le gazon était mouillé, tu es tombé**

x11. **Tu as essayé de gagner trop rapidement, la patate carnivore explose la fenêtre et te tue**


x12. **Tu essayes de rentrer chez toi mais la patate carnivore surgit et te tue.**

x13. **Tu t’es pris une barrière, tu meurs sur le coup.** 

x14. **Tu as écrasé 3 patates dommage, la patate carnivore est venue venger ses protégés.**

x15. **Les taupes ne t’ont pas très bien accueilli, tu meurs tué par les taupes.**

x16. **Tu es mort piétiné par Burger Man.**

x17. **Le Roi Charles troisième du nom sort du buisson et te lèche. Tu es mort léché par le Roi Charles**

x18. **Un accident de la route ça ne pardonne pas…**\
**Vous vous êtes percutés avec la police, ça t’a tué**

x19. **Tu as littéralement foncé sur une voiture en mouvement
Elle t’as écrasé, tu es mort**

x20. **Tu es mort tué par la patate carnivore**

x21. **Tu es mort tué par zgublux3000 ;) :p**

x22. **Les fourmies enflammées t’ont brûlé**

x23. **Tu es mort, tué par les taupes**

x24. **Tu es mort tué par la patate carnivore**

x25. **Le policier Tsvetelin Mitov Roham Bosphoramus Sylvanus t’a tiré dessus, tu es mort**

x26. **Tu es mort, kidnappé dans l’espace par le policier zgublux3000 ;) :p**

x27. **Le sorcier a fait exploser la voiture de police, tu meurt instantanément**

x28. **Tu es mort après avoir littéralement avalé des cailloux, ça t’arrive de réfléchir des fois ?**

x29. **Le chocolat chaud était… un peu chaud…**

x30. **Après l’affront que tu venais de lui faire, le burger n’a pas eu le choix et a décidé de te manger**

x31. **Le policier Tsvetelin Mitov Roham Bosphoramus Sylvanus t’a tiré dessus, tu es mort**

x32. **Tu es mort, tué par l’ours polaire**

x33. **Le date a été un échec, tu meurs après avoir avoir eu le coeur brisé**

x34. **Tu as été condamné à la prison à vie, tu meurs en cellule**

x35. **Tu es mort, littéralement noyé dans la mayonnaise**

x36. **Tu es mort, tué par les frites carnivores**

x37. **Tu es mort, tué par les frites carnivores**

x38. **Tu es mort, léché par le Roi Charles troisième du nom**

x39.
**Le chat te regarde.\
Tu refuses de payer.\
Il soupire, presque déçu.\
Puis, d’un geste sec, il te pousse.\
Après tout, pourquoi investir sans retour ?\
La gravité, elle, travaille gratuitement.**


x40. **Tu es mort, à cause du coup très puissant de Tsvetelin Mitov Roham Bosphoramus Sylvanus t’a mit dans le ventre**

x41. **Le pistolet n’a servi à rien du tout, la patate carnivore n’a fait qu’une bouchée de toi**

x42. **Cacahuète a été sacrifié, tu es sorti vivant de cet affrontement, mais à quel prix ?**

x43. **Tu es mort, léché par le Roi Charles troisième du nom** 

x44. **Le sorcier t’a littéralement explosé**

x45. **Tu es mort, léché par le Roi Charles troisième du nom**

x46. **Tu es mort tué par la patate carnivore**

x47. **Tu n’as pas réussi à protéger blob, tu es mort tué par des patates spatiales.**

x48. **La magie est morte avec le Père Noël, tu deviens l’orphelin du froid…**

x49. **Tu as tué cacahuète, tu n’as pas honte !**

### Scènes de victoires :

y1. **Tu as suivi le blob interdimensionnel et tu te retrouves dans sa super fête avec ses super potes, c’est la régalade**

y2. **Le papillon t’as défendu et tu as réussi à toucher le trophée légendaire de la légende qui t’offre la victoire**

y3. **Le tuto cuisine du sorcier a porté ses fruits, tu as vaincu ton ennemi juré et en plus tu gagnes un plat de frites**

y4. **Tu rencontres le père Noël, vous faites du ski ensemble en pure légende**

y5. **Tu as réglé le plus grand des conflits\
Et en plus tu es devenu ami avec ta pire ennemie\
C’est à ma connaissance la meilleure fin possible**



