import random
import pygame

pygame.init()
screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Hangman")
scene = 0 # -1: 종료 0: 메인 1: 단어 입력 2: 게임 4: 게임 오버 5: 게임 클리어
difficulty = 0 # 0: easy 1: normal 2: hard 
mode = 0 # 0: 싱글플레이 1: 멀티플레이

alphabet = "abcdefghijklmnopqrstuvwxyz"

word_easy = ["pear", "apple", "orange", "mango", "grapes", 
            "peach", "plum", "kiwi", "banana", "melon", 
            "papaya", "pineapple", "coconut", "cherry", "blueberry", 
            "lemon", "tiger", "lion", "giraffe", "gorilla", 
            "fox", "owl", "panda", "wolf", "zebra", 
            "koala", "bear", "camel", "deer", "bat", 
            "duck", "dog", "cat", "kangaroo", "leopard", 
            "cheetah", "sheep", "goat", "buffalo", "rabbit", 
            "horse", "pig", "spain", "sweden", "greece", 
            "iraq", "korea", "black", "white",  "grey", 
            "pink", "red", "yellow", "green",  "blue", 
            "purple", "navy", "coral", "actor", "baker", 
            "barber", "chef",  "cook", "doctor", "general", 
            "guard", "judge", "model", "nurse", "pilot"]

word_normal = ["astronaut", "interpreter", "strawberry", "watermelon", "netherlands", 
            "charcoal", "bodyguard", "entertainer", "firefighter", "hairdressor", 
            "hotelier", "ireland", "portugal", "elephant", "meerkat", 
            "penguin", "turtle", "england", "finland", "denmark", 
            "france", "poland", "turkey", "china", "japan", 
            "taiwan", "vietnam", "israel", "pakistan", "anchor", 
            "designer", "director", "editor", "farmer", "florist", 
            "hippopotamus", "lawyer", "reporter", "singer", "scientist", 
            "soldier", "teacher", "writer", "switzerland", "astronaut"]

word_hard = ["jazz", "quiz", "icebox", "rhythm", "ivory", 
            "jackpot", "topaz", "khaki", "cycle", "lucky", 
            "wave", "wizard", "oxygen", "galaxy", "pixel", 
            "zombie"]

title = pygame.image.load("title.png")
title_size = title.get_rect().size
title_width = title_size[0]
title_height = title_size[1]
title_x = screen_width / 2 - title_width / 2
title_y = title_height / 2

button_singleplay = pygame.image.load("button_singleplay.png")
button_singleplay_size = button_singleplay.get_rect().size
button_singleplay_width = button_singleplay_size[0]
button_singleplay_height = button_singleplay_size[1]
button_singleplay_x = 100
button_singleplay_y = title_height + screen_height / 4

button_multiplay = pygame.image.load("button_multiplay.png")
button_multiplay_size = button_multiplay.get_rect().size
button_multiplay_width = button_multiplay_size[0]
button_multiplay_height = button_multiplay_size[1]
button_multiplay_x = screen_width - 100 - button_multiplay_width
button_multiplay_y = title_height + screen_height / 4

difficulty_text = pygame.image.load("difficulty_0.png")
difficulty_text_size = difficulty_text.get_rect().size
difficulty_text_width = difficulty_text_size[0]
difficulty_text_height = difficulty_text_size[1]
difficulty_text_x = button_singleplay_x + button_singleplay_width / 2 - difficulty_text_width / 2
difficulty_text_y = button_singleplay_y + button_singleplay_height

attempt_image = pygame.image.load("attempt_0.png")
attempt_image_size = attempt_image.get_rect().size
attempt_image_width = attempt_image_size[0]
attempt_image_height = attempt_image_size[1]
attempt_image_x = 0
attempt_image_y = screen_height / 2 - attempt_image_height / 2

game_font = pygame.font.Font(None, 100)
input = ""
answer = ""
word = ""
missed = ""
attempt = 0
score = 0

