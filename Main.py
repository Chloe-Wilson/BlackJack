import pygame
from random import randint
from os import path
import os

pygame.init()
pygame.font.init()

screen = pygame.display.set_mode((1000, 800))
pygame.display.set_caption('BlackJack with GUI')
felt = (0, 100, 0)
red = (255, 0, 0)
white = (255, 255, 255)
screen.fill(felt)
myFont = pygame.font.SysFont('Comic Sans MS', 30)

if not path.exists("Money.txt"):
    f = open("Money.txt", 'w')
    f.write('100')
    f.close()

f = open("Money.txt", 'r')
try:
    tmp = f.readlines()
    money = float(tmp[0])
except:
    money = 100
f.close()

bet = 0

fullDeck = ['Ace of Spades', 'Two of Spades', 'Three of Spades', 'Four of Spades', 'Five of Spades',
            'Six of Spades', 'Seven of Spades', 'Eight of Spades', 'Nine of Spades', 'Ten of Spades',
            'Jack of Spades', 'Queen of Spades', 'King of Spades',
            'Ace of Diamonds', 'Two of Diamonds', 'Three of Diamonds', 'Four of Diamonds', 'Five of Diamonds',
            'Six of Diamonds', 'Seven of Diamonds', 'Eight of Diamonds', 'Nine of Diamonds', 'Ten of Diamonds',
            'Jack of Diamonds', 'Queen of Diamonds', 'King of Diamonds',
            'Ace of Clubs', 'Two of Clubs', 'Three of Clubs', 'Four of Clubs', 'Five of Clubs',
            'Six of Clubs', 'Seven of Clubs', 'Eight of Clubs', 'Nine of Clubs', 'Ten of Clubs',
            'Jack of Clubs', 'Queen of Clubs', 'King of Clubs',
            'Ace of Hearts', 'Two of Hearts', 'Three of Hearts', 'Four of Hearts', 'Five of Hearts',
            'Six of Hearts', 'Seven of Hearts', 'Eight of Hearts', 'Nine of Hearts', 'Ten of Hearts',
            'Jack of Hearts', 'Queen of Hearts', 'King of Hearts']
deck = list(fullDeck)
dealer = []
hand = []
turn = 2
start = True
running = True


def resetDeck(deck):
    deck = list(fullDeck)


def drawTxt(txt, color, x, y):
    drawtxt = myFont.render(txt, False, color)
    screen.blit(drawtxt, (x, y))


def playCard(card, x, y):
    pic = pygame.image.load('PlayingCards\\' + str(card) + '.png')
    pic = pygame.transform.scale(pic, (100, 140))
    screen.blit(pic, (x, y))


def deal():
    if len(deck) < 20:
        resetDeck(deck)

    # Deal dealers cards
    while len(dealer) != 0:
        dealer.pop(0)
    delt = randint(0, len(deck) - 1)
    dealer.append(deck[delt])
    deck.pop(delt)
    delt = randint(0, len(deck) - 1)
    dealer.append(deck[delt])
    deck.pop(delt)

    # Deal player cards
    while len(hand) != 0:
        hand.pop(0)
    delt = randint(1, len(deck)) - 1
    hand.append(deck[delt])
    deck.pop(delt)
    delt = randint(1, len(deck)) - 1
    hand.append(deck[delt])
    deck.pop(delt)

    # Draw cards
    playCard(dealer[0], 300, 100)
    playCard('cardBack', 325, 100)
    playCard(hand[0], 300, 560)
    playCard(hand[1], 325, 560)


def drawHitStandButton():
    pygame.draw.rect(screen, red, (100, 650, 100, 50))
    pygame.draw.rect(screen, red, (800, 650, 100, 50))
    drawTxt('Hit', white, 128, 650)
    drawTxt('Stand', white, 808, 650)


def drawPlayerTurn():
    screen.fill(felt)
    drawDeck()

    deal()
    drawHitStandButton()


def drawDeck():
    screen.blit(pygame.transform.scale(pygame.image.load('PlayingCards\cardBack.png'), (100, 140)), (50, 350))
    drawTxt("Money = $" + str(money), (0, 0, 0), 10, 10)


def betting():
    screen.fill(felt)
    drawDeck()

    # Bet add
    pygame.draw.rect(screen, red, (850, 325, 50, 50))
    pygame.draw.rect(screen, white, (870, 335, 10, 30))
    pygame.draw.rect(screen, white, (860, 345, 30, 10))

    # Bet minus
    pygame.draw.rect(screen, red, (850, 425, 50, 50))
    pygame.draw.rect(screen, white, (860, 445, 30, 10))

    # Bet button
    pygame.draw.rect(screen, red, (720, 500, 170, 50))
    drawTxt('Place Bet', white, 740, 500)

    drawTxt('$' + str(bet), (0, 0, 0), 750, 375)


