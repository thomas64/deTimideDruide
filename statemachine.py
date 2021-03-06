
"""
class: StateMachine
"""

from console import Console
from constants import GameState


class StateMachine(object):
    """
    Manages a stack based state machine.
    peek(), pop() and push() perform as traditionally expected.
    peeking and popping an empty stack returns None.
    """
    def __init__(self):
        self.statestack = list()
        self.prev_state = None
        self.new_state = False

    def peek(self):
        """
        Returns the current state without altering the stack.
        Returns None if the stack is empty.
        """
        try:
            return self.statestack[-1]      # [-1] is om de laatste in een list te krijgen
        except IndexError:
            return None                     # empty stack

    def deep_peek(self, stackindex=-2):
        """
        Kijk in de op een na bovenste laag van de stack.
        :param stackindex: -1 is de bovenste, -2 is de op een na bovenste, -3 etc.
        """
        try:
            return self.statestack[stackindex]
        except IndexError:
            return None

    def pop(self):
        """
        Returns the current state and remove it from the stack.
        Returns None if the stack is empty.
        """
        try:
            # fade is nooit een prev state
            if self.peek().name != GameState.FadeBlack:
                self.prev_state = self.peek().name
            self.peek().on_exit()
            # bij messagebox en fade geen console output
            if self.peek().name != GameState.MessageBox and \
               self.peek().name != GameState.FadeBlack:
                Console.state_pop(self.peek().name)
            del self.statestack[-1]
            if not self.is_empty():
                self.peek().on_enter()
            self.new_state = True
            return len(self.statestack) > 0
        except IndexError:
            return None                     # empty stack

    def deep_pop(self, stackindex=-2):
        """
        Pop de op een na bovenste laag van de stack.
        Deze is in leven geroepen zodat je eerst wat op de stack kan gooien. En dan die daar onder zit te poppen.
        Op deze manier wordt de on_enter() van die dááronder niet aangeroepen.
        """
        self.deep_peek().on_exit()
        Console.state_deep_pop(self.deep_peek().name)
        del self.statestack[stackindex]

    def push(self, state, with_on_enter=True):
        """
        :param state: Push a new state onto the stack.
        :param with_on_enter: wanneer False, sla dan de on_enter() over. vaak voor het uitstellen van de muziek.
        :return: Returns the pushed value.
        """
        try:  # try is voor als er niets te peeken valt nog
            if self.peek().name != GameState.FadeBlack:
                self.prev_state = self.peek().name
        except AttributeError:
            pass
        if state.name != GameState.MessageBox and \
           state.name != GameState.FadeBlack:
            Console.state_push(state.name)
        self.statestack.append(state)
        if with_on_enter:
            self.peek().on_enter()
        self.new_state = True
        return state

    def _clear(self):
        """
        Clear the whole stack.
        """
        if self.peek().name != GameState.FadeBlack:
            self.prev_state = self.peek().name
        self.peek().on_exit()
        Console.state_clear()
        self.statestack = []

    def change(self, state, with_on_enter=True):
        """
        Clear the whole stack. And pushes one.
        :param state: Push a new state onto the stack.
        :param with_on_enter: wanneer False, sla dan de on_enter() over. vaak voor het uitstellen van de muziek.
        """
        self._clear()
        self.push(state, with_on_enter)

    def is_empty(self):
        """..."""
        return len(self.statestack) == 0

    def swap(self):
        """
        X (Als de laatste 2 op de stack een messagebox zijn, draai ze dan om.) X
        Nee, draai ze gewoon om, ongeacht de voorwaarde.
        """
        # if self.statestack[-1].name == GameState.MessageBox and self.statestack[-2].name == GameState.MessageBox:
        self.statestack[-1], self.statestack[-2] = self.statestack[-2], self.statestack[-1]

        """
        Interessant om later misschien eens (ongeveer) te gebruiken. Deze draait een gedeelte van de list om.
        def reverse_sublist(lst,start,end):
            sublist=lst[start:end]
            sublist.reverse()
            lst[start:end]=sublist
            print(lst)
        """

    def push_confirmbox_to_end(self):
        """
        Kijk eerst of de laatste een ConfirmBox is.
        Ga dan van voren bekijken naar de eerste MessageBox.
        Stop dan de ConfirmBox voor die MessageBox.
        Verwijder de ConfirmBox aan het eind.
        """
        if self.peek().name == GameState.ConfirmBox:
            first_index = None
            for index, state in enumerate(self.statestack):
                if state.name == GameState.MessageBox:
                    first_index = index
                    break
            if first_index is not None:
                self.statestack.insert(first_index, self.peek())
                self.pop()
            else:
                Console.error_no_messagebox_in_stack()
                raise AttributeError
        else:
            Console.error_no_confirmbox_in_top_state()
            raise AttributeError

    def input_state_after_all_messageboxes(self, new_state):
        """
        Kijk eerst van voren waar de eerste MessageBox is.
        Stop dan de nieuwe messageboxen ervoor.
        """
        first_index = None
        for index, state in enumerate(self.statestack):
            if state.name == GameState.MessageBox:
                first_index = index
                break
        if first_index is not None:
            self.statestack.insert(first_index, new_state)
        else:
            Console.error_no_messagebox_in_stack()
            raise AttributeError
