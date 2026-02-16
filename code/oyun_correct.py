import os
import re

import jpype

if not jpype.isJVMStarted():
    jar_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'oyun-correct-3.0.4-jar-with-dependencies.jar')
    jpype.startJVM(jvmpath=jpype.getDefaultJVMPath(), classpath=[jar_path])

OyunCorrector = jpype.JClass("com.oyun.OyunCorrector")


def oyun_correct(text):
    start_ws, text, end_ws = re.match(pattern="([ \t\n\r\f]*)(.*?)([ \t\n\r\f]*)$", string=text, flags=re.S).groups()
    text = str(OyunCorrector.correct(text))
    text = re.sub(pattern="\u202F(?![\u1820-\u1842])", repl=" ", string=text)
    text = re.sub(pattern="\u202F", repl="\u180E", string=text)
    return start_ws + text + end_ws
