import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox
# import matplotlib.pyplot as plt

def count(object:str,image_path:str):
    # Load the image
    image = cv2.imread(image_path)

    # Detect common objects in the image
    # boxes, labels, confidences = cv.detect_common_objects(image,0.5,0.3,'yolov3')
    boxes, labels, confidences = cv.detect_common_objects(image)

    # Draw bounding boxes on the image
    output = draw_bbox(image, boxes, labels, confidences)
    # output_rgb = cv2.cvtColor(output, cv2.COLOR_BGR2RGB)
    cv2.imwrite('./images/output.png',output)

    # # Display the images
    # plt.figure(figsize=(10, 10))
    # plt.axis('off')
    # plt.imshow(output_rgb)
    # plt.show()

    num_cars = labels.count(object)
    return (f"Number of {object}: {num_cars}",output)

if __name__ == '__main__':
    test = count('car','./images/cars.png')
    print(test[0])
    cv2.imwrite('./images/output.png',test[1])
