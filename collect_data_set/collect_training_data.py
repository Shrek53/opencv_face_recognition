import os, sys
import glob
import cv2

cam = cv2.VideoCapture(0)
cv2.namedWindow("Capture Images")
img_counter = 0
folder_name = input("Enter person name: ")
folder_path = './dataset/{}/'.format(folder_name)
if not os.path.isdir(folder_path):
    os.mkdir(folder_path)
else:
    files = file_count = glob.glob(folder_path + '*.*')
    file_count_in_folder = len(files)
    # print('number of files - {}'.format(file_count_in_folder))
    img_counter = file_count_in_folder

while True:
    ret, frame = cam.read()
    cv2.imshow("Capture Images", frame)
    if not ret:
        break
    k = cv2.waitKey(1)

    if k % 256 == 27:
        # ESC pressed
        print("Escape hit, closing...")
        break
    elif k % 256 == 32:
        # SPACE pressed
        img_name = "./dataset/{}/opencv_frame_{}.png".format(folder_name, img_counter)
        cv2.imwrite(img_name, frame)
        print("{} written!".format(img_name))
        img_counter += 1

cam.release()

cv2.destroyAllWindows()
