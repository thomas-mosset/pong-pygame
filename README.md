# Pong

Le projet reprend le concept du jeu **Pong**. Le ou la joueuse peut choisir de jouer seul·e contre une autre personne sur la même machine, ou bien contre l’ordinateur (IA). La partie se termine lorsqu’un·e des 2 a atteint le score de 5 points.

## Technologies utilisées

- Pygame
- Watchdog
- PyAudio (branche ``voice-recognition``)
- SpeechRecognition (branche ``voice-recognition``)

## Fonctionnalités

- Déplacer verticalement son joueur ;
- Jouer à « 1 vs 1 » (sur la même machine) ou « 1 vs Ordinateur » ;
- Choisir niveau de difficulté (``facile``, ``moyen``, ``difficile``) lorsqu’on joue contre l’ordinateur ;
- Rejouer une partie ;
- Menus (principal, choix de difficulté, pause, rejouer)

## Comment jouer

- Le ou la joueuse 1 (à gauche de l’écran) peut utiliser respectivement les touches ``Z`` et ``S`` pour aller vers le haut ou vers le bas ;

- Le ou la joueuse 2 (à droite de l’écran) peut utiliser respectivement les touches ``flèche du haut`` et ``flèche du bas`` pour aller vers le haut ou vers le bas ;

*Note : En plus des touches clavier, le ou la joueuse 1 peut utiliser des instructions vocales (``« monter »`` pour aller vers le haut, ``« descendre »`` pour aller vers le bas) pour diriger son pion lorsque le jeu est en mode « 1 vs Ordinateur ». ⚠️ Fonctionnalité uniquement visible via la branche ``voice-recognition`` car buguée (lag entre la commande dictée et l'action en jeu + commande vocale souvent non comprise surtout lorsqu'il y a du bruit).*

## Ressources utilisées

- Image : [Freepik](https://www.freepik.com/)
- Sons : [Soundsnap](https://www.soundsnap.com/)
- Font : [Rocket-Command](https://www.fontspace.com/rocket-command-font-f143316)

## Démo

[![Démo du jeu (v2)](https://markdown-videos-api.jorgenkh.no/youtube/VdSLbLxRyE8)](https://youtu.be/VdSLbLxRyE8)

## Lancer le jeu

Cloner le repo, puis lancer les commandes suivantes :

```sh
pip install pygame
```

*Si utilisation de la branche ``voice-recognition`` :*

```sh
pip install SpeechRecognition
pip install PyAudio
```

*Si ``PyAudio`` bloque sur Windows, utiliser :*

```sh
pip install pipwin
pipwin install pyaudio
```

Puis, pour lancer le jeu :

```sh
python src/main.py
```

Si utilisation de Watchdog (permet de surveiller les changements dans le fichier pour refresh le jeu automatiquement) :

```sh
pip install watchdog
watchmedo auto-restart --patterns="*.py" --recursive --directory=src -- python src/main.py
```
