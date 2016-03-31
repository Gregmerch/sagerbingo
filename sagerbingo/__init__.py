import pandas as pd
import numpy as np
from IPython.display import Audio

sf = 'files/ld_sd_compiled.mp3'
sf2 = 'files/ld_sd_shuffled1.mp3'
sf3 = 'files/ld_sd_shuffled2.mp3'
sf4 = 'files/ld_sd_shuffled3.mp3'
sf5 = 'files/ld_sd_shuffled4.mp3'
sf6 = 'files/ld_sd_shuffled5.mp3'
sf_l = [sf2,sf3,sf4,sf5,sf6]

def setup():
    return Audio(url='../sagerbingo/'+sf,autoplay=True)

def shuffle():
    return Audio(url='../sagerbingo/'+np.random.choice(sf_l),autoplay=True)


class Board(object):
    """
    This package creates a board object
    There is an attribute of board called board (Board.board) that is a data frame.
    You can always add new square options using the add_option method
    Also you the X function crosses out a given box (For example 'S1' or 'R5') pass the elements into that method as
    board.X('S',1)
    Check the example ipynb for help
    """
    def __init__(self,squares):
        self.squares_options = squares
        #self.squares = np.random.choice(self.squares_options,25,replace=False).reshape(5,5)
        self.games = ['simple','cross','X','blackout']
        self.shuffle()
        self.sound(sf)

    def add_option(self,option):
        self.squares_options.append(option)
        
    def shuffle(self):
        self.squares = np.random.choice(self.squares_options,25,replace=False).reshape(5,5)
        self.board = pd.DataFrame(self.squares)
        self.board.columns = ['S','A','G','E','R']
        self.board['G'][2] = "Good Afternoon Business Analysts!"
        return self.board


    def X(self,col,row):
        text = self.board.ix[row][col]
        return_val = unicode()
        for c in text:
            return_val = unicode(return_val + c)+ u'\u0336'
        self.board.ix[row][col] = return_val
        return self.board
    
    def un_X(self,col,row):
        text = self.board.ix[row][col]
        return_val = ''
        for c in text:
            if c == u'\u0336':
                pass
            else: return_val += c
        self.board.ix[row][col] = return_val
        return self.board


    def sound(self,soundfile):
        ex_folder = '../sagerbingo'
        return Audio(url=ex_folder+sf,autoplay=True)

    """
    Game development is still active
    def bingo(self,game='simple'):
        self.game = game
        if self.game == 'simple':
            if self.board.sum(axis=0) == 5:
                return "Winner"
            elif self.board.sum(axis=1) == 5:
                return "Winner"
        elif self.game == 'cross':
            self.board.ix[2].sum()
    """