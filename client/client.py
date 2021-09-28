from random import randint
import json

from pyfiglet import figlet_format
import grpc
from google.protobuf.json_format import MessageToJson

import pb.gateway_pb2, pb.gateway_pb2_grpc


class GatewayService:
    def __init__(self, tableNumber) -> None:
        self.tableNumber = tableNumber

    def getMenu(self) -> dict:
        with grpc.insecure_channel('localhost:5000') as channel:
            stub = pb.gateway_pb2_grpc.ServerStub(channel)
            request = pb.gateway_pb2.MenuRequest(tableNumber=self.tableNumber)
            response = stub.GetMenu(request)
            return json.loads(MessageToJson(response))

    def createOrder(self, items) -> dict:
        with grpc.insecure_channel('localhost:5000') as channel:
            stub = pb.gateway_pb2_grpc.ServerStub(channel)
            request = pb.gateway_pb2.OrderRequest(id=items, tableNumber=self.tableNumber)
            response = stub.CreateOrder(request)
            return json.loads(MessageToJson(response))

    def closeAccount(self) -> dict:
        with grpc.insecure_channel('localhost:5000') as channel:
            stub = pb.gateway_pb2_grpc.ServerStub(channel)
            request = pb.gateway_pb2.CloseAccountRequest(tableNumber=self.tableNumber)
            response = stub.CloseAccount(request)
            return json.loads(MessageToJson(response))

# Inciando variáveis globais

table_number = randint(1, 100)

service = GatewayService(table_number)

CATEGORY = {
    'sandwiches': 'SANDUICHES',
    'dishMades': 'PRATOS FEITOS',
    'drinks': 'BEBIDAS',
    'desserts': 'SOBREMESAS'
}

def showFiglet(phrase):
    print(figlet_format(phrase, font='starwars'))

def show_options():
    while True:
        print('Selecione uma opção válida!\n')

        print('************* DIGITE O NUMERO CORRESPONDENTE A OPÇÃO DESEJADA *************\n')

        print('[ 1 ] Realizar um pedido ')
        print('[ 2 ] Pedir a conta \n')
        IN = input()
        if IN == '1' or IN == '2':
            return int(IN)

        print('************* OPÇÃO INVALIDA! *************\n')

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

    print('\nDIGITE [ OK ] PARA ENVIAR O PEDIDO\n')

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
    return service.getMenu()

def create_order(items):
    return service.createOrder(items)

def close_account():
    return service.closeAccount()

def show_total_account(total):
    print('****** TOTAL ******')
    showFiglet('R$ {}'.format(total))

def show_order_done(order) -> None:
    t = int(order.get('preparationTime'))
    for food in order.get('foods'):
        print(' ####### ' + food.upper() + '#######')
    print('\nTEMPO TOTAL: {} min: {} seg\n'.format(t//60, t%60))

def selected_otpions():
    while True:
        print('Selecione uma opção válida!\n')

        print('************* DIGITE O NUMERO CORRESPONDENTE A OPÇÃO DESEJADA *************\n')

        print('[ 1 ] Pedir a conta ')
        print('[ 2 ] Pedir novamente\n')
        opt = input()
        if opt == '1' or opt == '2':
            return int(opt)

        print('************* OPÇÃO INVALIDA! *************\n')


def startAttendance():
    import time
    time.sleep(1)
    while True:

        """ option = show_options()
        if option == 1:
            while True: """

        menu = get_menu()
        items = selected_items_from_menu(menu)
        print('\nPreparando pedido ...\n')
        order = create_order(items)
        show_order_done(order)
        opt = selected_otpions()

        if opt == 1 :
            total = close_account()

            show_total_account(total['total'])
            break

        
        
            


# print('[ 1 ] X-Salada - R$29,35\nPÃO, alface, tomate')


if __name__ == '__main__':
    showFiglet('FOOD BAR')
    print('Seja Bem vindo ao restaurante FOOD BAR!\nEstá é a mesa ' + str(table_number) + '\n')
    
    startAttendance()