def hit():
    if len(hand) >= 10:
        drawTxt('That\'s enough cards', white, 400, 385)
        return
    delt = randint(0, len(deck) - 1)
    hand.append(deck[delt])
    deck.pop(delt)
    playCard(hand[len(hand) - 1], 275 + len(hand) * 25, 560)


def value(card):
    splitCard = card.split()
    if splitCard[0] == 'Ace':
        return 11
    if splitCard[0] == 'Two':
        return 2
    if splitCard[0] == 'Three':
        return 3
    if splitCard[0] == 'Four':
        return 4
    if splitCard[0] == 'Five':
        return 5
    if splitCard[0] == 'Six':
        return 6
    if splitCard[0] == 'Seven':
        return 7
    if splitCard[0] == 'Eight':
        return 8
    if splitCard[0] == 'Nine':
        return 9
    if splitCard[0] == 'Ten':
        return 10
    if splitCard[0] == 'Jack':
        return 10
    if splitCard[0] == 'Queen':
        return 10
    if splitCard[0] == 'King':
        return 10

def drawDealerTurn():
    pygame.draw.rect(screen, felt, (400, 385, 200, 30))
    pygame.draw.rect(screen, felt, (100, 650, 100, 50))
    pygame.draw.rect(screen, felt, (800, 650, 100, 50))
    playCard(dealer[1], 325, 100)
    pygame.display.update()
    total = 0
    for card in hand:
        if value(card) == 11 and total > 10:
            total += 1
        else:
            total += value(card)

    dealerTotal = 0
    dealer.sort(key=value)
    for card in dealer:
        if value(card) == 11 and dealerTotal > 10:
            dealerTotal += 1
        else:
            dealerTotal += value(card)

    while dealerTotal < 17:
        delt = randint(0, len(deck) - 1)
        dealer.append(deck[delt])
        playCard(deck[delt], 275 + len(dealer) * 25, 100)
        deck.pop(delt)

        dealerTotal = 0
        dealer.sort(key=value)
        for card in dealer:
            if value(card) == 11 and dealerTotal > 10:
                dealerTotal += 1
            else:
                dealerTotal += value(card)

    if total == 21 and len(hand) == 2:
        drawTxt('BlackJack', white, 400, 375)
        return 2
    elif total > 21:
        drawTxt('Bust', white, 400, 375)
        return 0
    elif dealerTotal > 21:
        drawTxt('Dealer Busted', white, 400, 375)
        return 1
    elif total > dealerTotal:
        drawTxt('You Win', white, 400, 375)
        return 1
    elif total < dealerTotal:
        drawTxt('You Lose', white, 400, 375)
        return 0
    else:
        drawTxt('Tie', white, 400, 375)
        return 3

def drawPlayAgain():
    pygame.draw.rect(screen, red, (715, 100, 185, 50))
    drawTxt('Play Again', white, 735, 100)

while running:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if turn == 2:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 850 < mouse[0] < 900 and 325 < mouse[1] < 375:
                    bet += 5
                    if bet > money:
                        bet = money
                elif 850 < mouse[0] < 900 and 425 < mouse[1] < 475:
                    bet -= 5
                    if bet < 0:
                        bet = 0
                if 720 < mouse[0] < 890 and 500 < mouse[1] < 550:
                    turn = 1
                    start = True
        elif turn == 1:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 100 < mouse[0] < 200 and 650 < mouse[1] < 700:
                    hit()
                elif 800 < mouse[0] < 900 and 650 < mouse[1] < 700:
                    hand.sort(key=value)
                    turn = 0
                    start = True
        elif turn == 0:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                if 715 < mouse[0] < 900 and 100 < mouse[1] < 150:
                    bet = 0
                    turn = 2
    if bet == 0 and turn == 1:
        break
    if turn == 2:
        betting()
    if turn == 1 and start == True:
        drawPlayerTurn()
        start = False
    if turn == 0 and start == True:
        result = drawDealerTurn()
        if result == 0:
            money -= bet
        elif result == 1:
            money += bet
        elif result == 2:
            money += bet * 1.5
        start = False
    if turn == 0:
        drawPlayAgain()

os.remove("Money.txt")
if money != 0:
    f = open("Money.txt", 'w')
    f.write(str(money))
    f.close()
pygame.quit()
