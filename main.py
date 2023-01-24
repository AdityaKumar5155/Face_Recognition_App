try:
    from sklearn import tree
except:
    print("sklearn is not installed, Install it by 'python -m pip install sklearn'")
    input("Press Enter to exit!")
    exit()
try:
    import cv2
except:
    print("cv2 is not installed, Install it by 'python -m pip install opencv-python'")
    input("Press Enter to exit!")
    exit()
import webbrowser
rick_switch = 0
# from time import sleep

features = []
labels = []
clf = tree.DecisionTreeClassifier()
n = int(input("How many scenes you want to capture? : "))
vid = cv2.VideoCapture(1)

frames = 0
labelId = 0
feature = []

try:
    while True:
        if frames <= 50:
            # Capture the video frame
            # by frame
            ret, frame = vid.read()
            cv2.imshow('frame', frame)
            rows, cols = frame.shape[:2]

            for i in range(rows):
                for j in range(cols):
                    k = frame[i, j]
                    feature.append(k[0])
                    feature.append(k[1])
                    feature.append(k[2])
            features.append(feature)
            labels.append(labelId)
            feature = []
            frames = frames + 1
        elif labelId < n - 1:
            input("Press Enter to continue!")
            frames = 0
            labelId = labelId + 1
            continue
        else:
            feature = []  # Freed some RAM by erasing unnecessary variable
            break
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()

    clf = clf.fit(features, labels)
    print("TRAINING SUCCESSFUL!!!")
except:
    print("Enough RAM not available!")
    print("Try to reduce the number of scenes and try again!")
    input("To exit press Enter!")
    exit()

input("Press Enter to Test Program")

feature2 = []
vid2 = cv2.VideoCapture(1)
while True:
    ret, frame2 = vid2.read()
    cv2.imshow('frame', frame2)
    rows, cols = frame2.shape[:2]

    frameData = []
    feature2 = []

    for i in range(rows):
        for j in range(cols):
            z = frame2[i, j]
            feature2.append(z[0])
            feature2.append(z[1])
            feature2.append(z[2])
    frameData = feature2

    print(clf.predict([frameData]))
    
    # if (clf.predict([frameData]) == 2 and rick_switch == 0):
    #     webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    #     rick_switch = 1

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid2.release()
cv2.destroyAllWindows()
input("PROGRAM COMPLETE!!!")
