# from keras.models import load_model
# import cv2
# import numpy as np
# import os

# os.chdir('D:/Anirudh/pythonprojects/envs/auto-py-to-exe36/rock-paper-scissors-master')

# filepath = 'D:/Anirudh/pythonprojects/envs/auto-py-to-exe36/rock-paper-scissors-master/image_data/test'

# REV_CLASS_MAP = {
#     0: "rock",
#     1: "paper",
#     2: "scissors",
#     3: "none"
# }


# def mapper(val):
#     return REV_CLASS_MAP[val]


# model = load_model("rock-paper-scissors-model.h5")
# filelen = 200

# for val in range(filelen):
#     # prepare the image
#     path = filepath + '/' + str(val + 1) + '.jpg'
#     img = cv2.imread(path)
#     img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
#     img = cv2.resize(img, (227, 227))

#     # predict the move made
#     pred = model.predict(np.array([img]))
#     move_code = np.argmax(pred[0])
#     move_name = mapper(move_code)
#     print("Predicted: {}".format(move_name))

#     with open('test.txt', 'a') as file:
#         file.write('\n')
#         file.write("Predicted: {}".format(move_name))


from keras.models import load_model
import cv2
import numpy as np

REV_CLASS_MAP = {
    0: "rock",
    1: "paper",
    2: "scissors",
    3: "none"
}

def mapper(val):
    return REV_CLASS_MAP[val]

model = load_model("rock-paper-scissors-model.h5")
cap = cv2.VideoCapture(0)

while True:
    frame = cap.read()[1]
    cv2.imshow('Live', frame)
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    frame = cv2.resize(frame, (227, 227))
    pred = model.predict(np.array([frame]))
    move_code = np.argmax(pred[0])
    move_name = mapper(move_code)
    print("Predicted: {}".format(move_name))
    key = cv2.waitKey(10)
    if key == 27:
        break

cap.release()
cv2.destroyAllWindows()