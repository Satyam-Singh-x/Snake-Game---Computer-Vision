import cv2
import cvzone
import numpy as np
import math
import random
from HandTrackingModule import HandDetector

# ---------------- Camera Setup ---------------- #
cap = cv2.VideoCapture(0, cv2.CAP_MSMF)

if not cap.isOpened():
    print("Trying camera index 1...")
    cap = cv2.VideoCapture(1, cv2.CAP_MSMF)

if not cap.isOpened():
    print("❌ ERROR: Camera not available")
    exit()

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)

print("🎥 Webcam started")

detector = HandDetector(detectionCon=0.8, maxHands=1)

# ---------------- Snake Game ---------------- #
class SnakeGameClass:
    def __init__(self, foodPath, headPath):
        self.imgFood = cv2.imread(foodPath, cv2.IMREAD_UNCHANGED)
        self.imgHead = cv2.imread(headPath, cv2.IMREAD_UNCHANGED)

        if self.imgFood is None or self.imgHead is None:
            print("❌ Food or Snake image not found")
            exit()

        self.hFood, self.wFood, _ = self.imgFood.shape
        self.resetGame()

    def resetGame(self):
        self.points = []
        self.lengths = []
        self.currentLength = 0
        self.allowedLength = 150
        self.prevHead = None
        self.score = 0
        self.gameOver = False
        self.randomFoodLocation()

    def randomFoodLocation(self):
        self.foodPoint = random.randint(100, 1180), random.randint(100, 620)

    def update(self, img, head):
        if self.gameOver:
            cvzone.putTextRect(img, "GAME OVER", (420, 280), scale=4, thickness=4)
            cvzone.putTextRect(img, f"Score: {self.score}", (470, 350), scale=3)
            cvzone.putTextRect(img, "Press R to Restart", (400, 420), scale=2)
            return img

        cx, cy = head
        if self.prevHead is None:
            self.prevHead = (cx, cy)

        px, py = self.prevHead
        self.points.append((cx, cy))
        dist = math.hypot(cx - px, cy - py)
        self.lengths.append(dist)
        self.currentLength += dist
        self.prevHead = (cx, cy)

        while self.currentLength > self.allowedLength:
            self.currentLength -= self.lengths.pop(0)
            self.points.pop(0)

        fx, fy = self.foodPoint
        if abs(cx - fx) < self.wFood // 2 and abs(cy - fy) < self.hFood // 2:
            self.randomFoodLocation()
            self.allowedLength += 40
            self.score += 1

        for i in range(1, len(self.points)):
            cv2.line(img, self.points[i - 1], self.points[i], (0, 255, 255), 20)

        img = cvzone.overlayPNG(img, self.imgHead, (cx - 30, cy - 30))
        img = cvzone.overlayPNG(
            img,
            self.imgFood,
            (fx - self.wFood // 2, fy - self.hFood // 2),
        )

        cvzone.putTextRect(img, f"Score: {self.score}", (40, 80), scale=3)

        if len(self.points) > 10:
            pts = np.array(self.points[:-4], np.int32)
            if cv2.pointPolygonTest(pts, (cx, cy), True) > -10:
                self.gameOver = True

        return img


# ---------------- Game Init ---------------- #
game = SnakeGameClass(
    "D:\AdvancedML\Snake Game\donut.png",
    "D:\AdvancedML\Snake Game\snake_transparent.png",
)

# ---------------- Main Loop ---------------- #
while True:
    success, img = cap.read()
    if not success or img is None:
        print("❌ Empty frame")
        continue

    img = cv2.flip(img, 1)
    img = detector.findHands(img, draw=False)
    lmList = detector.findPosition(img, draw=False)

    if lmList:
        cx, cy = lmList[8][1], lmList[8][2]
        img = game.update(img, (cx, cy))

    cv2.imshow("🐍 Snake Game", img)

    key = cv2.waitKey(1)
    if key == 27:
        break
    elif key == ord("r"):
        game.resetGame()

cap.release()
cv2.destroyAllWindows()
