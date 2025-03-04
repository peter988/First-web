import random 
import numpy as np 
import pandas as pd
import openpyxl
import os
import re

df = pd.read_excel('FIRST CATALOGUE NEW.xlsx')
ds = df[df.columns[4]].tolist() 
codes = df[df.columns[1]].tolist()
codes = codes[:127]
ds = ds[:127]
titles = []
desc = []
for idx,code in enumerate(codes):
    titles.append(str(code) + ' ' + ds[idx])
    if  str(df[df.columns[2]].tolist()[idx]) != 'nan':
        if str(df[df.columns[5]].tolist()[idx]) != 'nan':
            desc.append(str(code) + ' ' + ds[idx] + '<br>' + str(df[df.columns[2]].tolist()[idx]) + '<br>' +  str(df[df.columns[5]].tolist()[idx]))
        else:
            desc.append(str(code) + ' ' + ds[idx] + '<br>' + str(df[df.columns[2]].tolist()[idx]))
    else:
        if str(df[df.columns[5]].tolist()[idx]) != 'nan':
            desc.append(str(code) + ' ' + ds[idx] + '<br>' + str(df[df.columns[5]].tolist()[idx]))
        else:
            desc.append(str(code) + ' ' + ds[idx])
prices = df[df.columns[6]].tolist()

initial_template = '''<div class="product-card" data-name="Truck Engine">
            <img src="https://via.placeholder.com/200" alt="Truck Engine">
            <div class="product-name">Truck Engine</div>
            <div class="product-price">$2,500</div>
        </div>'''
image_directory = 'filters/'

def find_image_for_code(code):
    # Clean the code for matching
    clean_code = code.replace(' ', '').lower()
    
    # List all files in the image directory
    image_files = os.listdir(image_directory)
    
    # Try to find a match using different patterns
    for image_file in image_files:
        if re.search(r'{}.*\.jpg'.format(re.escape(clean_code)), image_file.lower()):
            return os.path.join(image_directory, image_file)  # Return the full path to the image
    if code == 'FK13850NN':
        return 'filters/13850nn.jpg'
    return ''  # Default placeholder if no match is found

def make_text(photo_source, title, description, price,extra):
    perc = random.choice(range(5, 66, 5))  # Generate a random percentage (multiple of 5)
    price = round(price + (price * (5 / 100)), 2) 
    fake_price = round(price + (price * (perc / 100)), 2)  # Calculate the fake price

    text = f'''
    <div class="product-card" data-name="{title + description}" onclick="openProductDetail(this)">
        <div class="discount-badge">{perc}% OFF</div>
        <img class = "product-image" src="{photo_source}" alt="{title}">
        <div class="product-name">{title}</div>
        <div class="product-description">{description}</div>
        <div class="price-container">
            <div class="old-price">${fake_price}</div>
            <div class="new-price">${price}</div>
        </div>
        <div class="extra-main">{extra}</div>
    </div>
    '''
    return text

codes_done = []
with open('ff.txt', 'w+', encoding="utf-8") as f:
    all_text = ''
    for idx,code in enumerate(codes):
        if code not in codes_done:
            code = str(code)
            photo_source = find_image_for_code(code)
            text = make_text(photo_source,code,ds[idx],prices[idx],desc[idx])
            all_text += text
            all_text += '\n'
            codes_done.append(code)
    print(all_text)
    f.write(all_text)
        