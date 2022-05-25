from PIL import Image
from tqdm import tqdm
import json
import random

def nft_generator_equally():

  flavors = ['gentlepurple', 'mint','pink','purple','yellow']
  eyes = ['curious','cute','focused','sleepy','usual']
  mouths =['shh','shocked','smiling','surprised','usual']
  accs = ['blush','bubble','dot','earing','glasses','hat','none','ribbon']

  # for test
  # flavors = flavors[:2]
  # eyes = eyes[:2]
  # mouths = mouths[:2]
  # accs = accs[:2]

  count = 0
  for flavor in tqdm(flavors):
    for eye in eyes:
      for mouth in mouths:
        for acc in accs:

          count +=1
          flavor_img = Image.open(f"../flavor/{flavor}.png")
          eye_img = Image.open(f"../eye/{eye}.png")
          mouth_img = Image.open(f"../mouth/{mouth}.png")
          acc_img = Image.open(f"../acc/{acc}.png")

          flavor_img.paste(eye_img, (0, 0), eye_img)
          flavor_img.paste(mouth_img, (0, 0), mouth_img)
          flavor_img.paste(acc_img, (0, 0), acc_img)


          # 이미지 저장
          number = ('000' + str(count))[-4:]
          url = f"gominjelly_{number}.png"
          flavor_img.save(f"nft/{url}", "PNG")

          # json 저장
          params = {
            'flavor':flavor,
            'eye':eye,
            'mouth':mouth,
            'acc':acc
          }

          create_json(params,number)


# 랜덤하게 추출쓰 ~ 몇개 추출할건지 total_number에 입력하삼
def nft_generator_random(total_number):

  flavors = ['apple', 'blueberry','cherry','grape','orange']
  eyes = ['curious','cute','focused','sleepy','usual']
  mouths =['shh','shocked','smiling','surprised','usual']
  accs = ['blush','bubble','dot','earing','glasses','hat','none','ribbon']


  count = 0
  while count < total_number:

    count +=1
    flavor = random.choice(flavors)
    eye = random.choice(eyes)
    mouth = random.choice(mouths)
    acc = random.choice(accs)

    flavor_img = Image.open(f"../flavor/{flavor}.png")
    eye_img = Image.open(f"../eye/{eye}.png")
    mouth_img = Image.open(f"../mouth/{mouth}.png")
    acc_img = Image.open(f"../acc/{acc}.png")

    flavor_img.paste(eye_img, (0, 0), eye_img)
    flavor_img.paste(mouth_img, (0, 0), mouth_img)
    flavor_img.paste(acc_img, (0, 0), acc_img)


    # 이미지 저장
    number = ('000' + str(count))[-4:]
    url = f"gominjelly_{number}.png"
    flavor_img.save(f"nft/{url}", "PNG")

    # json 저장
    params = {
      'flavor':flavor,
      'eye':eye,
      'mouth':mouth,
      'acc':acc
    }

    create_json(params,number)



def create_json(params, number):

  content = {
    "image": f"https://gominjelly.s3.ap-northeast-2.amazonaws.com/nft/gominjelly_{number}.png",
    "description": "Hi there. I am GOMINJELLY. I worry about people especially you. If there is a problem you cannoy talk to anybody, I am here for you!  ",
    "name": f"GOMINJELLY #{number}",
    "attributes": [
      {
        "trait_type": "flavor",
        "value": f"{params['flavor']}"
      },{
        "trait_type": "eye",
        "value": f"{params['eye']}"
      },{
        "trait_type": "mouth",
        "value": f"{params['mouth']}"
      },{
        "trait_type": "acc",
        "value": f"{params['acc']}"
      }
    ]
  }



  json_object=json.dumps(content,indent=4)


  with open(f'json/meta_{number}.json', "w") as outfile:
    outfile.write(json_object)
    outfile.close()

nft_generator_random(1000)
