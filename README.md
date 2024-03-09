[![Maintainability](https://api.codeclimate.com/v1/badges/c0c0bd41b3105ab57b32/maintainability)](https://codeclimate.com/github/chifcrow/python-project-49/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/c0c0bd41b3105ab57b32/test_coverage)](https://codeclimate.com/github/chifcrow/python-project-49/test_coverage)
<a href="https://github.com/chifcrow/python-project-49/actions"><img src="https://github.com/chifcrow/python-project-49/workflows/hexlet-check/badge.svg" /></a>

# Добро пожаловать в серию образовательных мини-игр "Brain Games".

## <span style="color:#266599">Установка игры</span>
```
pip install --user git+https://github.com/chifcrow/python-project-49.git
```
## <span style="color:#266599">Знакомство и приветствие</span>:

### <span style="color:blue">_Запуск игры_</span>:
```
$ brain_games
```
## <span style="color:#266599">Игра "Калькулятор"</span>:

### <span style="color:blue">_Описание игры_</span>:
Игра "Калькулятор" представляет собой математическую викторину, где пользователю предлагается решить случайное математическое выражение. 

### <span style="color:blue">_Запуск игры_</span>:
```
$ brain_calc
```
### <span style="color:blue">_Пример игрового процесса_</span>:
```
Welcome to the Brain Games!<br/>
May I have your name? Sam<br/>
Hello, Sam!<br/>
What is the result of the expression?<br/>
Question: 4 + 10<br/>
Your answer: 14<br/>
Correct!<br/>
Question: 25 - 11<br/>
Your answer: 14<br/>
Correct!<br/>
Question: 25 * 7<br/>
Your answer: 175<br/>
Correct!<br/>
Congratulations, Sam!
```
Если вы введете правильный ответ, игра продолжится и вам будут представлены новые числа. Вам необходимо дать правильные ответы на три вопроса подряд, чтобы выиграть:<br/>
В случае неправильного ответа, игра завершится, и вы увидите следующее сообщение:<br/>
```
Question: 8 + 6
Your answer: 11
'11' is wrong answer ;(. Correct answer was '14'.
Let's try again, Sam!
```
## <span style="color:#266599">Игра "Проверка на чётность"</span>:

### <span style="color:blue">_Описание игры_</span>:
Игра "Проверка на чётность" требует от пользователя определить, является ли показанное ему число чётным. Пример игрового процесса:

### <span style="color:blue">_Запуск игры_</span>:
```
$ brain_even
```
### <span style="color:blue">_Пример игрового процесса_</span>:
```
Welcome to the Brain Games!<br/>
May I have your name? Bill<br/>
Hello, Bill!<br/>
Answer "yes" if the number is even, otherwise answer "no".<br/>
Question: 15<br/>
Your answer: yes<br/>
'yes' is wrong answer ;(. Correct answer was 'no'.<br/>
Let's try again, Bill!
```
Если вы введете правильный ответ, игра продолжится и вам будут представлены новые числа. Вам необходимо дать правильные ответы на три вопроса подряд, чтобы выиграть:<br/>
В случае неправильного ответа, игра завершится, и вы увидите следующее сообщение:<br/>
```
Question: 15<br/>
Your answer: yes<br/>
'yes' is wrong answer ;(. Correct answer was 'no'.<br/>
Let's try again, Bill!
```
## <span style="color:#266599">Игра "Наибольший общий делитель" (НОД)</span>:

### <span style="color:blue">_Описание игры_</span>:

Игра "Наибольший общий делитель (НОД)" — это увлекательная математическая игра, в которой ваша задача найти наибольший общий делитель двух случайно выбранных чисел.

### <span style="color:blue">_Запуск игры_</span>:
```
$ brain_gcd
```
### <span style="color:blue">_Пример игрового процесса_</span>:
```
Welcome to the Brain Games!<br/>
May I have your name? Sam<br/>
Hello, Sam!<br/>
Find the greatest common divisor of given numbers.<br/>
Question: 25 50<br/>
Your answer: 25<br/>
Correct!
```
Если вы введете правильный ответ, игра продолжится и вам будут представлены новые числа. Вам необходимо дать правильные ответы на три вопроса подряд, чтобы выиграть:<br/>
```
Question: 100 52<br/>
Your answer: 4<br/>
Correct!<br/>
Question: 3 9<br/>
Your answer: 3<br/>
Correct!<br/>
Congratulations, Sam!<br/>
```
В случае неправильного ответа, игра завершится, и вы увидите следующее сообщение:<br/>
```
Question: 25 50<br/>
Your answer: 1<br/>
'1' is wrong answer ;(. Correct answer was '25'.<br/>
Let's try again, Sam!<br/>
```
Попробуйте игру и проверьте свои навыки нахождения НОД!

## <span style="color:#266599">Игра "Арифметическая прогрессия"</span>:

### <span style="color:blue">_Описание игры_</span>:

В игре "Арифметическая прогрессия" вам будет представлен ряд чисел, формирующих арифметическую прогрессию, где одно из чисел заменено на две точки. Ваша задача — определить это пропущенное число.

### <span style="color:blue">_Запуск игры_</span>:
```
$ brain_progression
```
### <span style="color:blue">_Пример игрового процесса_</span>:
```
Welcome to the Brain Games!<br>
May I have your name? Sam<br>
Hello, Sam!<br>
What number is missing in the progression?<br>
Question: 5 7 9 11 13 .. 17 19 21 23<br>
Your answer: 15<br>
Correct!<br>
```
Если вы введете правильный ответ, игра продолжится и вам будут представлены новые числа. Вам необходимо дать правильные ответы на три вопроса подряд, чтобы выиграть:<br/>
В случае неправильного ответа, игра завершится, и вы увидите следующее сообщение:<br/>

```
Question: 5 7 9 11 13 .. 17 19 21 23<br>
Your answer: 1<br>
'1' is wrong answer ;(. Correct answer was '15'.<br>
Let's try again, Sam!<br>
```
## <span style="color:#266599">Игра "Простое ли число?"</span>:

### <span style="color:blue">_Описание игры_</span>:

В игре "Простое ли число?" вам будет представлено число, и вам нужно определить, является ли оно простым. Ответьте "yes", если число простое, и "no" — если нет.

### <span style="color:blue">_Запуск игры_</span>:
```
$ brain_prime
```
### <span style="color:blue">_Пример игрового процесса_</span>:
```
Welcome to the Brain Games!
May I have your name? Sam
Hello, Sam!
Answer "yes" if given number is prime. Otherwise answer "no".
Question: 7
Your answer: yes
Correct!
```
Если вы введете правильный ответ, игра продолжится и вам будут представлены новые числа. Вам необходимо дать правильные ответы на три вопроса подряд, чтобы выиграть:<br/>
В случае неправильного ответа, игра завершится, и вы увидите следующее сообщение:<br/>
```
Question: 4
Your answer: yes
'yes' is wrong answer ;(. Correct answer was 'no'.
Let's try again, Sam!
```
### <span style="color:blue">_Демонстрация игры_</span>:
[![asciicast](https://asciinema.org/a/646149.svg)](https://asciinema.org/a/646149)


