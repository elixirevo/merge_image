from PIL import Image
import os
import random
import json
import numpy as np
from metadata_enum import background_rarity, skin_rarity, tatto_rarity, hat_rarity, eyes_rarity, clothes_rarity, mouth_rarity, back_rarity, weapon_rarity

def mergeImage():
    background_list = os.listdir("./MYBOX/Background/")
    body_list = os.listdir("./MYBOX/Skin_color/")
    eye_list = os.listdir("./MYBOX/Eyes/")
    clothes_list = os.listdir("./MYBOX/Clothes/")
    hat_list = os.listdir("./MYBOX/Hat/")
    mouth_list = os.listdir("./MYBOX/Mouth/")
    tatto_list = os.listdir("./MYBOX/Tattoo/")
    back_list = os.listdir("./MYBOX/Back/")
    weapon_list = os.listdir("./MYBOX/Weapon/")

    available_background_rarity = background_rarity
    available_skin_rarity = skin_rarity
    available_tatto_rarity = tatto_rarity
    available_hat_rarity = hat_rarity
    available_eyes_rarity = eyes_rarity
    available_clothes_rarity = clothes_rarity
    available_mouth_rarity = mouth_rarity
    available_back_rarity = back_rarity
    available_weapon_rarity = weapon_rarity

    for i in range(0, 9928):
        count_background = np.sum(list(available_background_rarity.values()))
        count_skin = np.sum(list(available_skin_rarity.values()))
        count_tatto = np.sum(list(available_tatto_rarity.values()))
        count_hat = np.sum(list(available_hat_rarity.values()))
        count_eyes = np.sum(list(available_eyes_rarity.values()))
        count_clothes = np.sum(list(available_clothes_rarity.values()))
        count_mouth = np.sum(list(available_mouth_rarity.values()))
        count_back = np.sum(list(available_back_rarity.values()))
        count_weapon = np.sum(list(available_weapon_rarity.values()))

        all_count = count_background + count_skin + count_tatto + count_hat + count_eyes + count_clothes + count_mouth + count_back + count_weapon

        if all_count == 0:
            print("Make image is done")
            return
        else:
            choiced_background = random.choice(background_list)
            choiced_body = random.choice(body_list)
            choiced_eye = random.choice(eye_list)
            choiced_clothe = random.choice(clothes_list)
            choiced_hat = random.choice(hat_list)
            choiced_mouth = random.choice(mouth_list)
            choiced_tatto = random.choice(tatto_list)
            choiced_back = random.choice(back_list)
            choiced_weapon = random.choice(weapon_list)

            slice_background_name = choiced_background[0:-4]
            slice_body_name = choiced_body[0:-4]
            slice_eye_name = choiced_eye[0:-4]
            slice_clothe_name = choiced_clothe[0:-4]
            slice_hat_name = choiced_hat[0:-4]
            slice_mouth_name = choiced_mouth[0:-4]
            slice_tatto_name = choiced_tatto[0:-4]
            slice_back_name = choiced_back[0:-4]
            slice_weapon_name = choiced_weapon[0:-4]

            while(background_rarity[f"{slice_background_name}"] == 0):
                choiced_background = random.choice(background_list)
                slice_background_name = choiced_background[0:-4]
            
            while(skin_rarity[f"{slice_body_name}"] == 0):
                choiced_body = random.choice(body_list)
                slice_body_name = choiced_body[0:-4]

            while(eyes_rarity[f"{slice_eye_name}"] == 0):
                choiced_eye = random.choice(eye_list)
                slice_eye_name = choiced_eye[0:-4]

            while(clothes_rarity[f"{slice_clothe_name}"] == 0):
                choiced_clothe = random.choice(clothes_list)
                slice_clothe_name = choiced_clothe[0:-4]  

            while(hat_rarity[f"{slice_hat_name}"] == 0):
                choiced_hat = random.choice(hat_list)
                slice_hat_name = choiced_hat[0:-4]

            while(mouth_rarity[f"{slice_mouth_name}"] == 0):
                choiced_mouth = random.choice(mouth_list)
                slice_mouth_name = choiced_mouth[0:-4]

            while(tatto_rarity[f"{slice_tatto_name}"] == 0):
                choiced_tatto = random.choice(tatto_list)
                slice_tatto_name = choiced_tatto[0:-4]

            while(back_rarity[f"{slice_back_name}"] == 0):
                choiced_back = random.choice(back_list)
                slice_back_name = choiced_back[0:-4]

            while(weapon_rarity[f"{slice_weapon_name}"] == 0):
                choiced_weapon = random.choice(weapon_list)
                slice_weapon_name = choiced_weapon[0:-4]

            metadata = {}
            metadata['metadata'] = []
            metadata['metadata'].append({
                'image': f"test{i}.png",
                'background': slice_background_name,
                'body': slice_body_name,
                'eye': slice_eye_name,
                'clothe': slice_clothe_name,
                'hat': slice_hat_name,
                'mouth': slice_mouth_name,
                'tatto': slice_tatto_name,
                'back': slice_back_name,
                'weapon': slice_weapon_name,
            })

            background = Image.open(f"./MYBOX/Background/{slice_background_name}.png").convert("RGBA")
            body = Image.open(f"./MYBOX/Skin_color/{slice_body_name}.png").convert("RGBA")
            eye = Image.open(f"./MYBOX/Eyes/{slice_eye_name}.png").convert("RGBA")
            clothes = Image.open(f"./MYBOX/Clothes/{slice_clothe_name}.png").convert("RGBA")
            hat = Image.open(f"./MYBOX/Hat/{slice_hat_name}.png").convert("RGBA")
            mouth = Image.open(f"./MYBOX/Mouth/{slice_mouth_name}.png").convert("RGBA")
            tatto = Image.open(f"./MYBOX/Tattoo/{slice_tatto_name}.png").convert("RGBA")
            back = Image.open(f"./MYBOX/Back/{slice_back_name}.png").convert("RGBA")
            weapon = Image.open(f"./MYBOX/Weapon/{slice_weapon_name}.png").convert("RGBA")

            save_image_path = "./images"
            save_metadata_path = "./metaData"

            if not os.path.isdir(save_image_path):
                os.mkdir(save_image_path)
            if not os.path.isdir(save_metadata_path):
                os.mkdir(save_metadata_path)
            
            (heigh, width) = background.size

            background.paste(body, (0,0), body)
            background.paste(eye, (0,0), eye)
            background.paste(clothes, (0,0), clothes)
            background.paste(hat, (0,0), hat)
            background.paste(mouth, (0,0), mouth)
            background.paste(tatto, (0,0), tatto)
            background.paste(back, (0,0), back)
            background.paste(weapon, (0,0), weapon)

            background.save(f"./images/test{i}.png", "PNG")
            with open(f"{save_metadata_path}/metadata{i}.json", "w") as outfile:
                json.dump(metadata, outfile)

            available_background_rarity[f"{slice_background_name}"] -= 1
            available_skin_rarity[f"{slice_body_name}"] -= 1
            available_tatto_rarity[f"{slice_tatto_name}"] -= 1
            available_hat_rarity[f"{slice_hat_name}"] -= 1
            available_eyes_rarity[f"{slice_eye_name}"] -= 1
            available_clothes_rarity[f"{slice_clothe_name}"] -= 1
            available_mouth_rarity[f"{slice_mouth_name}"] -= 1
            available_back_rarity[f"{slice_back_name}"] -= 1
            available_weapon_rarity[f"{slice_weapon_name}"] -= 1


mergeImage()