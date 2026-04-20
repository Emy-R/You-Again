import pygame


class CodeInput:
    def __init__(self):
        self.text = ""
        try:
            # On charge ta police Kindergarden
            self.font = pygame.font.Font("Kindergarden.ttf", 40)
        except:
            self.font = pygame.font.SysFont("Arial", 40, bold=True)

    def update(self, event, scene_data, secret_code_memoire=None):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                codes_fixes = scene_data.get("codes", {})
                target = None

                # 1. Test du code secret généré (prioritaire)
                if secret_code_memoire and self.text == secret_code_memoire:
                    if codes_fixes:
                        target = list(codes_fixes.values())[0]

                # 2. Test des codes fixes (ex: "911")
                elif self.text in codes_fixes:
                    target = codes_fixes[self.text]

                # 3. Si faux, on prend la scène d'erreur définie dans le JSON
                else:
                    target = scene_data.get("on_error")

                self.text = ""
                return target

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
            elif event.unicode.isprintable():
                self.text += event.unicode
        return None

    def draw(self, screen, scene_data):
        if self.text == "":
            return

        # Récupération position et couleur depuis le JSON
        pos = scene_data.get("input_pos", {"x": 0.5, "y": 0.5})
        color = scene_data.get("text_color", [255, 255, 255])

        sw, sh = screen.get_size()
        x, y = int(pos["x"] * sw), int(pos["y"] * sh)

        img = self.font.render(self.text, True, color)
        rect = img.get_rect(center=(x, y))
        screen.blit(img, rect)
