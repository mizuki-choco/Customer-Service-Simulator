import pyxel
import random

pyxel.init(200, 200)

response1 = 35
response2 = 115
response3 = 15
response4 = 75
response5 = 135
complain = 15

score = 0
number = 0


class Clock:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c
        self.sec = 0
        self.min = 0

    def update(self):
        self.sec = pyxel.frame_count // 30
        self.min = self.sec // 60

    def draw(self):
        pyxel.text(self.x, self.y, "Time: %02d:%02d" % (self.min, self.sec % 60), self.c)
        #ここでタイマーを作った

class App:
    def __init__(self):
        self.clock = Clock(0, 0, 0)
        pyxel.run(self.update, self.draw)
        #この辺がなんかおかしい

    def update(self):
        global response1, response2, response3, response4, response5, complain, score, number
        self.clock.update()

    def draw(self):
        global response1, response2, response3, response4, response5, complain, score, number
        pyxel.cls(7)
        self.clock.draw() #タイマーの描画
        pyxel.rect(response1, 170, 50, 20, 14) #返事1の描画
        pyxel.rect(response2, 170, 50, 20, 14) #返事2の描画
        pyxel.rect(response3, 140, 50, 20, 11) #返事3の描画
        pyxel.rect(response4, 140, 50, 20, 11) #返事4の描画
        pyxel.rect(response5, 140, 50, 20, 11) #返事5の描画
        pyxel.rect(complain, 100, 170, 30, 13) #クレームの描画
        pyxel.text(165, 0, "SCORE:" + str(number), 3)

class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "correct_option": 0},
            {"question": "Which planet is known as the Red Planet?", "options": ["Earth", "Mars", "Jupiter", "Venus"], "correct_option": 1},
            {"question": "What is the largest mammal on Earth?", "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"], "correct_option": 1},
        ]
        self.current_question_index = 0
        self.score = 0

        pyxel.init(200, 150, "Quiz Game", fps=60)
        pyxel.mouse(True)

        pyxel.run(self.update, self.draw)

    def update(self):
        pass

    def draw(self):
        pyxel.cls(0)

        #質問の描画
        question = self.questions[self.current_question_index]["question"]
        pyxel.text(1, 10, question, 2)

        #選択肢の描画
        options = self.questions[self.current_question_index]["options"]
        for i, option in enumerate(options):
            pyxel.text(20, 40 + i * 20, f"{chr(65 + i)}. {option}", 2)

        #スコアの描画
        pyxel.text(10, 130, f"Score: {self.score}", 2)

        #マウスクリックで解答を選択する
        if pyxel.btnp(pyxel.KEY_SPACE):
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y

            #マウスが選択肢の中にあったらクリックしたとみなす
            for i in range(len(options)):
                if 20 <= mouse_x <= 180 and 40 + i * 20 <= mouse_y <= 60 + i * 20:
                    #解答が正解だった場合
                    if i == self.questions[self.current_question_index]["correct_option"]:
                        self.score += 1

                    #次の問題に移る
                    self.current_question_index += 1

                    #すべての問題に解答し終えた時
                    if self.current_question_index == len(self.questions):
                        pyxel.quit()

                    break


# アプリケーションの起動
App()
QuizGame()

#csvファイルを作る
#日本語フォントの入れ方