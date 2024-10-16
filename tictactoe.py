import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BUTTON_COLOR = (100, 100, 100)
BUTTON_HOVER_COLOR = (150, 150, 150)

# Game variables
GAME_WIDTH = 400  # Width of the game area
GAME_HEIGHT = 400  # Height of the game area
LINE_WIDTH = 10
BOARD_ROWS = 3
BOARD_COLS = 3
SQUARE_SIZE = GAME_WIDTH // BOARD_COLS
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 15
CROSS_WIDTH = 25
SPACE = SQUARE_SIZE // 4

# Screen size (larger than game variables)
SCREEN_WIDTH = 800  # Increase the width to 800
SCREEN_HEIGHT = 800  # Increase the height to 800

# Calculate offsets to center the grid
OFFSET_X = (SCREEN_WIDTH - GAME_WIDTH) // 2
OFFSET_Y = (SCREEN_HEIGHT - GAME_HEIGHT) // 2

# Set up the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Tic Tac Toe With AI')

# Board representation
board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]

# Player vs AI markers
player = 'X'
ai = 'O'

# Win counters
player_wins = 0
ai_wins = 0

# Function to reset win counters
def reset_win_counters():
    global player_wins, ai_wins
    player_wins = 0
    ai_wins = 0

# Draw the grid
def draw_grid():
    screen.fill(BLACK)
    for row in range(BOARD_ROWS + 1):
        pygame.draw.line(screen, WHITE, (OFFSET_X, OFFSET_Y + row * SQUARE_SIZE), (OFFSET_X + GAME_WIDTH, OFFSET_Y + row * SQUARE_SIZE), LINE_WIDTH)
    for col in range(BOARD_COLS + 1):
        pygame.draw.line(screen, WHITE, (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y), (OFFSET_X + col * SQUARE_SIZE, OFFSET_Y + GAME_HEIGHT), LINE_WIDTH)

