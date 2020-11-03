class Player:
    def __init__(self, initialRow, initialColumn):
        self.rowPosition = initialRow
        self.columnPosition = initialColumn

    # TODO
    def moveUp(self):
         self.rowPosition -= 1
         
    # TODO
    def moveDown(self):
         self.columnPosition += 1

    # TODO
    def moveLeft(self):
          self.rowPosition -= 1

    # TODO
    def moveRight(self):
          self.rowPosition += 1
         
