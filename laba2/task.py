import jetFunctions as jet

# print("кол-во шагов в цикле: ")
# loop_steps = int(input())
samplesInMeasure = 1 # кол-во сэмплов в измерении
print("кол-во точек: ")
moves = int(input())

counter = moves


# врубаем
jet.initSpiAdc()
jet.initStepMotorGpio()

measures = []

 
while counter > 3*moves/4:
    measures.append(jet.getMeanAdc(samplesInMeasure))
    jet.stepForward(1)
    counter = counter - 1

while counter > moves/4:
    measures.append(jet.getMeanAdc(samplesInMeasure))
    jet.stepBackward(1)
    counter = counter - 1

while counter > 0:
    measures.append(jet.getMeanAdc(samplesInMeasure))
    jet.stepForward(1)
    counter = counter - 1


# сохраняем файл
jet.save(measures, moves)


# вырубаем 
jet.deinitSpiAdc()
jet.deinitSpiAdc()


