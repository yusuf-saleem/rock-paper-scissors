from rps import getUserMove, getCpMove, declareWinner
import pytest

"""
test_getUserMove: Tests that getUserMove returns with correct move ID based on char input,
    otherwise return -1 as error

test_getCpMove: Tests that getCpuMove returns a valid move (1,2,or 3)

test_declareWinner: Tests that the game declares the correct winner based on moves made
"""


@pytest.mark.parametrize("test_input,expected,error",
[("r",1,"Incorrect ID for rock"),
("p",2,"Incorrect ID for paper"),
("s",3,"Incorrect ID for scissors"),
("z",-1,"Failed to recognize bad input!")]
)
def test_getUserMove(test_input,expected,error):

    """Tests that getUserMove returns with correct move ID based on char input,
    otherwise return -1 as error"""

    assert getUserMove(test_input) == expected, error

def test_getCpMove():

    """ Tests that getCpuMove returns a valid move (1,2,or 3)"""

    moves = [1,2,3]
    move = getCpMove()
    assert move in moves, "getCpuMove returned unkown move"

@pytest.mark.parametrize("userMove,cpMove,expected,error",
[(1,1,"Draw","declareWinner failed to recognize draw"),
(1,2,"Lose","declareWinner failed to recognize lose"),
(1,3,"Win","declareWinner failed to recognize win"),
(2,1,"Win","declareWinner failed to recognize win"),
(2,3,"Lose","declareWinner failed to recognize lose"),
(3,1,"Lose","declareWinner failed to recognize lose"),
(3,2,"Win","declareWinner failed to recognize win"),
(5,2,"InputError","declareWinner failed to recognize InputError")])
def test_declareWinner(userMove,cpMove,expected,error):

    """ Tests that the game declares the correct winner based on moves made"""

    assert declareWinner(userMove, cpMove) == expected, error