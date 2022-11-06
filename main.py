from PIL import Image, ImageDraw
import random
from tqdm import tqdm

from char_ import char_

# movie settings
FRAMES = 1200
SPAWN_PER_FRAME = 1
SPEED = 20

# frame settings
WIDTH = 1920
HEIGHT = 1060
CHAR_WIDTH = 25
CHAR_PADDING = 1

CHAR_COLOR = (0, 200, 0)
BACKGROUND_COLOR = (0,0,0)

def main():
    # struct
    rand_char = lambda: chr(random.randrange(33, 126))
    columns = [i for i in range(0, WIDTH, CHAR_WIDTH + CHAR_PADDING)]
    all_chars = list()
    new_chars = list()
    
    
    for n in tqdm(range(0, FRAMES), desc='Generating frames'):
        # for each frame
        bckg = Image.new('RGBA', (WIDTH, HEIGHT), color = BACKGROUND_COLOR)
        
        characters = Image.new('RGBA', (WIDTH, HEIGHT), color = (0,0,0,0))
        draw = ImageDraw.Draw(characters)
        
        
        # spawn chars
        for _ in range(0, SPAWN_PER_FRAME):
            new_chars.append(char_(rand_char(), 255, random.randint(0, len(columns) - 1), 0))
        
        # update new chars
        for char in new_chars:
            new_chars.append(char_(rand_char(),
                               255,
                               char.x,
                               char.y + SPEED))
            new_chars.remove(char)

        # update char's opacity
        for char in all_chars:
            char.opacity -= 5
            
            if(char.y > HEIGHT or char.opacity < 0):
                del char
                
        # append chars
        all_chars += new_chars
        
        # render chars
        for char in all_chars:
            draw.text((columns[char.x], char.y), char.char, (*CHAR_COLOR, char.opacity))
            
        Image.alpha_composite(bckg, characters).save(f'./imgs/{n}.png')
        del bckg, characters
    
if __name__=="__main__":
    main()