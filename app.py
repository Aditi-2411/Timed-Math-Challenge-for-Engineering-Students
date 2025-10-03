from flask import Flask, render_template, request, redirect, url_for
import random
import time

app = Flask(__name__)
app = Flask(__name__, static_url_path='/static')


# Sample math questions with options, correct answers, and explanations
# Separate questions based on topics
questions_by_topic = {
    'laplaceTransform': [
        {
            "question": "➢Find the Laplace transform of t e^t sin2t cost",
            "options": ["<br><u><span class='question'>    3(s+1)  </span> </u> <span class='question'>   +  </span> <u> <span class='question'>  (s-1) </span></u> <br> <span class='question'>[s²+2s+10]²  </span>  <span class='question'>    [s²-2s+20]²    </span>", "<br><u><span class='question'>    3(s-1)  </span> </u> <span class='question'>   +  </span> <u> <span class='question'>  (s+1) </span></u> <br> <span class='question'>[s²-2s+10]²  </span>  <span class='question'>    [s²-2s-2]²    </span>", "<br><u><span class='question'>    3(s-1)  </span> </u> <span class='question'>   +  </span> <u> <span class='question'>  (s-1) </span></u> <br> <span class='question'>[s²-2s+10]²  </span>  <span class='question'>    [s²-2s+2]²    </span>"],
            "answer": "<br><u><span class='question'>    3(s-1)  </span> </u> <span class='question'>   +  </span> <u> <span class='question'>  (s-1) </span></u> <br> <span class='question'>[s²-2s+10]²  </span>  <span class='question'>    [s²-2s+2]²    </span>",
            "explanation": "<br><br><br><b>Solution:</b><br>L[sin2t cost] = L[<u>1</u> (sin3t + sint)] = <u>1</u>L[sin3t + sint] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2<br><br>L[sin2t cost] = <u>1</u> [<u>&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;[s² + 9  &nbsp; s² + 1]<br><br>L[sin2t cost] = (-1)^n <u>1</u> <u>&nbsp;d&nbsp;</u> [<u>&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = <u>-1</u> [3{<u>&nbsp;&nbsp;&nbsp;-2s&nbsp;&nbsp;&nbsp;</u>} - {<u>&nbsp;&nbsp;&nbsp;2s&nbsp;&nbsp;&nbsp;</u>}]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 ds [s² + 9  &nbsp; s² + 1 ] &nbsp; 2 &nbsp;[ {(s² + 9)²} &nbsp;&nbsp;&nbsp;{(s² + 9)²}]<br><br>L[sin2t cost] = <u>1</u> [<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>] = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;&nbsp;</u> = φ(s)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;[(s² + 9)²  &nbsp;&nbsp; (s² + 1)²]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 9)² &nbsp; (s² + 9)²<br><br>L[t e^tsin2t cost] = φ(s - a)<br>By First Shifting Theorem;<br><br>L[t e^tsin2t cost] = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3(s - 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s - 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3(s - 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s - 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² - 1)² + 9²]&nbsp;&nbsp;&nbsp;[(s² - 1)² + 1²]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s²-2s+10]²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s²-2s+2]²<br><br>L[t e^tsin2t cost] = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3(s - 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s - 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s²-2s+10]²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s²-2s+2]²",
        },
        {
            "question": "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∞ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>➢Evaluate ∫ e^-t (∫ u² sinh u cosh u du) dt using Laplace Transform.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 ",
            "options": ["<br>-<u>14</u><br><span class='question'>  27</span>", "<br>-<u>14</u><br><span class='question'>  23</span>", "<br><u>14</u><br><span class='question'>  27</span>"],
            "answer": "<br>-<u>14</u><br><span class='question'>  27</span>",
            "explanation": "<br><br><br><b>Solution:</b><br>L[sinh u cosh u] = <u>1</u>[2 sinh u cosh u] = <u>1</u>L[sinh 2u] = <u>1</u>[<u>&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;[s² - 2²]<br><br>L[u² sinh u cosh u] = <u>d²</u> &nbsp;(<u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ds² (s² - 4)<br><br><u>d</u> &nbsp;(<u>&nbsp;&nbsp;-2s&nbsp;&nbsp;</u>) = <u>2(3s² + 4)</u><br>ds (s² - 4)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² - 4)³<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>L[∫ u² sinh u cosh u du] = <u>2(s² + 4)</u><br>&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s(s² - 4)³<br><br>Put s = 1, we get<br>∞&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>∫ e^-t (∫ u² sinh u cosh u du)dt = <u>2(3 + 4)</u> = -<u>14</u><br>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1(1 - 4)³&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27",
        },
        {
            "question": "➢Find the Laplace Transform of <u>1</u> e^-t sint<br> <span class='question'>                                                      t</span>",
            "options": ["<br>cot^(-1)(s + 1)", "<br>tan(s + 1)", "<br>cot(s + 1)"],
            "answer": "<br>cot^(-1)(s + 1)",
            "explanation": "<br><br><br><b>Solution:</b><br> L[sin t] = <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 1)<br>By First Shifting Theorem,<br>L[e^-t sin t] = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s + 1)² + 1<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∞<br>L[<u>1</u> e^-t sin t] = ∫ <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> ds<br>&nbsp;&nbsp;&nbsp;&nbsp;t&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s &nbsp;(s + 1)² + 1<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∞<br>[tan^-1 (s + 1)]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;π<br><br>[tan^-1 (∞) - tan^-1 (s + 1)]<br><br><u>π</u> - tan^-1 (s + 1)<br> 2<br><br>cot^-1 (s + 1)",
        },
        {
            "question": "<span class='question'>                                                            ∞</span><br>➢Using Laplace Transform evaluate ∫ e^-t (1 + 2t - t² + t³)H(t - 1)dt<br><span class='question'>                                                            0</span>",
            "options": ["<br><u>12</u><br><span class='question'> e</span>", "<br><u>16</u><br><span class='question'> e</span>", "<br><u>16</u><br><span class='question'> e²</span>"],
            "answer": "<br><u>16</u><br><span class='question'> e</span>",
            "explanation": "<br><br><br><b>Solution:</b><br>f(t) = 1 + 2t - t² + t³ &nbsp;&nbsp;&nbsp;&nbsp; ;a = 1<br><br>= f(t + 1) = 1 + 2(t + 1) - (t + 1)² + (t + 1)³<br><br>= 1 + 2t + 2 - (t² + 2t + 1) + t³ + 3t² + 3t + 1<br><br>= t³ + 2t² + 3t + 3<br><br>L[f(t + 1)] = L[t³ + 2t² + 3t + 3]<br><br>= <u>3!</u> + 2.<u>2!</u> + <u>3</u> + <u>3</u><br>&nbsp;&nbsp;&nbsp;s⁴ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp; s <br><br>&nbsp;&nbsp;&nbsp;&nbsp;We know, L[f(t)H(t-a)] = e^-as L[f(t+a)]<br>Substituting the value of L[f(t+a)] in above equation we get<br><br>L[(1 + 2t - t² + t³)H(t - 1)] = e^-as  [<u>3!</u> + 2.<u>2!</u> + <u>3</u> + <u>3</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s⁴ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp; s]<br><br> ∞<br>∫ e^-st (1 + 2t - t² + t³)H(t - 1)dt = e^-s  [<u>3!</u> + 2.<u>2!</u> + <u>3</u> + <u>3</u>]<br>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s⁴ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp; s]<br>Putting s=1 n the above equation;<br>∞<br>∫ e^-t (1 + 2t - t² + t³)H(t - 1)dt = e^-1  [<u>3!</u> + 2.<u>2!</u> + <u>3</u> + <u>3</u>]<br>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s⁴ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp; s]<br><br>= e^-1[6 + 4 + 3 + 3] = <u>16</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e",
        },
        {
            "question": "➢Find the Laplace Transform of t sin at ",
            "options": ["<br><u><span class='question'>    2as     </span></u><br><span class='question'> (s² + a²)²</span>", "<br><u><span class='question'>    -2as     </span></u><br><span class='question'> (s² + a²)²</span>", "<br><u><span class='question'>    2as     </span></u><br><span class='question'> (s² - a²)²</span>"],
            "answer": "<br><u><span class='question'>    2as     </span></u><br><span class='question'> (s² + a²)²</span>",
            "explanation": "<br><br><br><b>Solution:</b><br>L(t sin at) = (-1). <u>d</u> [L(sin at)]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ds<br><br>= -<u>d</u><u>       ( &nbsp;&nbsp;&nbsp;&nbsp;a       &nbsp;&nbsp;&nbsp;)</u><br>&nbsp;&nbsp;&nbsp;&nbsp;ds<span class='question'> (s² + a²)</span><br><br>= <u><span class='question'>    2as     </span></u><br><span class='question'> (s² + a²)²</span>",
        },
        {
            "question": "<span class='question'>                                                            ∞</span><br>➢Using Laplace Transform evaluate ∫ e^-t (1 + 3t + t²)H(t - 2)dt<br><span class='question'>                                                            0</span>",
            "options": ["<br><u>20</u><br><span class='question'> e²</span>", "<br><u>20</u><br><span class='question'> e</span>", "<br><u>16</u><br><span class='question'> e²</span>"],
            "answer": "<br><u>20</u><br><span class='question'> e²</span>",
            "explanation": "<br><br><br>Solution:<br>f(t) = 1 + 3t + t² &nbsp;&nbsp;&nbsp;&nbsp; ;a = 2<br><br>= f(t + 1) = 1 + 3(t + 2) + (t + 2)²<br><br>= 1 + 3t + 6 - (t² + 4t + 4)<br><br>= t² + 7t + 11<br><br>L[f(t + 1)] = L[t² + 7t + 11]<br><br>= <u>2!</u> + <u>7.1!</u> + <u>11</u><br>&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; s<br><br>&nbsp;&nbsp;&nbsp;&nbsp;We know, L[f(t)H(t-a)] = e^-as L[f(t+a)]<br>Substituting the value of L[f(t+a)] in above equation we get<br><br>L[(1 + 3t + t²)H(t - 2)] = e^-2s  [<u>2!</u> + <u>7.1!</u> + <u>11</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; s]<br><br>∞<br>∫ e^-st (1 + 3t + t²)H(t - 2)dt = e^-2s  [<u>2!</u> + <u>7.1!</u> + <u>11</u>]<br>0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;s³&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    s²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; s]<br>Putting s=1 n the above equation;<br><br><span class='question'>            ∞</span><br>∫ e^-t (1 + 3t + t²)H(t - 2)dt = e^-2  [<u>2!</u> + <u>7.1!</u> + <u>11</u>]<br><span class='question'>                                                            0</span> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1]<br><br>= e^-2[2 + 7 + 11] = <u>20</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;e²",
        },
        {
            "question": "➢Find the Laplace transform of t sin³ t",
            "options": ["<br>24 .  <u><span class='question'>       s(s - 25)        </span></u><br><span class='question'>    (s² + 1²)² (s² + 9)² </span>", "<br>24 .  <u><span class='question'>       s(s + 5)        </span></u><br><span class='question'>    (s² + 1²)² (s² + 9)² </span>", "<br>20 .  <u><span class='question'>       s(s - 5)        </span></u><br><span class='question'>    (s² - 1²)² (s² - 9)² </span>"],
            "answer": "<br>24 .  <u><span class='question'>       s(s + 5)        </span></u><br><span class='question'>    (s² + 1²)² (s² + 9)² </span>",
            "explanation": "<br><br><br><b>Solution:</b><br>sin3t = 3 sint - 4 sin³t<br><br>L[sin³ t] = <u> 1 </u>[L(3 sin t) - L(sin 3t)]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4<br><br>L[sin³ t] = -<u> 3 </u> &nbsp;&nbsp;<u> d </u>[<u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u> - <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;ds&nbsp;&nbsp;[s²+1 - s²+9]<br><br>L[sin³ t] = -<u> 3 </u> &nbsp;&nbsp;[<u>&nbsp;&nbsp;&nbsp;&nbsp;2s&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;&nbsp;&nbsp;2s&nbsp;&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;[ (s²+1)² - (s²+9)² ]<br><br>L[sin³ t] = <u> 3s </u> &nbsp;&nbsp;[<u>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;</u> - <u>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;[(s²+1)² - (s²+9)²]<br><br>L[sin³ t] = <u> 3s </u> [ <u>s⁴ + 18s² + 81 - s⁴ - 2s² - 1</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 &nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s²+1)² - (s²+9)²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br><br>L[sin³ t] = <u> 3s </u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;16(s + 5)&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2 &nbsp;&nbsp;&nbsp;(s²+1)² - (s²+9)²&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>= 24 .  <u><span class='question'>       s(s + 5)        </span></u><br><span class='question'>    (s² + 1²)² (s² + 9)² </span>",
        },
        {
            "question": "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t t t<br>➢Find L [∫ ∫ ∫ t sin t(dt)³]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 0 0",
            "options": ["<br><u><span class='question'>     -2      </span></u><br><span class='question'> s²(s² + 1)² </span>", "<br><u><span class='question'>     2      </span></u><br><span class='question'> s²(s² - 1)² </span>", "<br><u><span class='question'>     2      </span></u><br><span class='question'> s²(s² + 1)² </span>"],
            "answer": "<br><u><span class='question'>     2      </span></u><br><span class='question'> s²(s² + 1)² </span>",
            "explanation": "<br><br><br><b>Solution:</b><br>By the corollary, <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t t t<br>L [∫ ∫ ∫ t sin t(dt)³] = <u> 1 </u> L[t sint]<br>&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³<br><br>L[t sint ] = <u>&nbsp;&nbsp;&nbsp;&nbsp;2s&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 1)²<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t t t<br> L [∫ ∫ ∫ t sin t(dt)³] = <u> 1 </u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2s&nbsp;&nbsp;&nbsp;&nbsp;</u> = <u>&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;0 0 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;(s² + 1)² &nbsp;  s²(s² + 1)²",
        },
        {
            "question": "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>➢Find the Laplace Transform of t ∫ e^-4u sin 3u du<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0",
            "options": ["<br><u><span class='question'> 3(3s² - 16s + 25)  </span></u><br><span class='question'> (s³ + 8s² - 25)² </span>", "<br><u><span class='question'> 3(3s² + 16s + 25)  </span></u><br><span class='question'> (s³ + 8s² + 25)² </span>", "<br><u><span class='question'> 3(3s² + 16s - 25)  </span></u><br><span class='question'> (s³ - 8s² + 25)² </span>"],
            "answer": "<br><u><span class='question'> 3(3s² + 16s + 25)  </span></u><br><span class='question'> (s³ + 8s² + 25)² </span>",
            "explanation": "<br><br><br><b>Solution:</b><br>We have L[sin 3u] = <u>&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s² + 9<br><br>L(e^-4u sin 3u) = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s + 4)² + 9<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>L[ ∫ e^-4u sin 3u du] = <u>1</u>. <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;(s + 4)² + 9<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>L[ ∫ e^-4u sin 3u du] = (-1)<u>d</u>. [<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ds&nbsp;[s³ + 8s² + 25s] <br><br>=<u><span class='question'> 3(3s² + 16s + 25)  </span></u><br><span class='question'> (s³ + 8s² + 25)² </span>",
        },
        {
            "question": "&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∞<br>➢Find ∫ e^-3t t cost dt<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0",
            "options": ["<br><u>-14</u><br><span class='question'> 27</span>", "<br><u>2</u><br><span class='question'> 15</span>", "<br><u>2</u><br><span class='question'> 25</span>"],
            "answer": "<br><u>2</u><br><span class='question'> 25</span>",
            "explanation": "<br><br><br><b>Solution:</b><br>∞<br>∫ e^-3t t cost dt = L(t cos t) = -<u>d</u>L(cos t)<br>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;ds<br><br>-<u>d</u>[<u>&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;&nbsp;</u>] = -[<u>(s² + 1) - s.2s</u>] = <u>s² - 1</u> <br> ds [s² + 1]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;(s² + 1)²&nbsp;&nbsp;&nbsp;] &nbsp;&nbsp;(s² + 1)³<br><br>Putting s = 3, <br>∞<br> ∫ e^-3t t cost dt = <u>&nbsp;8&nbsp;</u> = <u>&nbsp;2&nbsp;</u><br>0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100&nbsp;&nbsp;&nbsp;&nbsp;25",
        },
        
    ],
    'InverseLaplaceTransform': [
        {
            "question": "➢Find the Inverse Laplace Transfom <u> &nbsp;&nbsp;s + 2&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s²(s + 3)",
            "options": ["<br><u> 1 </u> + <u> 2t </u> - <u> 1 </u> e^-3t <br><span class='question'>6     3    3</span>", "<br><u> 1 </u> - <u> 2t </u> - <u> 1 </u> e^-3t <br><span class='question'>9     3    9</span>", "<br><u> 1 </u> + <u> 2t </u> - <u> 1 </u> e^-3t <br><span class='question'>9     3    9</span>"],
            "answer": "<br><u> 1 </u> + <u> 2t </u> - <u> 1 </u> e^-3t <br><span class='question'>9     3    9</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><u>&nbsp;&nbsp;s + 2&nbsp;&nbsp;</u> = <u>A</u> + <u>B</u> + <u>&nbsp;&nbsp;C&nbsp;&nbsp;</u> <br> s²(s + 3) &nbsp;&nbsp;&nbsp;s &nbsp;&nbsp;&nbsp;s²&nbsp;&nbsp;&nbsp; s + 3<br><br>s + 2 = As²(s + 3) + B(s + 3) + Cs²<br>Put s = 0;<br>2 = B(3) <br>=<u>2</u>&nbsp;<br>&nbsp;&nbsp;3<br>Put s = -3;<br>-1 = C(-3)²<br> C = -<u>1</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9<br>Comparing coefficient of s² on both sides;<br>0 = A + C<br> A = <u>1</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9<br><br>L^-1[<u>&nbsp;&nbsp;s + 2&nbsp;&nbsp;</u>] = <u>1</u>L^-1 [<u>1</u>] + <u>2</u>L^-1[<u>1</u>] - <u>1</u>L^-1 [<u>&nbsp;&nbsp;1&nbsp;&nbsp;</u>] = <u>1</u>(1) + <u>2</u>t - <u>1</u>e^-3t<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [s²(s + 3)] &nbsp;&nbsp;&nbsp;9 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s] &nbsp;&nbsp;&nbsp;&nbsp;3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s²]&nbsp;&nbsp;&nbsp; 9 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s + 3] &nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3 &nbsp;&nbsp;&nbsp;&nbsp;9<br><br>L^-1[<u>&nbsp;&nbsp;s + 2&nbsp;&nbsp;</u>] = <u>1</u> + <u>2</u>t - <u>1</u>e^-3t<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s²(s + 3)]&nbsp;&nbsp;&nbsp;&nbsp; 9 &nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp; 9",
        },
        {
            "question": "➢Find the Inverse Laplace Transform by convolution Theorem <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 1)(s² + 9)",
            "options": ["<br><u>1</u>[3 sint - sin 3t]<br>24", "<br><u>1</u>[3 sint + sin 3t]<br>24", "<br><u>1</u>[3 sint - sin 3t]<br>8"],
            "answer": "<br><u>1</u>[3 sint - sin 3t]<br>24",
            "explanation": "<br><br><br><b>Solution:</b><br>Let φ1(s) = <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u> and φ2(s) = <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; (s² + 1) &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  (s² + 9)<br><br>L^-1[φ1(s)] = L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;</u>] = sint <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1)]<br><br>L^-1[φ2(s)] = L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;</u>] = <u>1</u> sin 3t <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 9)] &nbsp;&nbsp;3<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = ∫ sin u.<u>1</u>sin3(1 - u)du<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) (s² + 9)] &nbsp;&nbsp; 0  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  3<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = -<u>1</u> ∫ cos[(1 - 3)u + 3t] - cos[(4u - 3t)]du<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) (s² + 9)] &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;6&nbsp; 0 <br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = -<u>1</u> ∫ cos(3t - 2u) - cos(4u - 3t)du<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) (s² + 9)] &nbsp;&nbsp; &nbsp;&nbsp;&nbsp;6&nbsp; 0<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;t<br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = -<u>1</u>[<u>&nbsp;&nbsp;sin(3t - 2u)&nbsp;&nbsp;</u> - <u>&nbsp;&nbsp;sin(4u - 3t)&nbsp;&nbsp;</u>] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [(s² + 1) (s² + 9)] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6 [&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br><br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = <u>1</u> [<u>sin 3t</u> - <u>sin 3t</u> - <u>sin t</u> - <u>sin t</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) (s² + 9)]&nbsp;&nbsp;&nbsp;&nbsp;6 &nbsp;[&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp; ]<br><br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = <u>1</u> [<u>2 sin 3t - sin 3t</u> - <u>2 sin t - sin t</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) (s² + 9)]&nbsp;&nbsp;&nbsp;&nbsp;6 &nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ]<br><br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> . <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>] = <u>&nbsp;1&nbsp;</u> [3sin t - sin 3t]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) (s² + 9)]  &nbsp;&nbsp;&nbsp;24",
        },
        {
            "question": "➢Find the Inverse Laplace transform of <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s - 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s² + 2s + 2",
            "options": ["<br>e^-t[cos t - sin t]", "<br>e^-t[cos t + sin t]", "<br>e^-t[sin t - cos t]"],
            "answer": "<br>e^-t[cos t - sin t]",
            "explanation": "<br><br><br><b>Solution:</b><br>L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s - 1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>] = L^-1[<u>(s + 1) -1</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s² + 2s + 2] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s² + 1) + 1]<br><br>= L^-1[<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s + 1)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> -  <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;(s² + 1) + 1 &nbsp;&nbsp;&nbsp;&nbsp;   (s² + 1) + 1&nbsp;&nbsp;&nbsp;]<br><br>= e^-t L^-1 [<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> - <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [&nbsp;&nbsp;(s)² + 1 &nbsp;&nbsp;&nbsp; (s²) + 1&nbsp;&nbsp;]<br><br>= e^-t[cos t - sin t]", 
        },
        {
            "question": "➢ Compute the inverse Laplace transform of Y (s) =  <u>&nbsp;&nbsp;2&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3s⁴",
            "options": ["<br><u> 1 </u> t³<br>6", "<br><u> 1 </u> t³<br>9", "<br>-<u> 1 </u> t³<br>9"],
            "answer": "<br><u> 1 </u> t³<br>9",
            "explanation": "<br><br><br><b>Solution:</b><br>Y (s) = <u>&nbsp;2&nbsp;</u> = <u>1</u>. <u>3!</u> <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3s⁴   &nbsp;&nbsp; 9&nbsp;&nbsp;   s⁴<br>Thus, by linearity, <br>y(t) = L^-1[<u>1</u> . <u>3!</u>] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ 9 &nbsp;&nbsp;s⁴]<br><br>= <u>1</u>L^-1 [<u>3!</u>] <br>&nbsp;&nbsp; 9&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s⁴<br><br>= <u>1</u>t³ <br> &nbsp;&nbsp;&nbsp;9", 
        },
        {
            "question": "➢Compute the Inverse Laplace transform of Y (s) = <u>&nbsp;&nbsp;&nbsp;4(s - 1)&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s - 1)² + 4",
            "options": ["<br>-4e^t cos 2t", "<br>4e^t cos 4t", "<br>4e^t cos 2t"],
            "answer": "<br>4e^t cos 2t",
            "explanation": "<br><br><br><b>Solution:</b><br>The Transform pair is:<br>cos 2t = <u>&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;&nbsp;</u> <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s² + 4<br><br>e^t cos 2t = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s - 1&nbsp;&nbsp;&nbsp;&nbsp;</u> <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s - 1)² + 4<br>Hence,<br>y(t) = L^-1[ <u>&nbsp;&nbsp;&nbsp;4(s - 1)&nbsp;&nbsp;&nbsp;</u>] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[(s - 1)² + 4]<br><br>= 4e^t cos2t",
        },
        {
            "question": "➢The Inverse Laplace transform of <u>&nbsp;&nbsp;&nbsp;&nbsp;s + 9&nbsp;&nbsp;&nbsp;&nbsp;</u> is <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 6s + 13)",
            "options": ["<br>e^-3t cos 2t + 3e^-3t sin 2t", "<br>e^-3t sin 2t + 3e^-3t cos 2t", "<br>e^-3t cos 2t - 3e^-3t sin 2t"],
            "answer": "<br>e^-3t cos 2t + 3e^-3t sin 2t",
            "explanation": "<br><br><br><b>Solution:</b><br>F(s) = <u>&nbsp;&nbsp; s + 9 &nbsp;&nbsp;</u> <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s² + 6s 13<br><br>= <u>&nbsp;s + 3 + 6 &nbsp;</u><br> &nbsp;&nbsp;(s + 3)² + 4<br><br>F(s) = <u> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s + 3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> + <u> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </u> <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s + 3)² + 4  &nbsp;&nbsp;(s + 3)² + 4<br><br>L^-1[F(s)]<br><br>= e^-3t [L^-1 (<u>&nbsp;&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;&nbsp;&nbsp;</u>) + L^-1 (<u>&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;</u>)] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 4) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s² + 4)<br><br>= e^-3t cos 2t + 3e^-3t sin 2t",
        },
        {
            "question": "➢ The Inverse Laplace transform of U(s) = <u>1</u> + <u>&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;</u><br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s³&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s² + 4",
            "options": ["<br><u>s²</u> + 3 sin 2t<br>2", "<br><u>s²</u> - 3 sin 2t<br>2", "<br><u>s²</u> + 3 cos 2t<br>2"],
            "answer": "<br><u>s²</u> + 3 sin 2t<br>2",
            "explanation": "<br><br><br><b>Solution:</b><br>u(t) = L^-1 {U(s)}<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=<u>1</u>L^-1 {<u>&nbsp;2&nbsp;</u>} + 3L^-1{<u>&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;</u>} <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2  &nbsp;&nbsp;&nbsp; &nbsp;&nbsp; &nbsp;{s³} &nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {s² + 4}<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=<u>s²</u> + 3 sin 2t <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2",
        },
        {
            "question": "➢: Let G(s) = s(s² + 4s + 5)^-1. The inverse transform of G(s) is",
            "options": ["<br>e^-2t sin t - 2e^-2t cos t", "<br>e^-2t cos t - 2e^-2t sin t", "<br>e^-2t cos t + 2e^-2t sin t"],
            "answer": "<br>e^-2t cos t - 2e^-2t sin t",
            "explanation": "<br><br><br><b>Solution:</b><br>g(t)= L^-1{<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>} <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{s² + 4s + 5}<br><br>= L^-1{<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>} <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{(s + 2)² + 1}<br><br>= L^-1{<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s + 2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>} - L^-1{<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>}<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{(s + 2)² + 1}  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{(s + 2)² + 1}<br><br>= e^-2t cos t - 2e^-2t sin t",
        },
        {
            "question": "➢Find the Inverse Laplace Transform of L^-1{<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>}<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{s² - 2s - 8}",
            "options": ["<br>e^2t - e^-2t", "<br>e^4t - e^-2t", "<br>e^4t + e^-2t"],
            "answer": "<br>e^4t - e^-2t",
            "explanation": "<br><br><br><b>Solution:</b><br><u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> &nbsp;=&nbsp; <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> &nbsp;=&nbsp; <u>&nbsp;&nbsp;A&nbsp;&nbsp;</u> + <u>&nbsp;&nbsp;B&nbsp;&nbsp;</u> , <br> s² - 2s - 8   &nbsp;&nbsp;&nbsp;(s - 4)(s + 2) &nbsp;&nbsp;&nbsp; s - 4 &nbsp;&nbsp; s + 2<br><br>So,6= A(s + 2) + B(s - 4)<br><br>When s = 4, 6A = 6, so A = 1, when s = -2, -6B = 6, so B = -1<br><br>So, <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u> = <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u> - <u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u> <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;s² - 2s -8  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(s - 4) &nbsp; s + 2<br><br>L^-1 {<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u>} = L^-1{<u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>} - L^-1{<u>&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;</u>} = e^4t - e^-2t <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{s² - 2s - 8} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;{s - 4} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; {s + 2}",
        },
       
    ],
    'FourierSeries': [
        {
            "question": "8 - 4",
            "options": ["2", "4", "6"],
            "answer": "4",
            "explanation": "8 minus 4 equals 4.",
        },
        {
            "question": "2 - 4",
            "options": ["-2", "4", "6"],
            "answer": "-2",
            "explanation": "2 minus 4 equals -2.",
        },
        {
            "question": "8 - 2",
            "options": ["2", "4", "6"],
            "answer": "6",
            "explanation": "8 minus 2 equals 6.",
        },
        {
            "question": "6 - 2",
            "options": ["2", "4", "6"],
            "answer": "4",
            "explanation": "6 minus 2 equals 4.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        
    ],
    'ComplexVariables': [
        {
            "question": "➢Show that the following function is analytic and find their derivatives.  f(z) = z³",
            "options": ["3z²", "3z", "6z"],
            "answer": "3z²",
            "explanation": "<br><br><br><b>Solution:</b><br>We have f(z) = z³ = (x + iy)³<br><br>∴ f(z) = x³ + 3ix²y - 3xy² - iy³<br><br>∴ u = x³ - 3xy², v = 3x²y - y³<br><br>∴ <u>∂u</u> = 3x² - 3y², <br>&nbsp;&nbsp;∂x <br><br>∴ <u>∂v</u> = 6xy, <br>&nbsp;&nbsp;∂x <br><br>  ∴ <u>∂u</u> = -6xy, <br>&nbsp;&nbsp;∂y <br><br>∴ <u>∂v</u> = 3x² - 3y², <br>&nbsp;&nbsp;∂y <br><br>∴ ux = vy and uy = -vx<br><br>∴ f(z) = z³ is analytic and can be differential<br><br>∴ f(z) = 3z²",
        },
        {
            "question": "➢Show that the following function is analytic and find their derivatives.  f(z) = sinz",
            "options": ["cos 2", "cos z", "cos²z"],
            "answer": "cos z",
            "explanation": "<br><br><br><b>Solution:</b><br>f(z) = sinz = sin(x + iy) = sinx cos iy + cos x sin iy<br><br>= sin x cos hy + i cos x sin hy<br><br>∴ u = sin x cos hy, v = cos x sin hy<br><br>∴ <u>∂u</u> = cos x cos hy, <br>&nbsp;&nbsp;∂x <br><br>∴ <u>∂v</u> = -sin x sin hy, <br>&nbsp;&nbsp;∂x <br><br>  ∴ <u>∂u</u> = sin x sin hy, <br>&nbsp;&nbsp;∂y <br><br>∴ <u>∂v</u> = cos x cos hy, <br>&nbsp;&nbsp;∂y <br><br>∴ux = vy and uy = -vx<br><br>∴f(z) = sin z is analytic<br><br>∴f'(z) = cos z",
        },
        {
            "question": "➢Construct an analytic function whose real part is e^x cos y",
            "options": ["e^z - c", "e + c", "e^z + c"],
            "answer": "e^z + c",
            "explanation": "<br><br><br><b>Solution:</b><br>Let u = e^x cos y <br><br>∴ux = e^x cos y and uy = -e^x sin y<br><br>∴φ1 = ux = e^x cos y, φ2 = uy = -e^x sin y<br><br>∴By Milne-Thomson method<br><br>∴f'(z) = φ1(z,0) - iφ2(z,0) = e^z - i(0)<br><br>∴f(z) = ∫ e^z dz = e^z + c which is required analytic function",
        },
        {
            "question": "➢Find the value of z foe the following function which is not analytic",
            "options": ["0", "2", "6"],
            "answer": "0",
            "explanation": "<br><br><br><b>Solution:</b><br>We have z = e^-v(cos u + i sin u) = e^-v e^iu<br><br>∴ z = e^-v+iu = e^i²v+iu = e^(u+iv) = e^iw where w = u + iv<br><br>∴iw = log z<br><br>∴ w = 1/i log z<br><br>∴ dw/dz = 1/iz<br><br>∴ w is not analytic at z = 0",
        },
        {
            "question": "➢Determine the constants a, b, c, d if f(z) = x² + 2axy + by² + i(cx² + 2dxy + y²) is analytic",
            "options": ["a = 1, b = -1, c = -1, d = -1 ", "a = 1, b = -1, c = -1, d = 1 ", "a = -1, b = -1, c = -1, d = 1 "],
            "answer": "a = 1, b = -1, c = -1, d = 1 ",
            "explanation": "<br><br><br><b>Solution:</b><br>We have f(z) = u + iv<br><br>and u = x² + 2axy + by² ; v = cx² + 2dxy + y²<br><br>∴ ux = 2x - 2ay, uy = 2ax + 2by<br><br>∴ vx = 2cx - 2dy, vy = 2dx + 2y<br><br>Since, f(z) is analytic, Cauchy-Riemann Eqations are satisfies.<br><br>∴ ux = vy and uy = -vx<br><br>∴ 2x + 2ay = 2dx + 2y and 2ax + 2by = -2cx-2dy<br><br>Equating the coeffients of x and y,we get a = 1, b = -1, a = -c, -d = b = 1<br><br>∴ a = 1, b = -1, c = -1, d = 1 ",
        },
        
        
    ],
    'StatisticalTechniques': [
        {
            "question": "➢Compute Spearman's rank correlation coefficient from the following data<br><br>X : 18 20 34 52 12<br>Y : 39 23 35 18 46",
            "options": ["-0.6", "-0.9", "-0.3"],
            "answer": "-0.9",
            "explanation": "<br><br><br><b>Solution:</b><br>First we give ranks to the data in descending order and then calculate D² = (R1 - R2)².<br><br>Serial No.   &nbsp;&nbsp;&nbsp;    X   &nbsp;&nbsp;&nbsp;&nbsp;  R1  &nbsp;&nbsp;&nbsp;&nbsp;   Y  &nbsp;&nbsp;&nbsp;&nbsp;     R2  &nbsp;&nbsp;&nbsp;&nbsp;    D²=(R1 - R2)²  <br> &nbsp;&nbsp;&nbsp;&nbsp;       1         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      18          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        4       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          39            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       2        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4<br>&nbsp;&nbsp;&nbsp;&nbsp;       2         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      20          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        3       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          23            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       4        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;&nbsp;       3         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      34          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        2       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          35            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       3        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;&nbsp;       4         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      52          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        1       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          18            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       5        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16<br>&nbsp;&nbsp;&nbsp;&nbsp;       5         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      12          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        5       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          46            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       1        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;16<br><br>N = 5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∑ D² = 38<br><br>∴R = 1 - 6∑ D² / N³ - D. Here,∑D² = 38, N=5<br><br>∴R = 1 - 6 * 38 / 125 -5 = 1 - 228/120 = 1 - 1.9 = -0.9",
        },
        {
            "question": "➢The equations of the two regression lines are 3x + 2y = 26 and 6x + y = 31 find the means of X and Y",
            "options": ["X=4, Y=7", "X=6, Y=7", "X=4, Y=14"],
            "answer": "X=4, Y=7",
            "explanation": "<br><br><br><b>Solution:</b><br>We solve the equations simultaneously. Multiply the second by 2 and sbtract from the first.<br><br>∴ 3x + 2y = 26 - 2(12x + 2y = 62) = 9x = 36<br><br>∴x = 4<br><br>Putting this value of x in the second equation, we get 24 + y = 31 <br><br>∴y = 7<br><br>∴X = 4, Y = 7",
        },
        {
            "question": "➢Compute Spearman's coefficient of rank correlation coefficient from the data on height and weight of eight students.<br><br>Height : 60 62 &nbsp;64 &nbsp;&nbsp;66 &nbsp;&nbsp;&nbsp;68 &nbsp;&nbsp;70 &nbsp;&nbsp;72 &nbsp;&nbsp;74<br>Weight : 92 83 101 110 128 119 137 146",
            "options": ["0.956", "0.954", "0.952"],
            "answer": "0.952",
            "explanation": "<br><br><br><b>Solution:</b><br>Serial No.   &nbsp;&nbsp;&nbsp;    Height   &nbsp;&nbsp;&nbsp;&nbsp;  R1  &nbsp;&nbsp;&nbsp;&nbsp;   Weight  &nbsp;&nbsp;&nbsp;&nbsp;     R2  &nbsp;&nbsp;&nbsp;&nbsp;    D²=(R1 - R2)²  <br> &nbsp;&nbsp;&nbsp;&nbsp;       1         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      60          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        &nbsp;&nbsp;&nbsp;&nbsp;1       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          92            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       2        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;&nbsp;       2         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      62          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       &nbsp;&nbsp;&nbsp;&nbsp; 2       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          83            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       1        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;&nbsp;       3         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      64          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  3       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          101            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       3        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br>&nbsp;&nbsp;&nbsp;&nbsp;       4         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     66          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  4       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          110           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       4        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br>&nbsp;&nbsp;&nbsp;&nbsp;       5         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     68          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  5       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          128          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       6        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;&nbsp;       6         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      70          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  6       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          119        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       5        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1<br>&nbsp;&nbsp;&nbsp;&nbsp;       7         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      72          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  7       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          137           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       7        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br>&nbsp;&nbsp;&nbsp;&nbsp;       8         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      74          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  8       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          146           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       8        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br>N = 8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∑ D² = 4<br><br>∴R = 1 - 6∑ D² / N³ - D. Here,∑D² = 4, N=8<br><br>∴R = 1 - 6 * 4 / 512 - 8 = 1 - 24/504 = 1 - 10148 = 0.952",
        },
        {
            "question": "➢If the tangent of the angle made by the line of regression of y on x is 0.6 and σy = 2σx, find the correlation coeffient between x and y.",
            "options": ["0.3", "0.6", "0.9"],
            "answer": "0.3",
            "explanation": "<br><br><br><b>Solution:</b><br>If the eqation of the line of regression of y on x is y - y^- = byx(x - x^-) then we know that byx is the slope of the line of regression. We are thus, given byx = 0.6<br><br> But byx = r σy / σx and σy = 2 σx <br><br> Putting these value, 0.6 = r . 2σx / σx = 2r <br><br> ∴ r = 0.6 / 2 = 0.3",
        },
        {
            "question": "➢Fit a straight line to the following data.<br>Year x &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;: 1951 1961 191 1981 1991<br>Production y :&nbsp;&nbsp; 10 &nbsp;&nbsp;&nbsp;12 &nbsp;&nbsp;&nbsp;8&nbsp;&nbsp;&nbsp; &nbsp; 10&nbsp;&nbsp;&nbsp; 15 <br> Also estimate the production in 1987",
            "options": ["12.30", "12.28", "12.25"],
            "answer": "12.28",
            "explanation": "<br><br><br><b>Solution:</b><br>Now the means of x and y are x = 1971 and y = 11.<br><br>Since x and y are round figures, we shall take deviations from 1971 and 11.<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    y   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  X=x-1971  &nbsp;&nbsp;&nbsp;&nbsp;   Y=y-11  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     X²  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   XY  <br> &nbsp;&nbsp;&nbsp;&nbsp;       1951         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      10          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;        &nbsp;&nbsp;&nbsp;&nbsp;-20       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          -1            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       400        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;20<br>&nbsp;&nbsp;&nbsp;&nbsp;       1961         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      12          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       &nbsp;&nbsp;&nbsp;&nbsp; -10       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         1            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       1        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-10<br>&nbsp;&nbsp;&nbsp;&nbsp;       1971         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      8          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  0       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          -3            &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       3        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0<br>&nbsp;&nbsp;&nbsp;&nbsp;       1981         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     10          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  10       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;         -1           &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       4        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-10<br>&nbsp;&nbsp;&nbsp;&nbsp;       1991         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     15          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;      &nbsp;&nbsp;&nbsp;&nbsp;  20       &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;          4          &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;       6        &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;80<br><br>Now, Y = a + bX<br><br>∴∑ Y = Na + b ∑ X and ∑XY = a∑X + b∑X²<br><br>Putting the above values<br>0 = 5a + 0 ∴a = 0<br><br>and 80 = 0 + 1000b ∴b = 0.08<br><br>Hence , the equation is Y = 0.08X<br><br>Putting the values of X, Y we get<br>y - 11 = 0.008(x - 1971)<br>∴ y = -146.68 + 0.08x<br><br>Putting x = 1987<br>y = -146.68 + 0.08(1987) = 12.28<br><br>∴The production in 1987 is 12.28",
        },
        
        
    ],
    'Probability': [
        {
            "question": "➢A number is selected from first 30 natral numbers. What is the probability that it will be divisible by 3 or 4.",
            "options": ["<br><u> 1 </u><span class='question'>  2</span>", "<br><u> 1 </u><span class='question'>  4</span>", "<br><u> 4 </u><span class='question'>  2</span>"],
            "answer": "<br><u> 1 </u><span class='question'>  2</span>",
            "explanation": "<br><br><br><b>Solution:</b><br>A number is selected from first 30 natural numbers <br><br>∴n (S) = 30 <br><br>Let A be the event that number is divisible by 3.<br><br>∴A = [3,6,9,12,15,18,21,24,27,30]<br><br>∴n(A) = 10<br><br>P(A) = <u>n (A) </u> = <u> 10 </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n (S) &nbsp;&nbsp;&nbsp; 30<br><br>Let B be the event that the nmber is divisible by 4.<br><br>∴B = {4,8,12,16,20,24,28}<br><br>∴n(B) = 7<br><br>∴P(B) = <u>n (B)</u> = <u>7</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;n (S) &nbsp;&nbsp; 30<br><br>A ∩ B = {12, 24} <br><br>∴n (A ∩ B) = 2<br><br>∴P(A ∩ B) = <u> 2 </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;30<br><br>∴ The probability that the nmber will be divisible by 3 or 4 is given by, <br><br>P(A ∪ B) = P(A) + P(B) - P(A ∩ B)<br><br>= <u> 10</u> + <u> 7 </u> - <u> 2 </u> <br>&nbsp;&nbsp; 30 &nbsp;&nbsp;30 &nbsp;30<br><br>= <u> 15 </u><br>&nbsp;&nbsp;&nbsp;30<br><br>= <u> 1 </u> <br>&nbsp;&nbsp;&nbsp;&nbsp;2  <br><br>",
        },
        {
            "question": "➢A random variable X has the following probability function:<br>&nbsp;&nbsp;&nbsp;X&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;:&nbsp; 1 &nbsp;&nbsp;&nbsp;2 &nbsp;&nbsp;&nbsp;&nbsp;3 &nbsp;&nbsp;&nbsp;&nbsp;4 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;6 &nbsp;&nbsp;&nbsp;&nbsp;7<br>P(X = x) : &nbsp;k &nbsp; 2k &nbsp; 3k &nbsp; k² &nbsp; k² + k &nbsp; 2k² &nbsp; 4k² <br><br>Find (i)k (ii)P(X<5), (iii)P(X>5), (iv)P(<u>&nbsp;&nbsp; &nbsp;&nbsp;  X < 5 &nbsp;&nbsp;&nbsp;&nbsp;</u>), (v)P(<u>&nbsp;&nbsp; &nbsp;&nbsp; X = 4 &nbsp;&nbsp;&nbsp;&nbsp;</u>) <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(&nbsp;2 < X < 6&nbsp;&nbsp;) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  (&nbsp;&nbsp;3 < X < 5&nbsp;&nbsp;)",
            "options": ["(i)1/8 , (ii)49/64 , (iii)3/32 , (iv)25/36 , (v)1/64", "(i)-1 , (ii)49/64 , (iii)3/32 , (iv)25/36 , (v)1/64", "(i)1/8 , (ii)49/64 , (iii)3/45 , (iv)5/36 , (v)1/64"],
            "answer": "(i)1/8 , (ii)49/64 , (iii)3/32 , (iv)25/36 , (v)1/64",
            "explanation": "<br><br><br><b>Solution:</b><br>Since Σp(xi) =1 <br><br>k + 2k + 3k + K² + k² + 2k² +4k² = 1<br><br>∴ 8k² + 7k - 1 = 0 ∴(8k - 1)(k + 1) = 0 <br><br>∴k = 1/8 or k = -1 which is impossible (why ?) <br><br>thus we have the folllowing probability distribution <br><br>X :&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 5&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 6 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;7<br><br>P(X=x) :&nbsp;&nbsp; 1/8 &nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp2/8 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp3/8&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp 1/64&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp; 9/64&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp; 2/64&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp 4/64<br><br>P(X < 5) = P(X = 1,2,3,4)<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp= P(X = 1) + P(X = 2) + P(X = 3) + P(X = 4)<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp= <u> 1 </u> + <u> 2 </u> +<u> 3 </u> +<u> 1 </u> = <u> 49 </u><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp8 &nbsp&nbsp;&nbsp;&nbsp8 &nbsp&nbsp;&nbsp;&nbsp8 &nbsp;&nbsp64 &nbsp;&nbsp64<br><br>P(X > 5) = P(X = 6,7)= P(X = 6) + P(X = 7)<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u> 2 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 4 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 6 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 3 </u> <br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;64 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp64 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp64 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;32 <br><br>&nbsp;&nbsp;P(<u> X < 5 </u>) = <u>P(X < 5 ∩ 2 < X ≤ 6)</u> = P(<u>2 < X < 5 </u>)<br>P(2 < X ≤ 6 ) &nbsp&nbsp;&nbsp;&nbsp;  P(2 < X ≤ 6 )&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;P(2 < X ≤ 6 )<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= &nbsp<u>P(X = 3,4)</u>&nbsp;&nbsp;&nbsp;&nbsp;= &nbsp;&nbsp;<u>25/64</u> &nbsp;&nbsp;=&nbsp;&nbsp;<u>25</u> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P(X = 3,4,5,6)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36/64 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36 <br><br>P(<u> X = 4 </u>) = <u>P(X = 4 ∩ 3 ≤ X ≤ 5)</u> = <br>P(3 ≤ X ≤ 6 ) &nbsp&nbsp;&nbsp;&nbsp;  P(3 ≤ X ≤ 6 )&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= &nbsp<u>P(X = 4)</u>&nbsp;&nbsp;&nbsp;&nbsp;= &nbsp;&nbsp;<u>1/64</u> &nbsp;&nbsp;=&nbsp;&nbsp;<u>1</u> <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P(X = 3,4,5,)&nbsp;&nbsp;&nbsp;34/64 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp64<br><br>&nbsp;",
        },
        {
            "question": "➢For the distribution, (i)Find the probability that is an odd number, (ii)Find the probability that Xlies between 3 and 9.",
            "options": ["(i)3/2 , (ii)29/36", "(i)1/2 , (ii)26/36", "(i)1/2 , (ii)29/36"],
            "answer": "(i)1/2 , (ii)29/36",
            "explanation": "<br><br><br><b>Solution:</b><br>P(X is odd) = P(X = 3,5,7,9 or 11)<br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;= P(X = 3) + P(X = 5) P(X = 7) + P(X = 9)+ P(X = 11)<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;=&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u> 2 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; - &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 4 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 6 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 4 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u> 2 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 18 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; =&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 1 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  <br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp36 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp36 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36 &nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp36 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp2 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<br><br>P(3 ≤ X ≤ 9) = P(X = 3,4,5,6,7,8 or 9)<br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;=P(X = 3)+ P(X = 4)+.......+P(X = 9)<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;=&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u> 2 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; + &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 3</u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; +......+&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; <u> 4 </u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; = &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<u> 29</u><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36 &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp36 &nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp36&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp&nbsp36",
        },
        {
            "question": "➢The probability mass function of a random variable X is zero except at the points X = 0, 1, 2. At these points it has  the values P(0) = 3c³ , P(1) = 4c - 10c² , P(2) = 5c - 1<br><br>(i)Determine c , (ii)Find P(X < 1) , (iii)P(1 < X < 2) , (iv)P(0 < X < 2)",
            "options": ["(i)1/3 , (ii)1/9 , (iii)2/3 , (iv)8/9", "(i)1/3 , (ii)1/6 , (iii)2/3 , (iv)8/9", "(i)2/3 , (ii)1/9 , (iii)2/3 , (iv)8/9"],
            "answer": "(i)1/3 , (ii)1/9 , (iii)2/3 , (iv)8/9",
            "explanation": "<br><br><br><b>Solution:</b><br>Since Σp =1 we have p(0) + P(1) + P(2) = 1<br><br>∴3C³ - 10C² + 4C + 5C - 1 = 1 &nbsp&nbsp;&nbsp;&nbsp;&nbsp; ∴3c³-10C²+9C-2=0<br><br>(3C-1)(C- 2)(c-1) &nbsp&nbsp;&nbsp;&nbsp;&nbsp;∴c=1/3<br><br>(The other value are not possible . why?)<br><br>∴ The probability dsitribution is <u>&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;X&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;2</u><br>&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;P(X=x)&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;1/9&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;2/9&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;2/3<br><br>P(X < 1)= P(X<0)=1/9; &nbsp;&nbsp&nbsp;P(1 < X ≤ 2)=2/3<br><br>P(0 < X ≤ 2) = P(X = 1)+ P(X = 2) = <u>2</u>+<u>2</u>=<u>8</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp &nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;9&nbsp;&nbsp;&nbsp;3&nbsp;&nbsp;&nbsp;9<br><br>",
        },
        {
            "question": "➢Three factories A, B, C produce 30%, 50% and 20% of the total production of an item. Out of their prodction 80%, 50%, and 10% are defective. An item is chosen at random and found to be defective. Find the probability that it was produced by the factory A.",
            "options": ["1.47", "0.47", "0.57"],
            "answer": "0.47",
            "explanation": "<br><br><br><b>Solution:</b><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp; p1=P(item produced by A )= 0.3<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp; p2=P(item produced by B )= 0.5<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp; p3=P(item produced by C )= 0.2<br>Let D be the event  that the item i defective then <br><br>p1´ = P(D/A)=0.8, p2´= P(D/B)=0.5, p3´=P(D/C)=0.1<br><br>Now the  required event A/D<br><br>∴P(A/D)= <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;p1p1'&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;</u> = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.3×0.8&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;</u> <br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;p1p1'+p2p2'+p3p3'&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;0.3×0.8+0.5×0.5+0.2×0.1<br><br>&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;<u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.24&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;</u> =<u>0.24</u> = 0.47<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.24+0.25+0.02&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0.51<br><br>&nbsp;",
        },
        
        
        
    ],
    'LinearAlgebra(Theory of Matrices)': [
        {
            "question": "<br>➢Find the characteristic equation of the matrix A given below and hence,&nbsp; find the matrix represented by A⁸ - 5A⁷ + 7A⁶ - 3A⁵ + A⁴ - 5A³ + 8A² - 2A +I, where <br> A = [ [2 1 1] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[0 1 0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1 1 2] ]",
            "options": ["Characteristic equation: λ³ - 5λ² + 7λ - 3 = 0, <br>Matrix: [ [8 5 5] <br><span class='question'>               [0 3 0]</span><br><span class='question'>               [5 5 8]</span> ]", "Characteristic equation: λ⁵ - 5 λ + 7λ - 3 = 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Matrix: [ [8 5 6] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[1 3 1]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5 5 8] ]", "Characteristic equation: λ³ + 5λ² - 7λ + 3 = 0, <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Matrix: [ [6 5 5] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4 3 2]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5 5 5] ]"],
            "answer": "Characteristic equation: λ³ - 5λ² + 7λ - 3 = 0, <br>Matrix: [ [8 5 5] <br><span class='question'>               [0 3 0]</span><br><span class='question'>               [5 5 8]</span> ]",
            "explanation": "<br><br><br><b>Solution:</b><br>The characteristic equation is, <br> &nbsp;&nbsp;&nbsp;&nbsp; [ [2 - λ  1  1] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [0  1 - λ  0] = 0<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ 1  1  2 - λ] ] <br> ∴ (2 - λ) [(1 - λ) (2 - λ) - 0] -1 [0 - 0] + [0 - (1 - λ)] = 0 <br> ∴ (4 - 4λ + λ²) (1 - λ) - (1 - λ) = 0<br> ∴4 - 4λ + λ² - 4λ - λ³ - 1 + λ = 0 <br> ∴ λ³ - 5λ² + 7λ - 3 = 0. <br> This equation is satisfied by A. <br> Now dividing λ⁸ - 5λ⁷ + 7λ⁶ - 3λ⁵ + λ⁴ - 5λ³ + 8λ² - 2λ + 1 by λ³ - 5λ² + 7λ - 3, we get the quotient λ⁵ + λ and the remainder λ² + λ + 1 <br> &nbsp;&nbsp; In terms of the matrix A this means, <br> &nbsp;&nbsp; A⁸ - 5A⁷ + 7A⁶ - 3A⁵ + A⁴ - 5A³ + 8A² - 2A +I = (A³ - 5A² + 7A - 3I) (A⁵ + A) + (A² + A + I )<br> But (A³ - 5A² + 7A - 3I) = 0 <br> ∴ L.H.S = A² + A + I <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [2 1 1] [2 1 1] &nbsp;&nbsp; [5 4 4] <br>Now,   A² = &nbsp;[0 1 0] [0 1 0] = [0 1 0] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [1 1 2] [1 1 2] &nbsp;&nbsp; [4 4 5] <br> <br>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5 4 4] &nbsp;&nbsp; [2 1 1] &nbsp;&nbsp;&nbsp;[1 0 0] &nbsp;&nbsp;&nbsp;&nbsp;[8 5 5] <br>∴A² + A + I = [0 1 0] + [0 1 0] + [0 1 0] = [0 3 0]  <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4 4 5] &nbsp;&nbsp; [1 1 2]&nbsp; &nbsp; [0 0 1] &nbsp;&nbsp;&nbsp; [5 5 8] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[8 5 5] <br>∴ The given expression = [0 3 0] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[5 5 8]",
        },
        {
            "question": "<br>➢Find the eigenvalues and eigenvectors of &nbsp;&nbsp;&nbsp;[-2 2 -3]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A = [2 1 -6] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-1 -2 0]",
            "options": ["Eigenvalues- 5, 3, 3<br>Eigenvectors- [2 -1 0], [3 0 1]", "Eigenvalues- 5, -3, -3<br>Eigenvectors- [2 -1 0], [3 0 1]" , "Eigenvalues- 5, 2,2 <br>Eigenvectors- [2 -2 0], [0 0 1]"],
            "answer": "Eigenvalues- 5, -3, -3<br>Eigenvectors- [2 -1 0], [3 0 1]",
            "explanation": "<br><br><br><b>Solution:</b><br>The Characteristic eqation is <br>&nbsp; [-2-λ  &nbsp;2&nbsp;  -3]<br>&nbsp;&nbsp;&nbsp;[2  &nbsp;1-λ&nbsp;  -6] = 0<br>&nbsp;&nbsp;&nbsp;[-1 &nbsp; -2&nbsp;  -λ] ∴ (-2-λ) [(1-λ)(-λ)-(-2)(-6)] -2 [-2λ-6]-3 [-4+1(1-λ)] = 0 <br>∴ (-2-λ)[-λ + λ² -12] +2 [2λ + 6] +3 [3 + λ] = 0<br>∴ (2 + λ) [12 + λ - λ²] + 4λ + 12 + 9 + 3λ= 0<br>∴ 24 + 2λ - 2λ² + 12λ + λ² - λ³ + 7λ + 21 = 0<br> ∴ -λ³ - λ² + 21λ + 45 = 0<br>∴ λ³ + λ² - 21λ - 45 = 0<br>∴ λ³ - 5λ² + 6λ² - 30λ + 9λ - 45 = 0<br>∴ λ² (λ-5) + 6(λ-5) + 9(λ-5) = 0<br>∴ (λ-5)(λ² + 6λ + 9) = 0<br>∴ (λ-5)(λ+3)² = 0<br> ∴ λ = 5, -3, -3.",
        },
        {
            "question": "<br>➢Two of the eigen values of a 3 x 3 matrix are -1, 2. If the determinant of the matrix is 4, find its thired eigen value.",
            "options": ["2", "-2", "1"],
            "answer": "-2",
            "explanation": "<br><br><br><b>Solution:</b><br>If the third eigen value is x then their product is equal to 4.<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;∴(-1) (2) (x) = 4 &nbsp;&nbsp; ∴x= -2 <br>&nbsp;&nbsp;&nbsp;&nbsp;Hence, the third eigen value is -2.",
        },
        {
            "question": "<br>➢Find the eigenvalues and eigenvectors of the matrix <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-2 5 4]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;A=[5 7 5]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[4 5 -2]",
            "options": ["Eigenvalues are -3, 12, 6 <br><span class='question'>   Eigenvector is [1 1 -1]</span>", "Eigenvalues are -3, -12, -6 <br><span class='question'>   Eigenvector is [1 0 -1]</span>", "Eigenvalues are -3, 12, -6 <br><span class='question'>   Eigenvector is [1 0 -1]</span>"],
            "answer": "Eigenvalues are -3, 12, -6 <br><span class='question'>   Eigenvector is [1 0 -1]</span>",
            "explanation": "<br><br><br><b>Solution:</b><br>The characteristic equation is <br>&nbsp;&nbsp;&nbsp; |-2-λ&nbsp; &nbsp;&nbsp;&nbsp;5&nbsp;&nbsp;&nbsp; &nbsp;4|<br>&nbsp;&nbsp;&nbsp; |5&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;7-λ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;5| = 0<br>&nbsp;&nbsp;&nbsp; |4&nbsp;&nbsp;&nbsp;&nbsp; 5 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-2-λ| <br> <br>On simplification, we get <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(λ + 3)(λ - 12)(λ + 6) = 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∴λ= -3, 12, -6<br> &nbsp;&nbsp;&nbsp;&nbsp;∴ -3, 12, -6 are the eigenvalues.<br><br> <b>(i)</b> For λ = -3, [A-λ1 I] X = 0 gives<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 5 10 5 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 4 &nbsp;5 &nbsp;1 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br> &nbsp;&nbsp;&nbsp;By R2 - R3<br>  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1 &nbsp;5 &nbsp;4 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 4 &nbsp;5 &nbsp;1 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br> By R2 - R1 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 &nbsp;0 &nbsp;0 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 4 &nbsp;5 &nbsp;1 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0] <br><br> By R32<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 4 &nbsp;5 &nbsp;1 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 &nbsp;0 &nbsp;0 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br>By R2 - R1 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 3 &nbsp;0 -3 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 &nbsp;0 &nbsp;0 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br>∴ x1 + 5x2 + 4x3 = 0; &nbsp;&nbsp;&nbsp;3x1 - 3x3 = 0<br><br>Putting x3 = t, x1 =t and 5x2 + 5t = 0 ∴x2 = -t<br><br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ t] &nbsp;&nbsp;&nbsp;&nbsp;[ 1]<br>&nbsp;X = [-t] = t[-1] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ t] &nbsp;&nbsp;&nbsp;&nbsp;[ 1]<br>Hence, corrresponding to λ = -3, the given vector is [ 1 -1 1 ].<br> <b>(i)</b> For λ = 12, [A-λ2 I] X = 0 gives<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ -14&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 5 &nbsp;&nbsp;-5 &nbsp;5 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 4 &nbsp;5 &nbsp;-14 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br>∴ -14x1 + 5x2 + 4x3 = 0;  &nbsp;&nbsp;&nbsp;  5x1 - 5x2 + 5x3 = 0; &nbsp;&nbsp;&nbsp; 4x1 + 5x2 - 14x3 = 0<br>Solving the first two equations by Crammer's rule, we get <br>&nbsp;&nbsp;<u> x1 </u> = <u> -x2 </u> = <u> x3 </u><br>&nbsp;&nbsp;45&nbsp;&nbsp;&nbsp;-90&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;45 <br><br>&nbsp;&nbsp;<u> x1 </u> = <u> -x2 </u> = <u> x3 </u> = t<br>&nbsp;&nbsp;&nbsp;&nbsp;1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1 <br><br>∴x1 = t, x2 = 2t, x3 = t.<br>∴X = [ t 2t t ] = t[ 1 2 1 ]. Hence, corresponding to λ = 12, the eigenvector is [ 1 2 1 ].<br> <b>(i)</b> For λ = -6, [A-λ3 I] X = 0 gives<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ -4&nbsp; 5 &nbsp;4 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 5 &nbsp;&nbsp;13 &nbsp;5 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 4 &nbsp;5 &nbsp;4 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br>∴ 4x1 + 5x2 + 4x3 = 0;  &nbsp;&nbsp;&nbsp;  5x1 + 13x2 + 5x3 = 0; &nbsp;&nbsp;&nbsp; 4x1 + 5x2 - 4x3 = 0<br>Solving the first two equations by Crammer's rule, we get <br>&nbsp;&nbsp;<u> x1 </u> = <u> -x2 </u> = <u> x3 </u><br>&nbsp;&nbsp;-27&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;27 <br><br>&nbsp;&nbsp;<u> x1 </u> = <u> -x2 </u> = <u> x3 </u> = t<br>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-1 <br><br>∴x1 = t, x2 = 2t, x3 = t.<br>∴X = [ t 0t -t ] = t[ 1 0 -1 ]. Hence, corresponding to λ = 12, the eigenvector is [ 1 0 -1 ].",
        },
        {
            "question": "<br>➢Find the eigenvalues and eigenvectors of the following matrix.<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 2 1 0 ]<br>&nbsp;&nbsp;A = [ 0 2 1 ] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 0 2 ]",
            "options": ["Eigenvalues are 1, 1, 1 <br><span class='question'>   Eigenvector is [1 0 0]</span>", "Eigenvalues are 2, 2, 2 <br><span class='question'>   Eigenvector is [1 0 0]</span>", "Eigenvalues are 2, 2, 2 <br><span class='question'>   Eigenvector is [1 1 0]</span>"],
            "answer": "Eigenvalues are 2, 2, 2 <br><span class='question'>   Eigenvector is [1 0 0]</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><br> The characteristic equation is <br>&nbsp;&nbsp;&nbsp; |-2-λ&nbsp; &nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp; &nbsp;0|<br>&nbsp;&nbsp;&nbsp; |0&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;2-λ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1| = 0<br>&nbsp;&nbsp;&nbsp; |0&nbsp;&nbsp;&nbsp;&nbsp; 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-2-λ| <br> <br>On simplification, we get <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(2 - λ)³ = 0 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp; ∴λ= 2, 2, 2<br><br> For λ = 2, [A-λ1 I] X = 0 gives<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 1 0 ] &nbsp;&nbsp;[x1] &nbsp;&nbsp; &nbsp;&nbsp; [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 0 1 ]&nbsp;&nbsp; [x2] &nbsp;&nbsp; = [0]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 0 0 0 ] &nbsp;&nbsp;[x3] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[0]<br><br>∴0x1 + x2 + 0x3 = 0;&nbsp;&nbsp;&nbsp; 0x1 + 0x2 + x3 = 0 <br>By Cramer's rule<br>&nbsp;&nbsp;<u> x1 </u> = <u> -x2 </u> = <u> x3 </u> = t<br>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;0 <br><br>∴x1 = t, x2 = 0t, x3 = 0t.<br>∴X = [ t 0t 0t ] = t[ 1 0 0 ]. Hence, corresponding to λ = 2, the eigenvector is [ 1 0 0 ]",
        },
        {
            "question": "<br>➢&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 2 -1 1 ]<br>Find the characteristic equation of the matrix [ -1 2 -1 ] and verify that it is satisfied by A and hence, obtain A^-1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1 -1 2 ]",
            "options": ["<span class='question'>                 [ 3 1 -1 ]</span><br>A^-1 = 1/4 [ 1 3 1 ] <br><span class='question'>                  [-1 1 3 ]</span>", "<span class='question'>                 [ 3 -1 1 ]</span><br>A^-1 = 1/4 [ 1 3 1 ] <br><span class='question'>                  [-1 1 3 ]</span>", "<span class='question'>                 [ 3 1 -1 ]</span><br>A^-1 = 1/4 [ 1 -3 1 ] <br><span class='question'>                  [1 -1 3 ]</span>"],
            "answer": "<span class='question'>                 [ 3 1 -1 ]</span><br>A^-1 = 1/4 [ 1 3 1 ] <br><span class='question'>                  [-1 1 3 ]</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><br> The characteristic equation is <br>&nbsp;&nbsp;&nbsp; |2-λ&nbsp; &nbsp;&nbsp;&nbsp;-1&nbsp;&nbsp;&nbsp; &nbsp;1|<br>&nbsp;&nbsp;&nbsp; |-1&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;2-λ &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-1| = 0<br>&nbsp;&nbsp;&nbsp; |1&nbsp;&nbsp;&nbsp;&nbsp; -1 &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2-λ| <br> <br>∴ (2-λ)[(2-λ)²-1]+1[-1(2-λ)+1] +1[1-(2-λ)]=0<br>∴λ³ - 6λ² + 9λ -4 = 0 <br><br>Cayley-Hamilton Theorem states that this equation is satisfied by A, i.e. A³ - 6A² + 9A - 9I = 0<br><br>Now,<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 2 -1 1 ] &nbsp;&nbsp;[2 -1 -1 ] &nbsp;&nbsp; &nbsp;&nbsp; [ 6 -5 5 ]<br>A² = &nbsp;[ -1  2 -1 ]&nbsp;&nbsp; [-1 2 -1] &nbsp;&nbsp; = [-5 6 -5 ]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1 -1 2 ] &nbsp;&nbsp;[1 -1 2 ] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;[5 -5 6 ]<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 6 -5 5 ] &nbsp;&nbsp;[2 -1 1 ] &nbsp;&nbsp; &nbsp;&nbsp; [ 22 -21 21 ]<br>A³ = &nbsp;[ -5  2 -5 ]&nbsp;&nbsp; [-1 2 -1] &nbsp;&nbsp; = [-21 22 -21 ]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 5 -5 6 ] &nbsp;&nbsp;[1 -1 2 ] &nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;[21 -21 22 ]<br><br>It can be seen that A³ - 6A² + 9A -4I = 0<br><br>Now multiply by A^-1<br> ∴ A² - 6A + 9I -4A^-1 = 0<br>∴ 4A^-1 = (A² - 6A + 9I)<br><br>∴&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 3 1 -1 ]<br>A^-1 = 1/4 [ 1 3 1 ] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[-1 1 3 ]",
        },
        {
            "question": "<br>➢If λ1, λ2, λ3 are the eigen values of the matrix [ -2 -9 5 ] [ -5 -10 7 ] [ -9 -21 14 ] then find λ1+λ2+λ3 and λ1*λ2*λ3.",
            "options": ["Sum = 2 Product = 4", "Sum = 2 Product = 2", "Sum = 4 Product = 4"],
            "answer": "Sum = 2 Product = 4",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Sum of the eigenvalues is;<br>= λ1 + λ2 + λ3<br>= Sum of diagonal elements<br>= -2-10+14 = 2<br>Product of the eigenvalues is;<br> = λ1*λ2*λ3<br>= |A|<br>= -2(-140 + 144) + 9(-70 + 63) + 5(105 - 90)<br>= -8-63+75= 4",
        },
        {
            "question": "<br>➢Use Cayley-Hamilton theorem to find 2A⁴ - 5A³ - 7A + 6I where <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; A = [ 1 2 ]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ 2 2 ]",
            "options": ["<br>[ 36 32 ]<br>[ 32 52 ]", "<br>[ 32 36 ]<br>[ 32 52 ]", "<br>[ 36 32 ]<br>[ 52 32 ]"],
            "answer": "<br>[ 36 32 ]<br>[ 32 52 ]",
            "explanation": "<br><br><br><b>Solution:</b><br><br> The characteristic equation of A is <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;1-λ &nbsp;&nbsp;&nbsp;&nbsp;2 | <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;|&nbsp; 2 &nbsp;&nbsp;&nbsp;&nbsp;2-λ |<br><br>∴ (1-λ) (2-λ-4 = 0)<br>∴2-3λ+λ²-4 = 0<br>∴λ-3λ²-2 = 0<br><br>By Cayley-Hamilton theorem, tis equation is satisfied by A<br>∴ A² - 3A - 2I = 0 <br>Now dividing 2λ⁴ - 5λ³ - 7λ + 6 by λ² - 3λ - 2, we get <br> 2λ⁴ - 5λ - 7λ + 6I = (λ² - 3λ - 2) (2λ² +λ + 7) + 16A 20<br> In terms of matrix A, this means 2A - 5A³ - 7A + 6 = (A² - 3A 2I) (2A² + A + 7I) 16A + 20I <br><br> But as seen above <br> A - 3A - 2I = 0 <br>∴2A⁴ - 5A³ - 7A + 6I = 16A + 20I<br>= 16[ 1 2 ] + 20[ 1 0 ] = [ 36 32 ] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 2 2 ]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [ 0 1 ]&nbsp;&nbsp;&nbsp;&nbsp;[ 32 52 ]",
        },
       
        
    ],
    'ComplexIntegration': [
        {
            "question": "<br>➢Evaluate ∫ tan z dz where C is |z|=1/2 ",
            "options": ["0", "5", "tan z"],
            "answer": "0",
            "explanation": "<br><br><br><b>Solution:</b><br><br> The counter C is a circle with centre (0,0) and radius 1/2. <br> Now   tan z = <u>sin z</u>    <br>   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cos z <br> and cos z = 0 for z = +π/2.<br> But z = +-π/2 lies outside C. Hence, f(z) is analytic in and on C. <br> Hence, by Cauchy's theorem <br> ∫ f(z)dz = 0 <br> ∴ ∫tan z dz = 0.",
        },
        {
            "question": "<br>➢Evaluate ∫(8z + 3z)dz around the curve  x ^ (2/3) + y ^ (2/3) = a ^ (2/3)",
            "options": ["6πa²i", "4" , "cos⁴θ * sin²θ"],
            "answer": "6πa²i",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Since C is a closed curve and the part f(z) = 3z is analytic by Cauchy's Theorem ∫3z dz=0.<br>Hence, I= ∫8z dz = ∫8(x-iy)(dx+i idy)=8 ∫(x dx+y dy)+ i(xdy - ydx)<br>Now, we put x = a cos³θ,  y = a sin³θ <br>and dx = - 3a cos²θ  sinθ dθ, <br> dy = 3a sin²θ cosθ  dθ<br><br> I = 8 * 4 * 3a² ∫(0-pi/2)[(- cos⁵θ sinθ) + sin⁵θ cos θ] +i [(cos⁴θ  sin²θ + sin⁴θ  cos²θ)]  dθ <br> = 96 a² {[(cos⁶θ)/6] +[ sin⁶θ/ 6 ] + ∫ i[cos⁴θ sin²θ + sin⁴θ cos²θ]dθ}  <br><br> ∴ I = 96a² {(0 - 1/6) + (1/6 - 0) + i [3*1*1/6*4*2  *  pi/2 + 3*1*1/6*4*2 * pi/2]} <br> <br> = 96a² [0 + i(pi/32 + pi/32)] = 96a²i/16 pi <br> = 6πa²i",
        },
        {
            "question": "<br>➢Evaluate ∫ z dz, where C is the upper half of the circle r = 1.",
            "options": ["i π", "i π²", "π"],
            "answer": "i π",
            "explanation": "<br><br><br><b>Solution:</b><br><br>Let us put z = r e^iθ. <br> <br> Since r = 1, z = e^iθ, dz = e^iθ . i . dθ. <br><br>∴ ∫ z dz = ∫ (1 to -1) z dz <br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= ∫( 0 to π) e^iθ . e^iθ . i . dθ<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= ∫(0 to π)i dθ <br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= i [θ](0 to π) <br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= i π. ",
        },
        {
            "question": "<br>➢Evaluate ∫ (z + 2z)dz along the circle x² + y² = 1",
            "options": ["2iπ + e^2iπ - 1", "2iπ + e^4iπ - 2", "2iπ + e^4iπ - 1"],
            "answer": "2iπ + e^4iπ - 1",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Let us put z = r e^iθ <br><br>∴  r = 1, z = e^iθ, z = e^-iθ<br>∴ dz = i e^iθ dθ<br><br>∫ (z + 2z)dz =∫(0 to 2π) (e^iθ + 2eiθ) i . e^iθ dθ <br><br> = ∫ (0 to 2π) i dθ + 2i ∫ (0 to 2π) e^2iθ<br><br>= i [θ](0 to 2π) + 2i[<u>e^2iθ</u>](0 to 2π)<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;2i&nbsp;] <br><br>= 2iπ + e^4iπ - 1",
        },
        {
            "question": "<br>➢Show that ∫ logz dz = 2πi, where C is the unit circle in the z-plane.",
            "options": ["πi", "2πi", "2π"],
            "answer": "2πi",
            "explanation": "<br><br><br><b>Solution:</b><br><br>Since the counter is a circle we use polar coordinates.<br>We put z = e^iθ &nbsp;&nbsp;&nbsp;&nbsp; r = 1&nbsp;&nbsp;&nbsp;&nbsp; dz = i e^iθ dθ;&nbsp;&nbsp;&nbsp;&nbsp; θ varies from 0 to 2π<br><br>∴I = ∫(0 to 2π)(log e^iθ) . i e^iθ dθ <br><br>&nbsp;&nbsp;&nbsp;&nbsp;= i ∫(0 to 2π)i e^iθ dθ <br><br>&nbsp;&nbsp;&nbsp;&nbsp;= - ∫(0 to 2π)e^iθ dθ<br><br>= -[θ. <u> e^iθ</u> - ∫<u>e^iθ</u> . 1 . dθ](0 to 2π)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br><br>= -[θ. <u> e^iθ</u> - <u>e^iθ</u> . 1 . dθ](0 to 2π)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-1&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br><br>= -[θ. <u> e^iθ</u> - ∫<u>e^iθ</u> . 1 . dθ](0 to 2π)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; i &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br><br>= - [<u> 2π e^2iπ</u> + e^2iπ - 0 -1]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;i&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]         &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;     [ ∴e^2iπ = 1]<br><br> = -[<u> 2π </u> + 1 -1]<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;i&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;] <br><br>= - <u>2πi</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;i² <br><br> = 2πi.",
        },
        {
            "question": "<br>➢Evaluate ∫ z² dz, where C is the circle x = r cosθ, y = r sinθ, from θ = 0 to θ = π/3.",
            "options": ["-<u> 2r³</u><br><span class='question'>       2</span>", "-<u> 2r³</u><br><span class='question'>       3</span>", "-<u> 2r³</u><br><span class='question'>        15</span>"],
            "answer": "-<u> 2r³</u><br><span class='question'>       3</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><br> I = ∫ z² dz<br><br> = ∫ (0 to π/3) r² e^2iθ . re^iθ . idθ<br><br> = r³i∫(0 to π/3)e^3iθ dθ<br><br> = r³i[<u>&nbsp;e^3iθ&nbsp; </u>](0 to π/3)<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3i&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;]<br><br> = <u>&nbsp;r³&nbsp;</u>[e^iθ  - 1]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3<br><br> = <u>&nbsp;r³&nbsp;</u>[cosπ + isinπ -1]<br>&nbsp;&nbsp;&nbsp;&nbsp;3<br><br> = -<u>2r³</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3",
        },
        
        
    ],
    'ZTransform': [
        {
            "question": "<br>➢Obtain Z{1}and hence deduce Z{a^k}, k<u>></u>0.",
            "options": ["<br><u><span class='question'>  z  </span></u><br><span class='question'> </span>z-a", "<br><u><span class='question'>  z  </span></u><br><span class='question'> </span>z+a", "<br><u><span class='question'>  za  </span></u><br><span class='question'> </span>z-a"],
            "answer": "<br><u><span class='question'>  z  </span></u><br><span class='question'> </span>z-a",
            "explanation": "<br><br><br><b>Solution:</b><br><br> By defination,<br>Z{1} = ∑ 1 . z^-k <br><br>= 1 + <u>1</u> + <u>1</u> + <u>1</u> + ........<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z &nbsp;&nbsp;&nbsp; z² &nbsp;&nbsp;z³<br><br>= <u>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;1-(1/z)<br><br>= <u>&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z-1<br><br>Now, a^k = a^k . 1. Hence by change of scale property,<br><br>Z{a^k} = Z{a^k.1}<br><br>= <u>&nbsp;&nbsp;&nbsp;z/a&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;(z/a)-1<br><br>= <u> &nbsp;&nbsp;z&nbsp;&nbsp; </u><br>&nbsp;&nbsp;&nbsp;z-a",
        },
        {
            "question": "<br>➢Find Z{c^k sinα   k} from Z{sinα  k}",
            "options": ["<br><u><span class='question'>        c sinα         </span></u><br><span class='question'>  z² - 2 c cosα + c²</span>", "<br><u><span class='question'>        cz sinα         </span></u><br><span class='question'>  z² - 2 cz cosα + c²</span>", "<br><u><span class='question'>        z sinα         </span></u><br><span class='question'>  z - 2 cz cosα + c²</span>"],
            "answer": "<br><u><span class='question'>        cz sinα         </span></u><br><span class='question'>  z² - 2 cz cosα + c²</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><br>We know that, Z{sinα   k} = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z sinα &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z² - 2z cosα +1<br><br>By change of scale property,<br><br>Z{c^k sinα  k} = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(z/c)sinα &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  </u><br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(z/c)² - 2(z/c)cosα + 1<br><br> = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;cz sinα &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z² - 2cz cosα + c² ",
        },
        {
            "question": "<br>➢If {f(k)} = {9, 6, 3, 0, -3, -6, -9}, find Z{f(k)}.",
            "options": ["<br>9z² + 6z + 3 + 0 - <u>3</u> - <u>6</u> - <u>9</u><br><span class='question'>                            z²   z³   z⁴</span>", "<br>9z + 6 + 3 + 0 - <u>3</u> - <u>6</u> - <u>9</u><br><span class='question'>                            z²   z³   z⁴</span>", "<br>9z² + 6z + 3 + 3 - <u>3</u> - <u>6</u> - <u>9</u><br><span class='question'>                            z²   z³   z⁴</span>"],
            "answer": "<br>9z² + 6z + 3 + 0 - <u>3</u> - <u>6</u> - <u>9</u><br><span class='question'>                            z²   z³   z⁴</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Since 3 is the term corresponding to k = 0. We have<br><br>f(-2) = 9, f(-1) = 6, f(0) = 3, f(1) = 0, f(2) = -3, f(3) = -6, f(4) = -9.<br><br>∴ Z{f(k)} =  ∑(k=-2 to 4)   f(k)z^-k<br><br> = 9z^2 + 6z^1 + 3z^0 + 0z^-1 - 3z^-2 - 6z^-3 - 9z^-4<br><br>= 9z² + 6z + 3 + 0 - <u>3</u> - <u>6</u> - <u>9</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z² &nbsp;&nbsp;z³ &nbsp;&nbsp;z⁴",
        },
        {
            "question": "<br>➢If {f(k)} = {2⁰, 2¹, 2², 2, .....}, find Z{f(k)}.",
            "options": ["2", "4", "<br><u><span class='question'>  z  </span></u><br> z-2"],
            "answer": "4",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Z-transform of the sequence is<br><br>∴ Z{f(k)} =     f(k)z^-k<br><br> = 2⁰ z⁰ + 2¹ z^-1 + 2² z^-2 + 2³ z^-3 .....<br><br>= 1 + <u>2</u> - <u>(2)²</u> + <u>(2)³</u> +...........<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; z &nbsp;&nbsp; (z)² &nbsp;&nbsp; (z)³<br><br>= <u>&nbsp;&nbsp;&nbsp;&nbsp;1&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;1-(2/z)<br><br>= <u>&nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;z-2 ",
        },
        
        {
            "question": "<br>➢Find the Z-tranform of f(k) = a^k, k<u>></u>0.",
            "options": ["<br><u><span class='question'>  z  </u></span><br> z-a", "<br><u><span class='question'>  a  </u></span><br> z-a", "<br><u><span class='question'>  z  </u></span><br> z-b"],
            "answer": "<br><u><span class='question'>  z  </u></span><br> z-a",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Assuming that f(k) = 0 when k < 0 <br><br>Z{f(k)} = ∑ a^k z^-k <br><br>= ∑ 0 . z^-k + ∑ a^k z^-k<br><br>= 1 + <u> a </u> + <u> a² </u> + ......<br>&nbsp;&nbsp;&nbsp;&nbsp;z &nbsp;&nbsp;&nbsp;   z²<br><br>= <u> &nbsp;&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp;&nbsp;  </u><br>&nbsp;&nbsp;&nbsp;1-(a/z)<br><br>= <u> &nbsp;&nbsp;z&nbsp;&nbsp; </u>&nbsp;&nbsp;&nbsp; z-aThe series being G.P. is convergent if 1 > |a/z| i.e. |z| > |a|<br><br> ∴ ROC is |z| > |a|<br><br>∴Z{a^k} = <u> &nbsp;&nbsp;z&nbsp;&nbsp; </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z-a",
        },
        {
            "question": "<br>➢Find the Z-tranform of f(k) = b^k, k<0.",
            "options": ["<br><u><span class='question'>  z  </u></span><br> b-z", "<br><u><span class='question'>  z  </u></span><br> z-b", "<br><u><span class='question'>  b  </u></span><br> b-z"],
            "answer": "<br><u><span class='question'>  z  </u></span><br> b-z",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Assuming that f(k) = 0 when k > 0<br><br>Z{f(k)} = ∑ f(k) z^-k <br><br>= ∑ b^-k . z^-k = ∑ b^-n z^n where n = -k<br><br>= <u> z </u> + <u> z² </u> + <u> z³ </u> + .....<br>&nbsp;&nbsp;&nbsp;b &nbsp;&nbsp;  b²&nbsp;&nbsp;&nbsp;   b³<br><br>= <u> z </u> (1 + <u> z </u> + <u> z² </u> + ....)<br>&nbsp;&nbsp; b (   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b  &nbsp;&nbsp;  b²  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  )<br><br>= <u> z </u>&nbsp;&nbsp; <u>&nbsp;&nbsp;&nbsp;&nbsp; 1&nbsp;&nbsp;&nbsp;&nbsp; </u><br>&nbsp;&nbsp;&nbsp;b &nbsp; 1-(z/b)<br><br>= <u> &nbsp;&nbsp;&nbsp;z&nbsp;&nbsp;&nbsp; </u><br> &nbsp;&nbsp;&nbsp;b-z<br><br> The series being G.P. is convergent if 1 > |z/b| i.e. |z| < |b|<br><br>∴ ROC is |z| < |b|<br><br>∴Z{b^k} = <u> &nbsp;&nbsp;z&nbsp;&nbsp; </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;b-z",
        },
        {
            "question": "<br>➢Find Z{c^k cosα   k} from Z{cosα  k}",
            "options": ["<br><u><span class='question'>      (z-c cosα)       </span></u><br><span class='question'>  z - 2 c cosα + c²</span>", "<br><u><span class='question'>      z(z-c cosα)       </span></u><br><span class='question'>  z² - 2 cz cosα + c²</span>", "<br><u><span class='question'>      z(z- cosα)       </span></u><br><span class='question'>  z² - 2 z cosα + c²</span>"],
            "answer": "<br><u><span class='question'>      z(z-c cosα)       </span></u><br><span class='question'>  z² - 2 cz cosα + c²</span>",
            "explanation": "<br><br><br><b>Solution:</b><br><br> We know that, Z{cosα   k} = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z(z- cosα) &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; </u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z² - 2z cosα +1<br><br>By change of scale property,<br><br>Z{c^k cosα  k} = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z/c{z/c - cosα} &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  </u><br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(z/c)² - 2(z/c)cosα + 1<br><br> = <u>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z(z-c cosα)&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;z² - 2cz cosα + c²",
        },
        
        
    ],
    'ProbabilityDistributionandSamplingTheory': [
        {
            "question": "<br>➢A hospital switch board receives an average of 4 emergency calls in a 10 minutes interval. What is the probability that (i)there are atleast 2 emergency calls. (ii)there are exactly 3 emergency call in an interval of 10 minutes?",
            "options": ["1.195", "0.195", "0.91"],
            "answer": "0.195",
            "explanation": "<br><br><br><b>Solution:</b><br><br>We have P(x) = <u> e^-m . m^x </u>. Here, m = 4<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x!<br><br>(i) P(X < 2) = P(X = 0) - P(X = 1) - P(X = 2)<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= <u>e^-4 . 4⁰</u> + <u>e^-4 . 4¹</u> + <u>e^-4 . 4²</u><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 0!  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;1!&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;    2!<br><br&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= e^-4(1 + 4 + 8) = 0.238<br><br>(ii) P(X = 3) = <u> e^-m . m^x </u> = <u>e^-4 . 4³</u> = 0.195<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; x!  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; 3! ",
        },
        {
            "question": "<br>➢A variable X follows a Poisson distribution with variance 3. Calculate (i) P(X = 2) (ii)P(X > 4)",
            "options": ["0.53", "1.353", "0.353"],
            "answer": "0.353",
            "explanation": "<br><br><br><b>Solution:</b><br><br>We have P(x) = <u> e^-m . m^x </u>. Here, x = 0,1,2.....<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x!<br><br>∴P(X = 2) = <u> e^-3 . 3² </u>.  = 0.224<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2!<br><br>∴P(X > 4) = 1 - [P(X = 0) + P(X = 1) + P(X = 2) + P(X = 3)]<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;= 1 - 0.647 = 0.353 ",
        },
        {
            "question": "<br>➢If X and Y are independent Poisson variates with mean m1 and m2, find the probability that X + Y = k.",
            "options": ["k = 1,2", "k = 0,1,2", "k = 1,2,3"],
            "answer": "k = 0,1,2",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Since X, Y are independent Poisson variates with parameters m1 and m2, Z = X + Y is also a Poission variate with parameter m1 + m2.<br><br> ∴ P(Z = k) = <u>e^(m1+m2) (m1+m2)^k</u> , k = 0,1,2<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;k!",
        },
        {
            "question": "<br>➢If X, Y are independent Poission variates with mean 2 and 3, find the variance of 3X - 2Y.",
            "options": ["30", "40", "60"],
            "answer": "30",
            "explanation": "<br><br><br><b>Solution:</b><br><br> For Poission variate mean variance are equal.<br><br>Hence, Var. X = 2 and Var, Y = 3.<br><br> Since, X, Y are independent <br><br> Var. (3X - 2Y) = 9 Var(X) + 4 Var (Y) = 9(2) + 4(3) = 30",
        },
        {
            "question": "<br>➢An insurance company found that only 0.01% of the population is involved in a certain type of accident each year. If its 1000 policy holders were randomly selected from the population, what is the probability that no more than two clients are involved in such accident next year ?",
            "options": ["0.9998", "0.9999", "1.9998"],
            "answer": "0.9998",
            "explanation": "<br><br><br><b>Solution:</b><br><br> An insurance company found that only 0.01% of the population is involved in a certain type of accident each year. If its 1000 policy holders were randomly selected from the population, what is the probability that no more than two clients are involved in such accident next year ?<br><br>We have p = <u>0.01</u> = 0.0001, n = 1000 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;100<br><br>∴ m = np = 1000 * 0.001 = 0.1<br><br>∴ P(X = x) = e^0.1 <u>(0.1)^x</u><br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x!<br><br>∴ P(X < 2) = P(X = 0) + P(X = 1) + P(X = 2)∴ P(X < 2) = e^0.1[<u>(0.1)⁰</u> + <u>(0.1)¹</u> + <u>(0.1)²</u>] = 0.9998<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [  0!  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp; 1!  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;  2!]",
        },
        
        
    ],
    'LinearProgrammingProblems': [
        {
            "question": "<br>➢Express the following L.P.P in the standard matrix form.<br>Maximize z = 2x1 + 3x2 + 6x3<br>subject to 3x1 - 2x2+ 4x3 < 5 <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x1 + 5x2 = 10 <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1 + 2x2 + x3 < 2<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2, x3 > 0",
            "options": ["c = [2 3 3 0 0]", "c = [2 3 6 0 0]", "c = [2 3 0 0 0]"],
            "answer": "c = [2 3 6 0 0]",
            "explanation": "<br><br><br><b>Solution:</b><br><br>Introducing slack variables s1 and s3 both (> 0), we have<br><br>Maximize z = 2x1 + 3x2 + 6x3<br>subject to 3x1 - 2x2+ 4x3 < 5 <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x1 + 5x2 = 10 <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1 + 2x2 + x3 < 2<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2, x3 > 0<br><br>The constraints can be written in the matrix form as <br><br>[ 3 -2 4 1 0 ] [x1] = [5]<br>[ 2 5 0 0 0 ]&nbsp;&nbsp;[x2]   [10]<br>[ 1 2 1 0 -1 ] [x3] [2] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s1] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s2]<br> i.e Ax=b<br><br>Thus, the problem in the matrix form becomes:<br><br>Maximize z = cx<br>subject to Ax = b, x>0<br>where<br><br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 3 -2 4 1 0 ]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [x1] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; [5]<br>A = [ 2 5 0 0 0 ]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x2]  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; b = [10], c = [ 2 3 6 0 0 ]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[ 1 2 1 0 -1 ] &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x =  [x3]&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[2] <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s1]<br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[s2] ",
        },
        {
            "question": "<br>➢Convert the following L.P.P in the standard form<br> Maximise  z = 3x1 + 5x2<br>subject to 3x1 + 2x2 < 15 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2x1 + 5x2 > 12<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2 >0",
            "options": ["z = 3x1 + 5x2 + 0s1 + 0s2", "z = 3x1 + 5x2 + 0s1 - 0s2", "z = 3x1 + 5x2 + s1 + s2"],
            "answer": "z = 3x1 + 5x2 + 0s1 + 0s2",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Introducing the slack variables the problem can be converted to standard form as:<br><br>Maximise  z = 3x1 + 5x2 + 0s1 + 0s2<br>subject to 3x1 + 2x2 + s1 + 0s2 = 15 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 2x1 + 5x2 + 0s1 -s2 = 12<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2, s1, s2 >0",
        },
        {
            "question": "<br>➢Convert the following L.P.P in the standard form<br> Maximise  z = -3x1 + 2x2 - x3<br>subject to -3x2  2x3 > -6 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; 3x1 + 4x3 < 3<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;-3x1 + 5x2 < 4<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2 >0, x3 is unrestricted",
            "options": ["z = -z = 3x1 - 2x2 + x3 - x3 + 0s1 + s2 + s3", "z = -z = 3x1 - 2x2 + x3 - x3 + 0s1 + 0s2 + 0s3", "z = -z = 3x1 + 2x2 - x3 - x3 + 0s1 + 0s2 + 0s3"],
            "answer": "z = -z = 3x1 - 2x2 + x3 - x3 + 0s1 + 0s2 + 0s3",
            "explanation": "<br><br><br><b>Solution:</b><br><br> ",
        },
        {
            "question": "<br>➢Is the solution x1 = 1, x2 = 1/2, x = 0, x4 = 0, x5 = 0 a basic solution of the following problem? Give the unbounded solution <br> x1 + 2x2 + x3 + x4 = 2  <br> x1 + 2x2 + (1/2)x3 + x5 = 2",
            "options": ["x1 + 2x1 = 2", "x1 - 2x2 = 2", "x1 + 2x2 = 1"],
            "answer": "x1 + 2x2 = 2",
            "explanation": "<br><br><br><b>Solution:</b><br><br> We can write the given system in matrix form as<br><br>[ 1 2 1 1 0 ]&nbsp;&nbsp; [x1] = [2]<br> [ 1 2 1/2 0 1] [x2] &nbsp;&nbsp; [2]<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; &nbsp;&nbsp;[x3] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x4] <br> &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;[x5]<br><br>Putting x3 = 0, x4 = 0, x5 = 0 we get<br><br>[ 1 2 ] [x1] = [2]<br>[ 1 2 ] [x2]&nbsp;&nbsp;&nbsp;[2]<br><br>Therefore, x1 + 2x2 = 2, x1 + 2x2 = 2<br><br>The system gives only one equation x1 + 2x2 = 2.",
        },
        {
            "question": "<br>➢Find the dual for the following L.P.P<br>Maximise z = x1 - 2x2 + 3x3<br>subject to -2x1 + x2 + 3x2 = 2 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x1 + 3x2 + 4x3 = 1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2, x3 > 0",
            "options": ["w = 2y1 + y2", "w = 2y1 - y2", "w = 2y1 + y1"],
            "answer": "w = 2y1 + y2",
            "explanation": "<br><br><br><b>Solution:</b><br><br> Since the problem is of maximisation type, the constraints must be expressed in leass than or equal to form,<br><br>∴ -2x1 + x2 + 3x3 > 2 and (-2x1 + x2 + 3x3)<2<br><br>i.e-(-2x1 + x2 + 3x3 > 2) and-2x1 + x2 + 3x3 < -2<br><br>Also 2x1 + 3x2 + 4x3 > 1 and 2x1 + 3x2 + 4x3 < 1 <br><br>Hence, the given problem becomes,<br>Maximise z = x1 - 2x2 + 3x3<br>subject to -2x1 + x2 + 3x2 < 2 <br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2x1 + 3x2 + 4x3 < 1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;x1, x2, x3 > 0<br><br>Therefore the problem becomes<br>Minimize w = 2y1 + y2<br>Subject to -2y1 + 2y2 > 1<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;y1 + 3y2 > -2<br>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3y1 + 4y2 > 3",
        },
        
        
    ],
    'NonLinearProgrammingProblems': [
        {
            "question": "8 - 4",
            "options": ["2", "4", "6"],
            "answer": "4",
            "explanation": "8 minus 4 equals 4.",
        },
        {
            "question": "2 - 4",
            "options": ["-2", "4", "6"],
            "answer": "-2",
            "explanation": "2 minus 4 equals -2.",
        },
        {
            "question": "8 - 2",
            "options": ["2", "4", "6"],
            "answer": "6",
            "explanation": "8 minus 2 equals 6.",
        },
        {
            "question": "6 - 2",
            "options": ["2", "4", "6"],
            "answer": "4",
            "explanation": "6 minus 2 equals 4.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        {
            "question": "10 + 15",
            "options": ["12", "25", "15"],
            "answer": "25",
            "explanation": "10 plus 15 equals 25.",
        },
        
    ],

}