running = True
while(running) :
    #메인 화면
    while scene == 0:
        title = pygame.image.load("title.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                scene = -1

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    if difficulty == 0:
                        word = random.choice(word_easy)
                    elif difficulty == 0:
                        word = random.choice(word_normal)
                    else:
                        word = random.choice(word_hard)
                    answer = str("_ "*len(word))
                    attempt = 0
                    mode = 0
                    scene = 2

                elif event.key == pygame.K_d:
                    attempt = 0
                    mode = 1
                    scene = 1

                elif event.key == pygame.K_s:
                    difficulty += 1
                    difficulty %= 3
                    difficulty_text = pygame.image.load("difficulty_"+str(difficulty)+".png")
        screen.fill((255, 255, 255))
        screen.blit(title, (title_x, title_y))
        screen.blit(button_singleplay, (button_singleplay_x, button_singleplay_y))
        screen.blit(button_multiplay, (button_multiplay_x, button_multiplay_y))
        screen.blit(difficulty_text, (difficulty_text_x, difficulty_text_y))

        pygame.display.update()
    
    while scene == 1:
        title = pygame.image.load("insert.png")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                scene = -1
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN and word.isalpha:
                    answer = str("_ "*len(word))
                    scene = 2

                elif event.key == pygame.K_BACKSPACE:
                    word = word[:-1]

                else:
                    input = event.unicode
                    if input.isalpha:
                        input = input.lower()
                        if input in alphabet:
                            word += input

        text_word = game_font.render((str(word)), True, (17, 17, 17))
        text_word_size = text_word.get_rect().size
        text_word_x = screen_width / 2  - text_word_size[0] / 2
        text_word_y = title_height + screen_height / 4

        screen.fill((255, 255, 255))
        screen.blit(title, (title_x, title_y))
        screen.blit(text_word, (text_word_x, text_word_y))
        pygame.display.update()
    
    while scene == 2:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                scene = -1

            elif event.type == pygame.KEYDOWN:
                input = event.unicode
                input = input.lower()

                if input in alphabet and not(input in missed):
                    if input in word:
                        score += 1000 - attempt*100
                        answerList = list(answer.replace(" ", ""))
                        for i in range(0, len(word)):
                            if word[i] == input:
                                answerList[i] = word[i]
                        answer = ""
                        for i in range(0, len(answerList)):
                            answer += answerList[i] + " "
                        
                        if not("_" in answer):
                            scene = 4

                    else:
                        attempt += 1
                        score -= 300
                        missed += input
                        missed += " "
                        if attempt > 9:
                            scene = 3
        

        attempt_image = pygame.image.load("attempt_"+str(attempt)+".png")

        text_answer = game_font.render((str(answer)), True, (17, 17, 17))
        text_answer_size = text_answer.get_rect().size
        text_answer_x = screen_width / 2
        text_answer_y = screen_height / 4

        text_missed = game_font.render((str(missed)), True, (17, 17, 17))
        text_missed_size = text_missed.get_rect().size
        text_missed_x = screen_width / 2
        text_missed_y = screen_height / 4 + text_answer_y + 50

        screen.fill((255, 255, 255))
        screen.blit(attempt_image, (attempt_image_x, attempt_image_y))
        screen.blit(text_answer, (text_answer_x, text_answer_y))
        screen.blit(text_missed, (text_missed_x, text_missed_y))
        pygame.display.update()

        while scene == 3:
            title = pygame.image.load("gameover.png")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    scene = -1

                elif event.type == pygame.KEYDOWN:
                    input = ""
                    answer = ""
                    word = ""
                    missed = ""
                    attempt = 0
                    score = 0
                    scene = 0
            
            text_word = game_font.render((str(word)), True, (17, 17, 17))
            text_word_size = text_word.get_rect().size
            text_word_x = screen_width / 2  - text_word_size[0] / 2
            text_word_y = title_height * 3/2 + 50
            screen.fill((255, 255, 255))
            screen.blit(title, (title_x, title_y))
            screen.blit(text_word, (text_word_x, text_word_y))

            pygame.display.update()

        while scene == 4:
            title = pygame.image.load("clear.png")
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    scene = -1

                elif event.type == pygame.KEYDOWN:
                    input = ""
                    answer = ""
                    word = ""
                    missed = ""
                    attempt = 0
                    score = 0
                    scene = 0
            
            text_word = game_font.render((str(word)), True, (17, 17, 17))
            text_word_size = text_word.get_rect().size
            text_word_x = screen_width / 2  - text_word_size[0] / 2
            text_word_y = title_height * 3/2 + 50
            if mode == 0:
                text_score = game_font.render(("Your Score: " + str(score)), True, (17, 17, 17))
                text_score_size = text_score.get_rect().size
                text_score_x = screen_width / 2  - text_score_size[0] / 2
                text_score_y = text_word_y + 100

            screen.fill((255, 255, 255))
            screen.blit(title, (title_x, title_y))
            screen.blit(text_word, (text_word_x, text_word_y))
            if mode == 0:
                screen.blit(text_score, (text_score_x, text_score_y))

            pygame.display.update()

pygame.quit()