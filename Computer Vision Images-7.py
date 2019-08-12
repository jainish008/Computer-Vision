import cv2

src1 = cv2.imread('club.jpg')
src2 = cv2.imread('bmwgold.jpg')

src2 = cv2.resize(src2, src1.shape[1::-1])

dst = cv2.addWeighted(src1, 0.5, src2, 0.5, 0)

cv2.imwrite('club_bmw.jpg', dst)