@app.route("/instructions")
def instructions():
    return render_template("instruction.html")
# Dictionary to store recent results of the user
recent_results = {}


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/quiz", methods=["GET", "POST"])
def quiz():
    topic = request.args.get('topic', 'laplaceTransform')  # Default to 'laplaceTransform' if topic is not provided
    current_questions = questions_by_topic.get(topic, [])
    enumerated_questions = list(enumerate(current_questions))  # Generate enumerated list

    if request.method == "POST":
        start_time = float(request.form.get("start_time", 0))  # Default to 0 if start_time is not provided
        end_time = time.time()
        elapsed_time = round(end_time - start_time, 2)

        score = 0  # Initialize score counter
        feedback = []

        for index, question in enumerated_questions:
            user_answer_key = f"answer_{topic}_{index}"
            user_answer = request.form.get(user_answer_key)
            correct_answer = question["answer"]
            if user_answer == correct_answer:
                score += 1  # Increment score if user's answer is correct
                feedback.append({
                    "user_answer": user_answer,  # Include the user's answer in feedback
                    "correct": True, 
                    "explanation": "Correct!",
                    "question": question["question"]
                })
            else:
                feedback.append({
                    "user_answer": user_answer,  # Include the user's answer in feedback
                    "correct_answer": correct_answer,  # Include the correct answer in feedback
                    "correct": False,
                    "explanation": f"Wrong! The correct answer is {correct_answer}. {question['explanation']}",
                    "explanation_available": True,  # Indicate that explanation is available
                    "question": question["question"]  # Include the question text in feedback
                })

        total_questions = len(current_questions)
        # Store the result in recent_results
        recent_results[topic] = {
            "score": score,
            "total": total_questions,
            "elapsed_time": elapsed_time,
            "feedback": feedback,
        }
        return render_template(
            "result.html",
            score=score,
            total=total_questions,
            elapsed_time=elapsed_time,
            feedback=feedback,
            topic=topic,  # Pass the topic variable to the template
        )
    else:
        return render_template("quiz.html", questions=enumerated_questions, topic=topic, start_time=time.time())


@app.route("/back_to_questions/<topic>")
def back_to_questions(topic):
    # Redirect to the quiz page for the specified topic
    return redirect(url_for('quiz', topic=topic))


@app.route("/exit")
def exit_quiz():
    return render_template("exit.html")


@app.route("/recent_result/<topic>")
def recent_result(topic):
    # Fetch the recent result of the user for the specified topic
    result_data = recent_results.get(topic, {})
    return render_template("result.html", **result_data)


@app.route("/topic_selection")
def topic_selection():
    return render_template("topic_selection.html")


if __name__ == "__main__":
    app.run(debug=True)







