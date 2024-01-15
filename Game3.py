import pyxel
import random

pyxel.init(200, 200)
pyxel.sound(0).set(notes = 'A2C3', tones='TT', volumes='33', effects='NN', speed=10)
pyxel.sound(1).set(notes='C3A2', tones='TT', volumes='33', effects='NN', speed=10)

response1 = 13
response2 = 13
response3 = 13
response4 = 13
response5 = 13
complain = 15
score = 0

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
        pyxel.mouse(True) #ここでマウスカーソルを作った
        self.clock = Clock(0, 0, 0)
        self.quizgame = QuizGame() #クイズゲームのインスタンスが生成される
        self.game_over = False #Trueになったらゲーム終了
        pyxel.run(self.update, self.draw)

    def update(self):
        global response1, response2, response3, response4, response5, complain, score, number
        self.clock.update()

        if self.clock.sec >= 10:
            self.game_over = True
        #30秒経過したらゲーム終了

    def draw(self):
        global response1, response2, response3, response4, response5, complain, score, number
        pyxel.cls(6)
        self.clock.draw() #タイマーの描画
        pyxel.rect(response1, 75, 185, 15, 14) #返事1の描画
        pyxel.rect(response2, 95, 185, 15, 11) #返事2の描画
        pyxel.rect(response3, 115, 185, 15, 14) #返事3の描画
        pyxel.rect(response4, 135, 185, 15, 11) #返事4の描画
        pyxel.rect(response5, 155, 185, 15, 14) #返事5の描画
        pyxel.rect(complain, 35, 178, 30, 13) #クレームの描画

        if self.game_over:
            pyxel.text(80, 10, "GAME OVER!!!", 7) #30秒経ったら文字表示
            pyxel.text(70, 30, f"Your Score: {score}", 7) #スコアの表示を追加
        else:
            self.quizgame.draw() #QuizGameのdrawを呼び出す

class QuizGame:
    def __init__(self):
        self.questions = [
            {"question": "The air conditioning is too strong.", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer A:", "question2": "I can't stand it anymore!", "correct_option": 0},
            {"question": "The food is stale!", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer B:", "question2": "I will never come back to this restaurant!", "correct_option": 1},
            {"question": "The table is too small.", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer C:", "question2": "Please give a bigger space for our seats.", "correct_option": 0},
            {"question": "I still havent received my order!", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer D:", "question2": "I am hungry and can't stand it. Hurry up!", "correct_option": 2},
            {"question": "I did not order this salad.", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer E:", "question2": "I ordered pasta. Isn't this the neighbor's?", "correct_option": 2},
            {"question": "This rare steak is very good!", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer F:", "question2": "May I talk to the Chef, please?", "correct_option": 4},
            {"question": "Put your hands up!", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer ???:", "question2": "Hand over all valuables!", "correct_option": 3},
            {"question": "Is there a pizza that doesn't contain meat?", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer G:", "question2": "I'm a vegetarian.", "correct_option": 1},
            {"question": "Let me speak with your manager.", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer H:", "question2": "The cuisine is excellent.", "correct_option": 4},
            {"question": "I found a bug in my food!", "options": ["I am sorry for the inconvenience you faced.", "I'll bring you another one right away.", "I'll see about your order right away.", "I'll call the police.", "Thank you so much!"], "customer_name": "Customer I:", "question2": "It's disgusting!!", "correct_option": 1}
        ]
        random.shuffle(self.questions) #質問リストをランダムにシャッフル
        self.current_question_index = 0
        self.score = 0

    def update(self):
        pass

    def draw(self):
        
        #客の詳細の描画
        customer_name = self.questions[self.current_question_index]["customer_name"]
        pyxel.text(20, 40, customer_name, 0)

        #質問の描画
        question = self.questions[self.current_question_index]["question"]
        pyxel.text(20, 50, question, 0)

        #質問の続きの描画
        question = self.questions[self.current_question_index]["question2"]
        pyxel.text(20, 57, question, 0)

        #選択肢の描画
        options = self.questions[self.current_question_index]["options"]
        for i, option in enumerate(options):
            pyxel.text(15, 80 + i * 20, f"{chr(65 + i)}. {option}", 0)

        #スコアの描画
        pyxel.text(165, 0, f"SCORE: {self.score}", 0)

        #マウスクリックで解答を選択する
        if pyxel.btnp(pyxel.KEY_SPACE):
            mouse_x = pyxel.mouse_x
            mouse_y = pyxel.mouse_y

            #マウスが選択肢の中にあったらクリックしたとみなす
            for i in range(len(options)):
                if 20 <= mouse_x <= 180 and 80 + i * 20 <= mouse_y <= 100 + i * 20:
                    #解答が正解だった場合
                    if i == self.questions[self.current_question_index]["correct_option"]:
                        self.score += 1
                        pyxel.play(0,1)

                    #次の問題に移る
                    self.current_question_index += 1

                    #すべての問題に解答し終えた時
                    if self.current_question_index == len(self.questions):
                        pyxel.quit()

                    break

App()
