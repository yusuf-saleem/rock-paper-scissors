# Game: Rock, Paper, Scissors
This is a simple Python implementation of the classic game Rock, Paper, Scissors.
It can be run on its own using Python from terminal, or containerized if Docker is installed on the system.
Pytest unit tests are included to test the functions of the game.

* Rock blunts scissors
* Paper covers rock
* Scissors cut paper

- First, let the player choose Rock, Paper or Scissors by typing the letter ‘r’, ‘p’ or ‘s’;
- Then computer's turn;
- Decide game win, lose or draw, print choice of both sides

## Running With Docker
You are required to create a Dockerfile that allows us to build a docker container and execute the tool with docker run without having any dependencies other than docker installed, the following is what a user should do to run the application or tests:
   1. docker build -t rock-paper-scissors                              Build the docker image
   2. docker run -it --rm rock-paper-scissors                          Run the docker image which automatically starts the game
   3. docker run -ti --rm rock-paper-scissors pytest -v /app/test.py   Run the unit tests for the game

## Running With Python
This assumes you have Python3 installed on your system with pytest.
   1. python3 rps.py     Run the game
   2. pytest -v test.py  Run the unit tests for the game

    
    
