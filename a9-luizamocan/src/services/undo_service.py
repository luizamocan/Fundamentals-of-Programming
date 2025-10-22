from src.domain.exceptions import UndoError
class Operation:
    def __init__(self, functionUndo, functionRedo, data=None):
        self._functionUndo = functionUndo
        self._functionRedo = functionRedo
        self._data = data

    def undo(self):
        self._functionUndo(self._data)

    def redo(self):
        self._functionRedo(self._data)


class UndoService:
    def __init__(self):
        self._history = []
        self._index = -1

    def recordUndo(self, operation: Operation):
        self._history.append(operation)
        self._index = len(self._history) - 1

    def undo(self):
        if self._index == -1:
            raise UndoError("No more undo operations")
        else:
            print("Undo done successfully")
        self._history[self._index].undo()
        self._index = self._index - 1

    def redo(self):
        if self._index == len(self._history) - 1:
            raise UndoError("No more redo operations")
        else:
            print("Redo done successfully")
        self._index = self._index + 1
        self._history[self._index].redo()


class CascadeOperation:
    def __init__(self, *operations):
        self._operations = operations

    def undo(self):
        for operation in self._operations:
            operation.undo()

    def redo(self):
        for operation in self._operations:
            operation.redo()


class FunctionCall:
    def __init__(self, functionName, *functionArguments):
        self.__functionName = functionName
        self.__functionArguments = functionArguments

    def call(self):
        self.__functionName(*self.__functionArguments)

    def undo(self):
        # Undo is calling the function with the arguments reversed
        # This assumes that you can undo an operation by calling it with the reverse action
        if len(self.__functionArguments) == 1:
            self.__functionName(*self.__functionArguments)  # Call the function to reverse the action
        elif len(self.__functionArguments) > 1:
            # If there are more arguments, you may need to handle undo differently
            self.__functionName(*self.__functionArguments)

    def redo(self):
        # Redo calls the function again with the same arguments
        self.call()

    def __call__(self, *args, **kwargs):
        self.call()