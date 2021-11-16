import cv2
import os



img_dirs = os.listdir('./imgs/combine')
black_cnt, color_cnt = 0, 0

for img_dir in img_dirs:
    img = cv2.imread(os.path.join('./imgs/combine', img_dir))
    img = cv2.resize(img, dsize=(286, 286), interpolation=cv2.INTER_AREA)
    cv2.imshow('classification', img)
    keycode = cv2.waitKey()
    if keycode == ord('q'):
        break

    elif keycode == ord('c'):
        cv2.imwrite(f'./color/{color_cnt:04}.jpg', img)
        color_cnt += 1

    elif keycode == ord('b'):
        cv2.imwrite(f'./black/{black_cnt:04}.jpg', img)
        black_cnt += 1

cv2.destroyAllWindows()






