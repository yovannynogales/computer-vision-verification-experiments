from deepface import DeepFace
import matplotlib.pyplot as plt
import cv2

img_path = 'data/faces/samples/img11.jpeg' # Enter Your Image Path
img = cv2.imread(img_path)

result = DeepFace.analyze(img, actions=['age', 'gender', 'emotion'])

result = result[0]

plt.imshow(cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
plt.axis('off')
plt.show()

print(f"Age: {result['age']}")
print(f"Gender: {result['gender']}")
print(f"Dominant Emotion: {result['dominant_emotion']}")