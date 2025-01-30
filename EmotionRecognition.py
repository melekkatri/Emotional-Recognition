
from fer import FER

# Create an FER object to detect emotions
detector = FER()

# Define the emotions to detect
emotions = ['angry', 'disgust', 'fear', 'happy', 'sad', 'surprise', 'neutral']

image = r"C:\Users\Melek\Desktop\Sad.webp"
results = detector.detect_emotions(image)

for result in results:
        x, y, w, h = result['box']

        # Loop through the detected emotions and print the dominant one
for emotion, score in result['emotions'].items():
        if emotion in emotions:
             if score > 0.5:
                     print(emotion)
