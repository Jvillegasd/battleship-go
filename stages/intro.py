import sys
import pygame

# Import GUI items
from gui.card import Card
from gui.label import Label
from gui.button import Button
from gui.text_input import Input
from gui.dev_sign import DevSign


class Intro:
    """ This class manages Intro stage. """

    def __init__(self) -> None:
        self.states = {
            'game_started': False
        }
        self.gui_items = self.__load_gui_items()

        # Color name: Little Greene French Grey Pale
        self.background_color = (231, 231, 219)

    def handle_buttom_click(self, gui_btn: dict) -> bool:
        """ This function handles button click event """
        return gui_btn['enabled'] and gui_btn['item'].click()

    def draw(self, window: pygame.display) -> dict:
        """ This function draws gui items on window. """

        # Draw background
        window.fill(self.background_color)

        # Draw GUI items
        for _, gui_item in self.gui_items.items():
            if not gui_item['enabled']:
                continue

            if type(gui_item['item']) == list:
                for item in gui_item['item']:
                    item.draw(window)
            else:
                gui_item['item'].draw(window)

        pygame.display.update()

    def connect_to_server(self) -> None:
        """ This function creates a client to connect to game server. """
        self.gui_items['conn_label']['item'].change_text('Connecting to server...')

    def process_events(self) -> None:
        """
          This function handles pygame events related
          to current stage.
        """

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if self.gui_items['host_input']['enabled']:
                self.gui_items['host_input']['item'].handle_input_events(event)

            if self.gui_items['port_input']['enabled']:
                self.gui_items['port_input']['item'].handle_input_events(event)

        if self.handle_buttom_click(self.gui_items['start_button']):
            # self.states['game_started'] = True
            self.connect_to_server()

        return self.states

    def __load_gui_items(self) -> dict:
        """
          This function creates and loads gui items
          used in stage.
        """

        sign = DevSign(pos_x=325, pos_y=475)
        start_button = Button(
            text='Start game',
            pos_x=187,
            pos_y=320,
            width=120,
            height=40
        )
        title_label = Label(
            pos_x=190,
            pos_y=80,
            text='Battleship',
            font_size=20
        )
        card = Card(
          pos_x=100,
          pos_y=140,
          width=300,
          height=250
        )
        conn_label = Label(pos_x=170, pos_y=163, text='Connect to a server')

        host_input = Input(pos_x=230, pos_y=210, width=120)
        host_label = Label(pos_x=160, pos_y=212, text='Host:')

        port_input = Input(pos_x=230, pos_y=260, width=120)
        port_label = Label(pos_x=160, pos_y=262, text='Port:')

        gui_items = {
            'dev_sign': {
                'enabled': True,
                'item': sign
            },
            'card': {
                'enabled': True,
                'item': card
            },
            'title_label': {
                'enabled': True,
                'item': title_label
            },
            'host_label': {
                'enabled': True,
                'item': host_label
            },
            'host_input': {
                'enabled': True,
                'item': host_input
            },
            'port_label': {
                'enabled': True,
                'item': port_label
            },
            'port_input': {
                'enabled': True,
                'item': port_input
            },
            'conn_label': {
                'enabled': True,
                'item': conn_label  
            },
            'start_button': {
                'enabled': True,
                'item': start_button
            },
        }

        return gui_items
