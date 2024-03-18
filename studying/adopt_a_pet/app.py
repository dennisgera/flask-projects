from flask import Flask
from adopt_a_pet_helper import pets

app = Flask(__name__)

@app.route('/')
def index():
    return """<h1>Adopt a pet</h1><p>Browse through the links below to find your new flurry friend:</p>
    <ul><li><a href='/animals/dogs'>Dogs</a></li><li><a href='/animals/cats'>Cats</a></li><li>
    <a href='/animals/rabbits'>Rabbits</a></li></ul>"""


@app.route('/animals/<pet_type>')
def animals(pet_type):
    html = f'<h1>List of {pet_type}</h1><ul>'
    for idx, pet in enumerate(pets[pet_type]):
        html += f'<li><a href="/animals/{pet_type}/{idx}">{pet["name"]}</a></li>'  
    html += '</ul>'
    return html

def pet(pet_type, pet_id):
    pet = pets[pet_type][pet_id]
    return f"""
    <h1>{pet['name']}</h1>
    <img src={pet['url']} />
    <p>Age: {pet['description']}</p>
    <p>Breed: {pet['breed']}</p>
    <p>{pet['description']}</p>
    """