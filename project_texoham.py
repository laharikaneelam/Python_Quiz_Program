import time
import math
import random
from datetime import datetime

def loadQuestions():
    sQuizFile = "C:\\Users\\Laharaika\\Desktop\\Python_Django\\python_practise_programs\\QuizQuestions.txt"
    quizFileHandler = open(sQuizFile)

    for line in quizFileHandler:
        lstQuestions = line.split(',')

        sQNum, sQ, sOptA, sOptB, sOptC, sOptD, sAnswer = \
            lstQuestions[0].strip(), lstQuestions[1].strip(), lstQuestions[2].strip(), \
            lstQuestions[3].strip(), lstQuestions[4].strip(), lstQuestions[5].strip(), \
            lstQuestions[6].strip()

        dictQuestions[sQNum] = [sQ, f"A. {sOptA}", f"B. {sOptB}", f"C. {sOptC}", f"D. {sOptD}", sAnswer]

    iMaxQuestions = len(dictQuestions)

    quizFileHandler.close()
    return iMaxQuestions



def getNumberOfQuestions(aiMaxNumOfQuestions):
    print(f"*** There are {aiMaxNumOfQuestions} questions in the quiz bank.***")
    while True:
        sNum = input("How many questions do you want to answer?").strip()
        if not sNum.isnumeric():
            print(sNum, " is not a valid integer. Try again")
        else:
            iNum = int(sNum)
            if iNum < 1 or iNum > aiMaxNumOfQuestions:
                print(f"Please enter a number between 1 and {aiMaxNumOfQuestions}. Try again ")
            else:
                break
    return iNum



def setQuestionPaper(aiNumOfQsToAsk, aiMaxNumOfQsInDB):
    rLstQuestionsToAsk = []
    while True:
        sRandomQuestionNum = str(random.randint(1, aiMaxNumOfQsInDB))
        if sRandomQuestionNum in rLstQuestionsToAsk:
            continue
        else:
            rLstQuestionsToAsk.append(sRandomQuestionNum)
        if len(rLstQuestionsToAsk) == aiNumOfQsToAsk:
            break
    return rLstQuestionsToAsk



def askQuestion(asAskQNum, asDictQNum):
    while True:
        setQandAs = dictQuestions[asDictQNum]
        rtnsQuestion = "{0}\n\t{1}\n\t{2}\n\t{3}\n\t{4}".format(*setQandAs)

        rtnsUserAnswer = input(f"{asAskQNum}. {rtnsQuestion}\n"
                                   f"Please type your answer here:")

        rtnsUserAnswer = rtnsUserAnswer.strip().upper()
        if rtnsUserAnswer not in ("A", "B", "C", "D"):
            print(f"Sorry, your answer {rtnsUserAnswer} is not understood. Try Again")
        else:
            break
    rtnsCorrectAnswer = setQandAs[5]
    return rtnsQuestion, rtnsUserAnswer, rtnsCorrectAnswer



iQuizScore, iScorePerQuestion, iSleepTime = 0, 3, 1
dictQuestions = {}

iMaxNumQuestions = loadQuestions()

iNumOfQuestionsToAsk = getNumberOfQuestions(iMaxNumQuestions)
iMaxScore = iNumOfQuestionsToAsk*iScorePerQuestion

lstQuestionsToAsk = setQuestionPaper(iNumOfQuestionsToAsk, iMaxNumQuestions)
print(f"You will be asked {iNumOfQuestionsToAsk} Questions. All the Best")

dtStartTime = datetime.now()
sStartTime = dtStartTime.strftime("%d-%m-%Y  %H-%M-%S")
slogFile = f"C:\\Users\\Laharaika\\Desktop\\Python_Django\\python_practise_programs\\{sStartTime} -Quiz.txt"
logFileHandler = open(slogFile, "a")

logFileHandler.write(F"There are {iMaxNumQuestions} questions in the quiz database.\n")
logFileHandler.write(F"---> You chose to answer {len(lstQuestionsToAsk)}\n")
logFileHandler.write(F"You started your quiz at {sStartTime}\n")
time.sleep(iSleepTime)



iLoopCounter = 0
for sQuestionNum in lstQuestionsToAsk:
    iLoopCounter = iLoopCounter + 1
    (sQuestion, sGivenAnswer, sCorrAnswer) = askQuestion(iLoopCounter, sQuestionNum)
    if sGivenAnswer == sCorrAnswer:
        sMessageToPrint = f" {sGivenAnswer} is the right answer!! "
        iQuizScore = iQuizScore + iScorePerQuestion
    else:
        sMessageToPrint = f"Sorry! {sGivenAnswer} is not the right answer. Correct Answer is {sCorrAnswer}!!!"
    print(sMessageToPrint)
    logFileHandler.write(F"{iLoopCounter}. {sQuestion}\n")
    logFileHandler.write(F" Your answer{sGivenAnswer}. Correct Answer is {sCorrAnswer}\n")
    sMessageToPrint = f"----> Your score so far is {iQuizScore}/{iMaxScore}"
    logFileHandler.write(f"{sMessageToPrint}\n")
    print(sMessageToPrint)
    time.sleep(iSleepTime)



sMessageToPrint = f"Your final score is {iQuizScore}/{iMaxScore}"
logFileHandler.write(f"{sMessageToPrint}\n")
print(f"{sMessageToPrint}")
dtEndTime = datetime.now()
sEndTime = dtEndTime.strftime("%d-%m-%Y %H-%M-%S")
logFileHandler.write(F" You Completed the Quiz at {sEndTime}\n")
tTimeDelta = dtEndTime - dtStartTime
sMessageToPrint = F"You took {math.ceil(tTimeDelta.seconds/(60*60)-1)} hours, "\
                  F"{math.ceil(tTimeDelta.seconds/60%60 - 1)} minutes, and"\
                  F"{round(tTimeDelta.seconds%60)} seconds to complete the quiz.\n" \
                  F"A log file containing the quiz questions and results is available at {slogFile}"
logFileHandler.write(f"{sMessageToPrint}\n")
print(sMessageToPrint)
logFileHandler.close()
