def displayTheGeometricScoreAndBonusValues():
    global triangleBonus, triangleScore, leftTriangleBonus, leftTriangleScore, diamondBonus, diamondScore, smallDiamondBonus, smallDiamondScore, squareBonus, squareScore, smallSquareBonus, smallSquareScore, geometricSectionListIndex
    triangleBonus = 0
    triangleScore = 1
    leftTriangleBonus = 1
    leftTriangleScore = 0
    diamondBonus = 0
    diamondScore = 0
    smallDiamondBonus = 0
    smallDiamondScore = 0
    squareBonus = 2
    squareScore = 0
    smallSquareBonus = 0
    smallSquareScore = 0
    while True:
        if triangle:
            if input.button_is_pressed(Button.A):
                if triangleScore < 5:
                    triangleScore += 1
                    basic.show_number(triangleScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(triangle)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and animalSectionListIndex != 0:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if triangleScore <= 0:
                    basic.show_string("Press A")
                else:
                    triangleScore += -1
                    basic.show_number(triangleScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(triangle)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 0:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif left_triangle:
            if input.button_is_pressed(Button.A):
                if leftTriangleScore < 5:
                    leftTriangleScore += 1
                    basic.show_number(leftTriangleScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(left_triangle)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 1:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if leftTriangleScore <= 0:
                    basic.show_string("Press A")
                else:
                    leftTriangleScore += -1
                    basic.show_number(leftTriangleScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(left_triangle)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 1:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif diamond:
            if input.button_is_pressed(Button.A):
                if diamondScore < 5:
                    diamondScore += 1
                    basic.show_number(diamondScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(diamond)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 2:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if diamondScore <= 0:
                    basic.show_string("Press A")
                else:
                    diamondScore += -1
                    basic.show_number(diamondScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(diamond)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 2:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif small_diamond:
            if input.button_is_pressed(Button.A):
                if smallDiamondScore < 5:
                    smallDiamondScore += 1
                    basic.show_number(smallDiamondScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(small_diamond)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 3:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if smallDiamondScore <= 0:
                    basic.show_string("Press A")
                else:
                    smallDiamondScore += -1
                    basic.show_number(smallDiamondScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(small_diamond)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 3:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif square:
            if input.button_is_pressed(Button.A):
                if squareScore < 5:
                    squareScore += 1
                    basic.show_number(squareScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(square)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 4:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if squareScore <= 0:
                    basic.show_string("Press A")
                else:
                    squareScore += -1
                    basic.show_number(squareScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(square)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 4:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif small_square:
            if input.button_is_pressed(Button.A):
                if smallSquareScore < 5:
                    smallSquareScore += 1
                    basic.show_number(smallSquareScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(small_square)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 5:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if smallSquareScore <= 0:
                    basic.show_string("Press A")
                else:
                    smallSquareScore += -1
                    basic.show_number(smallSquareScore)
                    if input.logo_is_pressed():
                        while True:
                            geometricSectionListIndex = 0
                            geometricSectionSelectedImagesList.append(small_square)
                            while geometricSectionListIndex <= len(geometricSectionList) - 1 and geometricSectionListIndex != 5:
                                geometricSectionList[geometricSectionListIndex].show_image(0)
                                basic.pause(2000)
                                geometricSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheGeometricScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        else:
            displayEmotionSectionImages()
def displayAnimalSectionImages():
    global animalSectionListIndex
    while True:
        animalSectionListIndex = 0
        while animalSectionListIndex <= len(animalSectionList) - 1:
            if len(animalSectionSelectedImagesList) <= 3:
                animalSectionList[animalSectionListIndex].show_image(0)
                basic.pause(2000)
                animalSectionListIndex += 1
                if input.logo_is_pressed():
                    displayTheAnimalScoreAndBonusValues()
                else:
                    continue
            else:
                break
def displayEmotionSectionImages():
    global emotionSectionListIndex
    while True:
        emotionSectionListIndex = 0
        while emotionSectionListIndex <= len(emotionSectionList) - 1:
            if len(emotionSectionSelectedImagesList) <= 3:
                emotionSectionList[emotionSectionListIndex].show_image(0)
                basic.pause(2000)
                emotionSectionListIndex += 1
                if input.logo_is_pressed():
                    displayTheEmotionScoreAndBonusValues()
                else:
                    continue
            else:
                break
def displayTheAnimalScoreAndBonusValues():
    global duckBonus, duckScore, triangleScore, turtleScore, butterflyBonus, butterflyScore, giraffeBonus, giraffeScore, snakeBonus, snakeScore, rabbitBonus, rabbitScore, cowBonus, cowScore, animalSectionListIndex
    duckBonus = 1
    duckScore = 0
    triangleScore = 1
    turtleScore = 0
    butterflyBonus = 1
    butterflyScore = 0
    giraffeBonus = 0
    giraffeScore = 0
    snakeBonus = 1
    snakeScore = 0
    rabbitBonus = 1
    rabbitScore = 0
    cowBonus = 1
    cowScore = 0
    while True:
        if duck:
            if input.button_is_pressed(Button.A):
                if duckScore < 5:
                    duckScore += 1
                    basic.show_number(duckScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(duck)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 0:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if duckScore <= 0:
                    basic.show_string("Press A")
                else:
                    duckScore += -1
                    basic.show_number(duckScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(duck)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 0:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif turtle:
            if input.button_is_pressed(Button.A):
                if turtleScore < 5:
                    turtleScore += 1
                    basic.show_number(turtleScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(turtle)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 1:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if turtleScore <= 0:
                    basic.show_string("Press A")
                else:
                    turtleScore += -1
                    basic.show_number(turtleScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(turtle)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 1:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif butterfly:
            if input.button_is_pressed(Button.A):
                if butterflyScore < 5:
                    butterflyScore += 1
                    basic.show_number(butterflyScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(butterfly)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 2:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if butterflyScore <= 0:
                    basic.show_string("Press A")
                else:
                    butterflyScore += -1
                    basic.show_number(butterflyScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(butterfly)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 2:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif giraffe:
            if input.button_is_pressed(Button.A):
                if giraffeScore < 5:
                    giraffeScore += 1
                    basic.show_number(giraffeScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(giraffe)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 3:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if giraffeScore <= 0:
                    basic.show_string("Press A")
                else:
                    giraffeScore += -1
                    basic.show_number(giraffeScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(giraffe)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 3:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif snake:
            if input.button_is_pressed(Button.A):
                if snakeScore < 5:
                    snakeScore += 1
                    basic.show_number(snakeScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(snake)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 4:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if snakeScore <= 0:
                    basic.show_string("Press A")
                else:
                    snakeScore += -1
                    basic.show_number(snakeScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(snake)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 4:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif rabbit:
            if input.button_is_pressed(Button.A):
                if rabbitScore < 5:
                    rabbitScore += 1
                    basic.show_number(rabbitScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(rabbit)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 5:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if rabbitScore <= 0:
                    basic.show_string("Press A")
                else:
                    rabbitScore += -1
                    basic.show_number(rabbitScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(rabbit)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 5:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif cow:
            if input.button_is_pressed(Button.A):
                if cowScore < 5:
                    cowScore += 1
                    basic.show_number(cowScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(cow)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 6:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if cowScore <= 0:
                    basic.show_string("Press A")
                else:
                    cowScore += -1
                    basic.show_number(cowScore)
                    if input.logo_is_pressed():
                        while True:
                            animalSectionListIndex = 0
                            animalSectionSelectedImagesList.append(cow)
                            while animalSectionListIndex <= len(animalSectionList) - 1 and animalSectionListIndex != 6:
                                animalSectionList[animalSectionListIndex].show_image(0)
                                basic.pause(2000)
                                animalSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheAnimalScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        else:
            displayGeometricSectionImages()
def displayTheSections():
    sectionListIndex = 0
    while sectionListIndex <= len(sectionList) - 1:
        basic.show_string("" + (sectionList.remove_at(sectionListIndex)))
        basic.pause(1000)
        if animalSection:
            if input.logo_is_pressed():
                animalParticipantsListIndex = 0
                while animalParticipantsListIndex <= len(animalParticipantsList) - 1:
                    basic.show_string("" + (animalParticipantsList.remove_at(animalParticipantsListIndex)))
                    basic.pause(1000)
                    for animalParticipantsListIndex2 in animalParticipantsList:
                        if input.logo_is_pressed():
                            displayAnimalSectionImages()
                        else:
                            continue
                    animalParticipantsListIndex += 1
            else:
                continue
        elif geometricSection:
            if input.logo_is_pressed():
                geometricParticipantsListIndex = 0
                while geometricParticipantsListIndex <= len(geometricParticipantsList) - 1:
                    basic.show_string("" + (geometricParticipantsList.remove_at(geometricParticipantsListIndex)))
                    basic.pause(1000)
                    for geometricParticipantsListIndex2 in geometricParticipantsList:
                        if input.logo_is_pressed():
                            displayGeometricSectionImages()
                        else:
                            continue
                    geometricParticipantsListIndex += 1
            else:
                continue
        elif emotionSection:
            if input.logo_is_pressed():
                emotionParticipantsListIndex = 0
                while emotionParticipantsListIndex <= len(emotionParticipantsList) - 1:
                    basic.show_string("" + (emotionParticipantsList.remove_at(emotionParticipantsListIndex)))
                    basic.pause(1000)
                    for emotionParticipantsListIndex2 in emotionParticipantsList:
                        if input.logo_is_pressed():
                            displayGeometricSectionImages()
                        else:
                            continue
                    emotionParticipantsListIndex += 1
            else:
                continue
        sectionListIndex += 1
def displayGeometricSectionImages():
    global geometricSectionListIndex
    while True:
        geometricSectionListIndex = 0
        while geometricSectionListIndex <= len(geometricSectionList) - 1:
            if len(geometricSectionSelectedImagesList) <= 3:
                geometricSectionList[geometricSectionListIndex].show_image(0)
                basic.pause(2000)
                geometricSectionListIndex += 1
                if input.logo_is_pressed():
                    displayTheGeometricScoreAndBonusValues()
                else:
                    continue
            else:
                break
def displayTheEmotionScoreAndBonusValues():
    global happyBonus, happyScore, sadBonus, sadScore, confusedBonus, confusedScore, surprisedBonus, surprisedScore, sillyBonus, sillyScore, mehBonus, mehScore, emotionSectionListIndex
    happyBonus = 0
    happyScore = 1
    sadBonus = 0
    sadScore = 0
    confusedBonus = 0
    confusedScore = 0
    surprisedBonus = 0
    surprisedScore = 0
    sillyBonus = 1
    sillyScore = 0
    mehBonus = 0
    mehScore = 1
    while True:
        if happy:
            if input.button_is_pressed(Button.A):
                if happyScore < 5:
                    happyScore += 1
                    basic.show_number(happyScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(happy)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 0:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if happyScore <= 0:
                    basic.show_string("Press A")
                else:
                    happyScore += -1
                    basic.show_number(happyScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(happy)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 0:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif sad:
            if input.button_is_pressed(Button.A):
                if sadScore < 5:
                    sadScore += 1
                    basic.show_number(sadScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(sad)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 1:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if sadScore <= 0:
                    basic.show_string("Press A")
                else:
                    sadScore += -1
                    basic.show_number(sadScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(sad)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 1:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif confused:
            if input.button_is_pressed(Button.A):
                if confusedScore < 5:
                    confusedScore += 1
                    basic.show_number(confusedScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(confused)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 2:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if confusedScore <= 0:
                    basic.show_string("Press A")
                else:
                    confusedScore += -1
                    basic.show_number(confusedScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(confused)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 2:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif surprised:
            if input.button_is_pressed(Button.A):
                if surprisedScore < 5:
                    surprisedScore += 1
                    basic.show_number(surprisedScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(surprised)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 3:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if surprisedScore <= 0:
                    basic.show_string("Press A")
                else:
                    surprisedScore += -1
                    basic.show_number(surprisedScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(surprised)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 3:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif silly:
            if input.button_is_pressed(Button.A):
                if sillyScore < 5:
                    sillyScore += 1
                    basic.show_number(sillyScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(silly)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 4:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if sillyScore <= 0:
                    basic.show_string("Press A")
                else:
                    sillyScore += -1
                    basic.show_number(sillyScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(silly)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 4:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        elif meh:
            if input.button_is_pressed(Button.A):
                if mehScore < 5:
                    mehScore += 1
                    basic.show_number(mehScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(meh)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 5:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
                else:
                    basic.show_string("Press B")
            elif input.button_is_pressed(Button.B):
                if mehScore <= 0:
                    basic.show_string("Press A")
                else:
                    mehScore += -1
                    basic.show_number(mehScore)
                    if input.logo_is_pressed():
                        while True:
                            emotionSectionListIndex = 0
                            emotionSectionSelectedImagesList.append(meh)
                            while emotionSectionListIndex <= len(emotionSectionList) - 1 and emotionSectionListIndex != 5:
                                emotionSectionList[emotionSectionListIndex].show_image(0)
                                basic.pause(2000)
                                emotionSectionListIndex += 1
                                if input.logo_is_pressed():
                                    displayTheEmotionScoreAndBonusValues()
                                else:
                                    continue
                    else:
                        continue
            else:
                continue
        else:
            displayTheFinalStatistics()
def displayTheFinalStatistics():
    global animalSectionSelectedImagesIndex, geometricSectionSelectedImagesIndex, emotionSectionSelectedImagesIndex
    while True:
        basic.show_string("End of contest")
        animalSectionSelectedImagesIndex = 0
        basic.show_string("Animal Section")
        animalParticipantsListIndex3 = 0
        while animalParticipantsListIndex3 <= len(animalParticipantsList) - 1:
            basic.show_string("" + (animalParticipantsList.remove_at(animalParticipantsListIndex3)))
            basic.pause(1000)
            for animalParticipantsListIndex4 in animalParticipantsList:
                while animalSectionSelectedImagesIndex <= len(animalSectionSelectedImagesList) - 1:
                    animalSectionSelectedImagesList[animalSectionSelectedImagesIndex].show_image(0)
                    basic.pause(2000)
                    animalSectionSelectedImagesIndex += 1
            animalParticipantsListIndex3 += 1
        geometricSectionSelectedImagesIndex = 0
        basic.show_string("Geometric Section")
        geometricParticipantsListIndex3 = 0
        while geometricParticipantsListIndex3 <= len(geometricParticipantsList) - 1:
            basic.show_string("" + (geometricParticipantsList.remove_at(geometricParticipantsListIndex3)))
            basic.pause(1000)
            for geometricParticipantsListIndex4 in geometricParticipantsList:
                while geometricSectionSelectedImagesIndex <= len(geometricSectionSelectedImagesList) - 1:
                    geometricSectionSelectedImagesList[geometricSectionSelectedImagesIndex].show_image(0)
                    basic.pause(2000)
                    geometricSectionSelectedImagesIndex += 1
            geometricParticipantsListIndex3 += 1
        emotionSectionSelectedImagesIndex = 0
        basic.show_string("Emotion Section")
        emotionParticipantsListIndex3 = 0
        while emotionParticipantsListIndex3 <= len(emotionParticipantsList) - 1:
            basic.show_string("" + (emotionParticipantsList.remove_at(emotionParticipantsListIndex3)))
            basic.pause(1000)
            for emotionParticipantsListIndex4 in emotionParticipantsList:
                while emotionSectionSelectedImagesIndex <= len(emotionSectionSelectedImagesList) - 1:
                    emotionSectionSelectedImagesList[emotionSectionSelectedImagesIndex].show_image(0)
                    basic.pause(2000)
                    emotionSectionSelectedImagesIndex += 1
            emotionParticipantsListIndex3 += 1
emotionSectionSelectedImagesIndex = 0
geometricSectionSelectedImagesIndex = 0
animalSectionSelectedImagesIndex = 0
mehScore = 0
mehBonus = 0
sillyScore = 0
sillyBonus = 0
surprisedScore = 0
surprisedBonus = 0
confusedScore = 0
confusedBonus = 0
sadScore = 0
sadBonus = 0
happyScore = 0
happyBonus = 0
cowScore = 0
cowBonus = 0
rabbitScore = 0
rabbitBonus = 0
snakeScore = 0
snakeBonus = 0
giraffeScore = 0
giraffeBonus = 0
butterflyScore = 0
butterflyBonus = 0
turtleScore = 0
duckScore = 0
duckBonus = 0
emotionSectionSelectedImagesList: List[Image] = []
emotionSectionListIndex = 0
animalSectionSelectedImagesList: List[Image] = []
animalSectionListIndex = 0
geometricSectionSelectedImagesList: List[Image] = []
geometricSectionListIndex = 0
smallSquareScore = 0
smallSquareBonus = 0
squareScore = 0
squareBonus = 0
smallDiamondScore = 0
smallDiamondBonus = 0
diamondScore = 0
diamondBonus = 0
leftTriangleScore = 0
leftTriangleBonus = 0
triangleScore = 0
triangleBonus = 0
geometricParticipantsList: List[str] = []
emotionParticipantsList: List[str] = []
animalParticipantsList: List[str] = []
sectionList: List[str] = []
geometricSection = ""
emotionSection = ""
animalSection = ""
geometricSectionList: List[Image] = []
small_square: Image = None
square: Image = None
small_diamond: Image = None
diamond: Image = None
left_triangle: Image = None
triangle: Image = None
emotionSectionList: List[Image] = []
meh: Image = None
silly: Image = None
surprised: Image = None
confused: Image = None
sad: Image = None
happy: Image = None
animalSectionList: List[Image] = []
cow: Image = None
rabbit: Image = None
snake: Image = None
giraffe: Image = None
butterfly: Image = None
turtle: Image = None
duck: Image = None
duck = images.icon_image(IconNames.DUCK)
turtle = images.icon_image(IconNames.TORTOISE)
butterfly = images.icon_image(IconNames.BUTTERFLY)
giraffe = images.icon_image(IconNames.GIRAFFE)
snake = images.icon_image(IconNames.SNAKE)
rabbit = images.icon_image(IconNames.RABBIT)
cow = images.icon_image(IconNames.COW)
animalSectionList = [duck, turtle, butterfly, giraffe, snake, rabbit, cow]
happy = images.icon_image(IconNames.HAPPY)
sad = images.icon_image(IconNames.SAD)
confused = images.icon_image(IconNames.CONFUSED)
surprised = images.icon_image(IconNames.SURPRISED)
silly = images.icon_image(IconNames.SILLY)
meh = images.icon_image(IconNames.MEH)
emotionSectionList = [happy, sad, confused, surprised, silly, meh]
triangle = images.icon_image(IconNames.TRIANGLE)
left_triangle = images.icon_image(IconNames.LEFT_TRIANGLE)
diamond = images.icon_image(IconNames.DIAMOND)
small_diamond = images.icon_image(IconNames.SMALL_DIAMOND)
square = images.icon_image(IconNames.SQUARE)
small_square = images.icon_image(IconNames.SMALL_SQUARE)
geometricSectionList = [triangle,
    left_triangle,
    diamond,
    small_diamond,
    square,
    small_square]
animalSection = "Animal"
emotionSection = "Emotion"
geometricSection = "Geometric"
sectionList = [animalSection, emotionSection, geometricSection]
Anne = "Anne"
Jane = "Jane"
Mark = "Mark"
Sam = "Sam"
Danny = "Danny"
participantsNamesList = [Anne, Jane, Mark, Sam, Danny]
animalParticipantsList = [Anne, Jane, Mark, Sam]
emotionParticipantsList = [Jane, Mark, Sam, Danny]
geometricParticipantsList = [Anne, Mark, Sam, Danny]
while True:
    displayTheSections()