# Draw X or O on the board
def draw_figures():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 'X':
                # Draw X
                pygame.draw.line(screen, WHITE, (OFFSET_X + col * SQUARE_SIZE + SPACE, OFFSET_Y + row * SQUARE_SIZE + SPACE),
                                 (OFFSET_X + col * SQUARE_SIZE + SQUARE_SIZE - SPACE, OFFSET_Y + row * SQUARE_SIZE + SQUARE_SIZE - SPACE), CROSS_WIDTH)
                pygame.draw.line(screen, WHITE, (OFFSET_X + col * SQUARE_SIZE + SPACE, OFFSET_Y + row * SQUARE_SIZE + SQUARE_SIZE - SPACE),
                                 (OFFSET_X + col * SQUARE_SIZE + SQUARE_SIZE - SPACE, OFFSET_Y + row * SQUARE_SIZE + SPACE), CROSS_WIDTH)
            elif board[row][col] == 'O':
                # Draw O
                pygame.draw.circle(screen, WHITE, (OFFSET_X + int(col * SQUARE_SIZE + SQUARE_SIZE // 2), OFFSET_Y + int(row * SQUARE_SIZE + SQUARE_SIZE // 2)),
                                   CIRCLE_RADIUS, CIRCLE_WIDTH)

# Check if there's a winner
def check_winner():
    # Check rows, columns and diagonals
    for row in range(BOARD_ROWS):
        if board[row][0] == board[row][1] == board[row][2] != ' ':
            return board[row][0]
    for col in range(BOARD_COLS):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]
    return None

# Check if the board is full
def is_board_full():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                return False
    return True

# Game over screen
def game_over_screen(winner):
    global player_wins, ai_wins

    font = pygame.font.Font(None, 74)
    if winner == player:
        player_wins += 1
        message = f'YOU WIN ({player_wins})'
    elif winner == ai:
        ai_wins += 1
        message = f'AI WIN ({ai_wins})'
    else:
        message = 'NO ONE WIN'
    text = font.render(message, True, WHITE)
    screen.fill(BLACK)
    screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 4))
    
    play_again_text = font.render('Play Again', True, WHITE)
    reset_text = font.render('Home', True, WHITE)
    screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT - 150))
    screen.blit(reset_text, (SCREEN_WIDTH // 2 - reset_text.get_width() // 2, SCREEN_HEIGHT - 100))
    
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 + play_again_text.get_height() // 2))
                reset_rect = reset_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100 + reset_text.get_height() // 2))
                if play_again_rect.collidepoint((mouseX, mouseY)):
                    main()
                if reset_rect.collidepoint((mouseX, mouseY)):
                    reset_win_counters()
                    main_menu()
            if event.type == pygame.MOUSEMOTION:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                play_again_rect = play_again_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 150 + play_again_text.get_height() // 2))
                reset_rect = reset_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT - 100 + reset_text.get_height() // 2))
                if play_again_rect.collidepoint((mouseX, mouseY)):
                    play_again_text = font.render('Play Again', True, BUTTON_HOVER_COLOR)
                else:
                    play_again_text = font.render('Play Again', True, WHITE)
                if reset_rect.collidepoint((mouseX, mouseY)):
                    reset_text = font.render('Home', True, BUTTON_HOVER_COLOR)
                else:
                    reset_text = font.render('Home', True, WHITE)
                screen.fill(BLACK)
                screen.blit(text, (SCREEN_WIDTH // 2 - text.get_width() // 2, SCREEN_HEIGHT // 4))
                screen.blit(play_again_text, (SCREEN_WIDTH // 2 - play_again_text.get_width() // 2, SCREEN_HEIGHT - 150))
                screen.blit(reset_text, (SCREEN_WIDTH // 2 - reset_text.get_width() // 2, SCREEN_HEIGHT - 100))
                pygame.display.update()

# Minimax algorithm for AI
def minimax(is_maximizing):
    winner = check_winner()
    if winner == player:
        return -1
    if winner == ai:
        return 1
    if is_board_full():
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = ai
                    score = minimax(False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(BOARD_ROWS):
            for col in range(BOARD_COLS):
                if board[row][col] == ' ':
                    board[row][col] = player
                    score = minimax(True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

# AI move function
def ai_move():
    best_score = -math.inf
    best_move = None
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == ' ':
                board[row][col] = ai
                score = minimax(False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    if best_move:
        board[best_move[0]][best_move[1]] = ai

# Main menu
def main_menu():
    font = pygame.font.Font(None, 74)
    screen.fill(BLACK)
    start_text = font.render('Start Game', True, WHITE)
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - start_text.get_height() // 2))
    pygame.display.update()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                if text_rect.collidepoint((mouseX, mouseY)):
                    return
            if event.type == pygame.MOUSEMOTION:
                mouseX = event.pos[0]
                mouseY = event.pos[1]
                text_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
                if text_rect.collidepoint((mouseX, mouseY)):
                    start_text = font.render('Start Game', True, BUTTON_HOVER_COLOR)
                else:
                    start_text = font.render('Start Game', True, WHITE)
                screen.fill(BLACK)
                screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, SCREEN_HEIGHT // 2 - start_text.get_height() // 2))
                pygame.display.update()

# Main game loop
def main():
    global board
    board = [[" " for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    draw_grid()
    game_over = False

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                mouseX = event.pos[0]
                mouseY = event.pos[1]

                clicked_row = (mouseY - OFFSET_Y) // SQUARE_SIZE
                clicked_col = (mouseX - OFFSET_X) // SQUARE_SIZE

                if 0 <= clicked_row < BOARD_ROWS and 0 <= clicked_col < BOARD_COLS:
                    if board[clicked_row][clicked_col] == ' ':
                        board[clicked_row][clicked_col] = player
                        draw_figures()

                        winner = check_winner()
                        if winner or is_board_full():
                            draw_figures()
                            pygame.display.update()
                            pygame.time.wait(1000)
                            game_over = True
                            game_over_screen(winner)
                        else:
                            ai_move()
                            draw_figures()

                        winner = check_winner()
                        if winner or is_board_full():
                            draw_figures()
                            pygame.display.update()
                            pygame.time.wait(1000)
                            game_over = True
                            game_over_screen(winner)

        pygame.display.update()

if __name__ == "__main__":
    main_menu()
    main()