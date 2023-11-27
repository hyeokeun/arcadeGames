import random

class Game:
    def __init__(self):
        pass

    def start(self):
        pass

    def get_hint(self):
        pass

    def check_input(self, user_input):
        pass

    def play_again(self):
        pass

#틱택토게임
class TicTacToe(Game):
    def __init__(self):
        super().__init__()
        self.board = [" " for _ in range(9)]
        self.current_player = "X"
        self.game_over = False
        self.winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                                     (0, 3, 6), (1, 4, 7), (2, 5, 8),
                                     (0, 4, 8), (2, 4, 6)]

    def draw_board(self):
        for i in range(0, 9, 3):
            print(" | ".join(self.board[i:i + 3]))
            if i < 6:
                print("-" * 9)

    def check_winner(self, player):
        for combo in self.winning_combinations:
            if all(self.board[i] == player for i in combo):
                return True
        return False

    def check_draw(self):
        return " " not in self.board

#게임 방법 설명
    def start(self):
        print("틱택토 게임을 시작합니다.")
        print("게임 보드의 위치를 선택하려면 1부터 9까지의 번호를 입력하세요.")
        print("게임 보드의 위치는 다음과 같습니다:")
        print(" 1 | 2 | 3 ")
        print("-----------")
        print(" 4 | 5 | 6 ")
        print("-----------")
        print(" 7 | 8 | 9 ")
        print("게임은 각 플레이어가 번갈아가며 보드의 빈 공간에 'X' 또는 'O'를 표시하여 이기는 쪽을 결정합니다.")

        while not self.game_over:
            self.draw_board()
            print(f"현재 플레이어: {self.current_player}")
            choice = input("원하는 위치를 선택하세요 (1-9): ")

            if not choice.isdigit() or int(choice) < 1 or int(choice) > 9 or self.board[int(choice) - 1] != " ":
                print("잘못된 입력입니다. 다시 시도하세요.")
                continue

            choice = int(choice) - 1
            self.board[choice] = self.current_player

            if self.check_winner(self.current_player):
                self.draw_board()
                print(f"{self.current_player} 플레이어가 승리했습니다!")
                self.game_over = True
            elif self.check_draw():
                self.draw_board()
                print("무승부입니다!")
                self.game_over = True
            else:
                self.current_player = "O" if self.current_player == "X" else "X"

        self.play_again()

#다른게임 참여 여부
    def play_again(self):
        play_again = input("다른 게임을 하시겠습니까? (yes/no): ")
        if play_again.lower() == "yes":
            self.__init__()  # 게임을 초기화하여 다시 시작합니다.
            self.start()
        else:
            print("게임을 종료합니다. 감사합니다.")

#숫자 추측 게임
class GuessTheNumber(Game):
    def __init__(self):
        super().__init__()
        self.secret_number = random.randint(0, 100000)
        self.attempts = 0
        self.hint_count = 3
        self.max_attempts = 20
        self.min_range = 0
        self.max_range = 100000

#힌트기능
    def get_hint(self):
        hint_type = random.randint(1, 3)

        if hint_type == 1:
            print(f"힌트: 정답은 {self.min_range}과 {self.max_range} 사이에 있습니다.")
        elif hint_type == 2:
            num_str = str(self.secret_number)
            digit_position = random.randint(0, len(num_str) - 1)
            print(f"힌트: 정답 숫자의 {digit_position + 1}번째 자릿수는 {num_str[digit_position]}입니다.")
        else:
            num_str = str(self.secret_number)
            revealed_digit_position = random.randint(0, len(num_str) - 1)
            revealed_digit = num_str[revealed_digit_position]
            print(f"힌트: 정답 숫자 중 하나는 {revealed_digit}입니다.")

    def start(self):
        print("게임을 시작합니다. 0부터 100,000까지의 숫자 중 하나를 맞춰보세요.")
        print(f"힌트를 사용하려면 '힌트'라고 입력하세요.")

        while self.attempts < self.max_attempts:
            try:
                user_input = input("명령어를 입력하거나 추측한 숫자를 입력하세요: ")

                if user_input.lower() == "힌트" and self.hint_count > 0:
                    self.get_hint()
                    self.hint_count -= 1
                    print(f"남은 힌트 횟수: {self.hint_count}")
                    continue

                user_guess = int(user_input)
                self.attempts += 1

# 범위알려주는 기능
                if user_guess < self.min_range or user_guess > self.max_range:
                    print(f"범위를 벗어난 숫자입니다. 현재 범위: {self.min_range}-{self.max_range}")
                    continue

                if user_guess < self.secret_number:
                    print(f"너무 작습니다. 정답은 더 큽니다. 다시 시도하세요.")
                    self.min_range = user_guess + 1
                elif user_guess > self.secret_number:
                    print(f"너무 큽니다. 정답은 더 작습니다. 다시 시도하세요.")
                    self.max_range = user_guess - 1
#몇번째에 맞췄는지 알려주는 코드                
                else:
                    print(f"축하합니다! {self.secret_number}를 {self.attempts}번 만에 맞추셨습니다!")
                    break

                print(f"사용자가 지금까지 입력한 수와 범위로 정답이 가능한 범위는 {self.min_range}부터 {self.max_range}까지 입니다.")

            except ValueError:
                print("올바른 숫자나 명령어를 입력하세요.")

        self.play_again()

    def play_again(self):
        play_again = input("다른 게임을 하시겠습니까? (yes/no): ")
        if play_again.lower() == "yes":
            self.__init__()  # 게임을 초기화하여 다시 시작합니다.
            self.start()
        else:
            print("게임을 종료합니다. 감사합니다.")

#초기 게임 모드 선택
def choose_game_mode():
    mode = input("게임 모드를 선택하세요 (1: 숫자 추측, 2: 틱택토): ")

    if mode == "1":
        guess_game = GuessTheNumber()
        guess_game.start()
    elif mode == "2":
        tic_tac_toe_game = TicTacToe()
        tic_tac_toe_game.start()
    else:
        print("올바른 모드를 선택하세요 (1 또는 2).")

choose_game_mode()
