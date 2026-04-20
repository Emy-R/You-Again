import pygame
import json
import os
import random
from affichageText import play_story, play_lore
from CodeInput import CodeInput

class Confetti :
    def __init__(self, sw, sh):
        self.sw, self.sh = sw, sh
        self.x = random.randint(0, sw)
        self.y = random.randint(-sh, 0)
        self.size = random.randint(8,15)
        self.color = random.choice([(255,50,50),(50,255,50),(80,80,255),(255,255,100),(255,100,255)])
        self.speed = random.uniform(3, 7)
        self.angle = random.uniform(0, 360)

    def update(self ):
        self.y += self.speed
        self.angle += 10
        if self.y > self.sh :
            self.y = -20
            self.x = random.randint(0, self.sw)

    def draw(self, screen):
        s = pygame.Surface((self.size, self.size), pygame.SRCALPHA)
        s.fill(self.color)
        rotated_s = pygame.transform.rotate(s, self.angle)
        screen.blit(rotated_s, (self.x, self.y))

class SceneManager:
    def __init__(self, screen, minigames):
        self.screen = screen
        self.minigames = minigames
        self.current_scene_name = None
        self.current_scene = None
        self.data={}
        # Variables utiles pour les animations :
        self.animated_objects = []
        self.anim_start_time = None
        self.anim_duration = None
        self.anim_target = None
        # Variables pour les fondus
        self.fade_surface = pygame.Surface(self.screen.get_size())
        self.fade_surface.fill((0, 0, 0))  # Un rectangle noir de la taille de l'écran
        self.fade_type = None
        #code
        self.code_handler = CodeInput()  # On crée l'outil ici
        self.input_text = ""

        self.sound_events = []

        self.secret_code = ""

        #confettis
        self.confettis = []

        pygame.mixer.init()
        self.hover_sound = pygame.mixer.Sound("son/test.wav")
        self.hover_sound.set_volume(0.4)

        with open("scenes/mort.json") as m:
            self.mort_texts=json.load(m)

        with open ('scenes/victoire.json', 'r') as f:
            self.victoire_texts=json.load(f)

        with open ('scenes/lore.json') as l:
            self.lore_textes=json.load(l)

    def load_scene(self, scene_name):
        # si c'est une scène de mort
        if scene_name.startswith("mort_"):
            texts = self.mort_texts.get(scene_name)
            play_story(self.screen, "images/mort.png", texts)
            scene_name = "menu"  # on redirige juste vers le menu

        if scene_name.startswith("victoire_"):
            texts=self.victoire_texts.get(scene_name)
            play_story(self.screen, "images/victoire.png", texts,(0,0,0))
            scene_name = "menu"
        bg_lore = "images/i195.png"
        if scene_name.startswith("lore"):
            texts=self.lore_textes.get(scene_name)
            play_lore(self.screen, bg_lore, texts)
            self.load_scene("scene178")
            return

        # Décharger ancienne scène
        self.current_scene = None

        # Stopper tous les sons en cours
        for sound in self.sound_events:
            sound.stop()

        # Charger fichier JSON
        with open(f"scenes/{scene_name}.json", "r") as f:
            data = json.load(f)
            self.data=data

        # lancement mini-jeux auto après animation
        mg_name = self.data.get("minigame")

        if mg_name and mg_name in self.minigames:

            result = self.minigames[mg_name](
                self.screen,
                *self.screen.get_size(),
                pygame.time.Clock()
            )

            if result == "win":
                next_scene = self.data.get("win_target")

            elif result == "lose_wall":
                next_scene = self.data.get("lose_wall_target")

            else:
                next_scene = self.data.get("target")

            if next_scene:
                self.load_scene(next_scene)

            return

        # Code_secret
        if self.data.get("generate_code"):
            import random
            self.secret_code = "".join([str(random.randint(0,9)) for _ in range(5)])
            print(self.secret_code)

        #le fondu
        self.fade_type = data.get("fade", None)
        # Charger image
        image = pygame.image.load(f"images/{data['image']}").convert_alpha()
        sw, sh = self.screen.get_size()
        image = pygame.transform.smoothscale(image, (sw, sh))

        # Créer zones (coordonnées en pourcentage)
        zones = []
        for z in data["zones"]:
            rect = pygame.Rect(
                int(z["x"] * sw),
                int(z["y"] * sh),
                int(z["width"] * sw),
                int(z["height"] * sh)
            )
            zone_data = z.copy()

            zone_data["rect"] = rect
            zone_data["hovered"] = False

            zones.append(zone_data)

        self.current_scene = {
            "image": image,
            "zones": zones
        }

        self.current_scene_name = scene_name
        self.start_time = pygame.time.get_ticks()

        # Ajout des confettis
        self.confettis = []

        scenes_victoire = ["scene120", "scene129", "scene171", "scene226", "scene235"]

        if scene_name.startswith("victoire") or scene_name in scenes_victoire :
            sw, sh = self.screen.get_size()
            self.confettis = [Confetti(sw, sh) for _ in range(100)]

        # --- Animation ---
        self.animated_objects = []

        if "animation" in data:
            from animated_object import AnimatedObject

            anim = data["animation"]

            self.anim_start_time = pygame.time.get_ticks()
            self.anim_duration = anim.get("duration")
            self.anim_target = anim.get("complete_target")

            for obj in anim.get("objects", []):
                animated_obj = AnimatedObject(
                    obj["image"],
                    obj["movement"],
                    self.anim_duration,
                    obj.get("scale", 1.0)
                )
                self.animated_objects.append(animated_obj)
        else:
            self.anim_start_time = None
            self.anim_duration = None
            self.anim_target = None

        # --- Bruitage ---
        self.sound_events = []

        self.code_handler.text = ""

        if "sounds" in data:
            from sound_event import SoundEvent

            for s in data["sounds"]:
                sound = SoundEvent(
                    file=s["file"],
                    trigger=s.get("trigger", "start"),
                    start_time=pygame.time.get_ticks(),
                    volume=s.get("volume", 1.0),
                    delay=s.get("delay", 0),
                    loop=s.get("loop", False)
                )
                self.sound_events.append(sound)

    def draw(self, debug=False):
        self.screen.blit(self.current_scene["image"], (0, 0))

        mouse_pos = pygame.mouse.get_pos()

        # Variable pour savoir si on survole AU MOINS une zone
        au_dessus_d_une_zone = False
        for zone in self.current_scene["zones"]:
            if zone["rect"].collidepoint(mouse_pos):
                au_dessus_d_une_zone = True
                if not zone.get("hovered", False):
                    self.hover_sound.play()
                    zone["hovered"] = True
            else:
                zone["hovered"] = False
        # CHANGER LE CURSEUR
        if au_dessus_d_une_zone:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_HAND)  # La main
        else:
            pygame.mouse.set_cursor(pygame.SYSTEM_CURSOR_ARROW)  # La flèche
        # Affichage du code et debug
        if debug:
            for zone in self.current_scene["zones"]:
                pygame.draw.rect(self.screen, (255, 0, 0), zone["rect"], 3)

        for obj in self.animated_objects:
            obj.draw(self.screen)

        #Ajout pour le code secret et la télé qui bug
        if self.data.get("generate_code") and self.secret_code:
            sw, sh = self.screen.get_size()

            tv_x = int(0.373 * sw)
            tv_y = int( 0.054 * sh)
            tv_w = int(0.358 * sw)
            tv_h = int(0.386 * sh)

            tv_rect = pygame.Rect(tv_x,tv_y,tv_w, tv_h)

            pos_x = tv_rect.centerx
            pos_y = tv_rect.centery

            if not hasattr(self, 'tv_timer'):
                self.tv_timer = pygame.time.get_ticks()

            temps_total = pygame.time.get_ticks() - self.tv_timer

            pygame.draw.rect(self.screen, (20, 20, 20), tv_rect)

            if 1000 < temps_total < 3000 :
                font_tele = pygame.font.Font("Kindergarden.ttf", 160)
                txt_surface = font_tele.render(self.secret_code, True, (255, 250, 255))
                txt_rect = txt_surface.get_rect(center = (pos_x, pos_y))
                self.screen.blit(txt_surface, txt_rect)

                if random.random() < 0.8:
                    rx = random.randint(tv_rect.left, tv_rect.right)
                    ry = random.randint(tv_rect.top, tv_rect.bottom)
                    pygame.draw.rect(self.screen, (200, 200, 200), (rx, ry,2,2))

            else :
                intensite = 600
                for _ in range(intensite):
                    c = random.randint(150, 255)
                    rx = random.randint(tv_rect.left, tv_rect.right)
                    ry = random.randint(tv_rect.top, tv_rect.bottom)
                    pygame.draw.rect(self.screen, (c, c, c), (rx, ry,2,2))

                if random.random() < 0.3:
                    h_y = random.randint(tv_rect.top, tv_rect.bottom)
                    h_h = random.randint(1,4)
                    pygame.draw.rect(self.screen, (255, 255, 255), (tv_rect.left, h_y, tv_rect.width, h_h))


                if random.random() < 0.05 :
                    flash = pygame.Surface((tv_rect.width,tv_rect.height))
                    flash.set_alpha(40)
                    flash.fill((200,200,255))
                    self.screen.blit(flash, tv_rect.topleft)

        else:
            if hasattr(self, 'tv_timer'):
                del self.tv_timer

        # Confettis
        for c in self.confettis :
            c.draw(self.screen)

        mouse_pos = pygame.mouse.get_pos()
        # fondu
        if self.fade_type and self.anim_duration:
            elapsed = pygame.time.get_ticks() - self.anim_start_time
            progress = min(1.0, elapsed / self.anim_duration)  # 0.0 à 1.0

            if self.fade_type == "out":
                alpha = int(progress * 255)  # Devient noir
            elif self.fade_type == "in":
                alpha = int((1 - progress) * 255)  # Devient clair
            else:
                alpha = 0

            self.fade_surface.set_alpha(alpha)
            self.screen.blit(self.fade_surface, (0, 0))

        for zone in self.current_scene["zones"]:
            if zone["rect"].collidepoint(mouse_pos):
                if not zone["hovered"]:
                    self.hover_sound.play()
                    zone["hovered"] = True
            else:
                zone["hovered"] = False
        if debug:
            for zone in self.current_scene["zones"]:
                pygame.draw.rect(self.screen, (255, 0, 0), zone["rect"], 3)

        #Affichage du code
        if self.data.get("codes"):
            # On affiche le texte de l'outil
            self.code_handler.draw(self.screen, self.data)

    def handle_click(self, pos):
        target = self.data.get("skippable")
        now = pygame.time.get_ticks()
        if target and (now - self.start_time > self.data.get("skip_delay",350)):
            return self.load_scene(target)

        for zone in self.current_scene["zones"]:
            if zone["rect"].collidepoint(pos):


                mg_name = zone.get("minigame")


                if mg_name and mg_name in self.minigames:
                    result = self.minigames[mg_name](
                        self.screen,
                        *self.screen.get_size(),
                        pygame.time.Clock()
                    )
                else:
                    result = "lose"

                if result == "win":
                    next_scene = zone.get("win_target")
                elif result == "lose_wall":
                    next_scene = zone.get("lose_wall_target")
                else:
                    next_scene = zone.get("target")

                if next_scene:
                    self.load_scene(next_scene)

                return

    # verification du code
    def check_keyboard(self, event):
        if self.data.get("codes"):
            # On passe l'event, le dictionnaire data, et le code secret
            prochaine = self.code_handler.update(event, self.data, self.secret_code)

            if prochaine:
                self.load_scene(prochaine)
    def update(self):
        current_time = pygame.time.get_ticks()

        # Ajout pour la télé qui bug
        if self.data.get("generate_code") and hasattr(self,'tv_timer'):
            delta = current_time - self.tv_timer
            if delta > 5000 :
                prochaine = self.data.get("animation", {}).get("complete_target")
                if prochaine:
                    self.load_scene(prochaine)
                    return

        # Ajout pour les confettis
        for c in self.confettis :
            c.update()

        for obj in self.animated_objects:
            obj.update(current_time)

        for sound in self.sound_events:
            sound.update(current_time)

        if self.anim_duration is not None:
            elapsed = current_time - self.anim_start_time
            if elapsed >= self.anim_duration:
                if self.anim_target:
                   self.load_scene(self.anim_target)
