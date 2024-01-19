import requests
from django.shortcuts import render
from .models import Card
import random

def index(request):
    random_commanders = fetch_random_mtg_cards()
    processed_commanders = [process_card(card) for card in random_commanders]

    context = {
        'commanders': processed_commanders
    }
    return render(request, 'home/index.html', context)



async def async_fetch_mtg_cards():
    url = 'https://api.magicthegathering.io/v1/cards?supertypes=legendary&types=creature'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            if response.status == 200:
                data = await response.json()
                return data['cards'][:10]  # Limiting to 10 cards
            else:
                return []


async def fetch_legendary_creatures(request):
    commanders = cache.get('commanders')
    if not commanders:
        mtg_cards = await async_fetch_mtg_cards()
        # process and store the cards
        commanders = [await process_card(card_data) for card_data in mtg_cards]
        cache.set('commanders', commanders, timeout=3600)

    return render(request, 'commanders.html', {'commanders': commanders})


def process_card(card_data):
    card, created = Card.objects.get_or_create(
        name=card_data['name'],
        defaults={
            'mana_cost': card_data.get('manaCost', ''),
            'cmc': card_data.get('cmc', 0),
            'type_line': card_data.get('type', ''),
            'oracle_text': card_data.get('text', ''),
            'colors': ','.join(card_data.get('colors', [])),
            'image_url': card_data.get('imageUrl', '')
        }
    )
    return card


def fetch_random_mtg_cards():
    url = 'https://api.magicthegathering.io/v1/cards?supertypes=legendary&types=creature'
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        all_cards = data['cards']
        random_cards = random.sample(all_cards, min(len(all_cards), 9))
        return random_cards
    else:
        return []

