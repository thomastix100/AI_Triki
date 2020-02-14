
import numpy as np
from Game import Game
import copy


class Triki(Game):

    def actions(self,state):
        """Devemos retornar todas las posiciones donde podemos colocar una ficha"""
        lis = []
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] == 0:
                    lis.append((i,j))
        return lis

    def result(self,state, move):
        #Toma el tablero y la jugada, y retorna el tablero con la jugada.... osea el estado
        auxList = copy.deepcopy(state)
        auxList[move[0]][move[1]] = self.to_move(state)
        return auxList

    def utility(self, state, player):
        """Return the value of this final state to player."""
        """Devuelve el valor de este estado final al jugador"""
        finalista = 0
        if player == 1:
            player = 2


        for i in range(len(state)):
            if state[i].count(player) == 3:
                finalista = player

        auxState = state.copy()
        aux_state = [list(i) for i in zip(*auxState)]

        for i in range(len(aux_state)):
            if aux_state[i].count(player) == 3:
                finalista = player

        
        if state[0][0] == player:
            if state[1][1] == player:
                if state[2][2] == player:
                    finalista = player

        if state[0][2] == player:
            if state[1][1] == player:
                if state[2][0] == player:
                    finalista = player


        if finalista == 2:
            finalista = -1

        return finalista

    def terminal_test(self, state):
        """Return True if this is a final state for the game."""
        ganador = 1
        if self.to_move == 1:
            ganador = 2
        
        for i in range(len(state)):
            if state[i].count(ganador) == 3:
                return True

        auxState = state.copy()
        aux_state = [list(i) for i in zip(*auxState)]

        for i in range(len(aux_state)):
            if aux_state[i].count(ganador) == 3:
                return True
                
        return not self.actions(state)

    def to_move(self, state):
        """Return the player whose move it is in this state."""
        """Devuelve el jugador cuyo movimiento es en este estado"""
        num = 0
        for i in range(len(state)):
            for j in range(len(state[i])):
                if state[i][j] != 0:
                    num += 1
       
        if num%2 == 0:
            return 1
        else:
            return 2

    def display(self, state):
        """Print or otherwise display the state."""
        """Imprime o muestra el estado"""
        print(state)

    def __repr__(self):
        return '<{}>'.format(self.__class__.__name__)

    def play_game(self):
        """Play an n-person, move-alternating game."""
        raise NotImplementedError