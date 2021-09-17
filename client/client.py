from random import randint
import grpc
from google.protobuf.json_format import MessageToJson
import json

import pb.gateway_pb2, pb.gateway_pb2_grpc


table_number = randint(1, 10)
CATEGORY = {
    'sandwiches': 'SANDUICHES',
    'dishMades': 'PRATOS FEITOS',
    'drinks': 'BEBIDAS',
    'desserts': 'SOBREMESAS'
}

print('Seja Bem vindo ao restaurante FOOD BAR!\nEstá é a mesa ' + str(table_number) + '\n')

def show_options():
    while True:
        print('Selecione uma opção válida!')

        print('DIGITE O NUMERO CORRESPONDENTE A OPÇÃO DESEJADA\n')

        print('[ 1 ] Realizar um pedido ')
        print('[ 2 ] Pedir a conta \n')
        IN = input()
        if IN == '1' or IN == '2':
            return int(IN)

        print('OPÇÃO INVALIDA!\n')

def converter_to_price_str(price:float):
    price_str_split = str(price).split('.')
    return 'R$ {},{}'.format(price_str_split[0], price_str_split[1])


def selected_items_from_menu(menu:dict):
    map_cod = dict()
    cod = 1
    items = list()

    categories = menu.keys()
    for category in categories:
        if len(menu[category]) != 0:
            print("\n## {} ##\n".format(CATEGORY[category]))
            for food in menu[category]:
                map_cod[cod] = {'id':food['id'], 'name': food['name']}
                print('[ {} ] {} - {}'.format(cod, food['name'], converter_to_price_str(food['price'])))
                cod += 1

                if food.get('ingredients'):
                    ingredients_str = ''
                    for index in range(len(food['ingredients'])):
                        ingredients_str += food['ingredients'][index]
                        if index != len(food['ingredients']) -1:
                            ingredients_str += ', '
                    print(ingredients_str + '.\n')
                else:
                    print('\n')

    print('\n[ OK ]\n')
    while True:
        cod_input = input()
        try:
            if cod_input.upper() == 'OK':
                return items
            item_id = map_cod[int(cod_input)]['id']
            items.append(item_id)
            print('\n{} Adicionado\n'.format(map_cod[int(cod_input)]['name']))

        except:
            print('\nOpção inválida\n')

def get_menu():
    #Mock
    """ return {
        "sandwiches": [
            {
                "id": "123",
                "name": "X-Salada",
                "price": 26.55,
                "ingredients": ["Tomate", "pão", "alface"]
            }
        ],
        "dishMade": [],
        "drinks": [],
        "dessert": []
    } """
    with grpc.insecure_channel('localhost:5000') as channel:
        stub = pb.gateway_pb2_grpc.ServerStub(channel)
        request = pb.gateway_pb2.MenuRequest(tableNumber = table_number)
        response = stub.GetMenu(request)
        json_obj = json.loads(MessageToJson(response))
        return json_obj

while True:

    option = show_options()
    if option == 1:
        menu = get_menu()
        items = selected_items_from_menu(menu)

        print('\nPreparaando pedido ...\n')

# print('[ 1 ] X-Salada - R$29,35\nPÃO, alface, tomate')