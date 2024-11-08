import cv2 # type: ignore
import numpy as np # type: ignore
import matplotlib.pyplot as plt # type: ignore
# Load the image
image = cv2.imread('mario.jpg', cv2.IMREAD_GRAYSCALE)
# Define the Roberts operator kernels
roberts_x = np.array([[1, 0], [0, -1]], dtype=np.float32)
roberts_y = np.array([[0, 1], [-1, 0]], dtype=np.float32)
# Apply the Roberts operator
edge_x = cv2.filter2D(image, -1, roberts_x)
edge_y = cv2.filter2D(image, -1, roberts_y)
# Calculate the edge magnitude
edge_magnitude = np.sqrt(np.square(edge_x) + np.square(edge_y))
edge_magnitude = np.uint8(edge_magnitude)
# Display the results
plt.subplot(121), plt.imshow(image, cmap='gray'), plt.title('Original Image')
plt.subplot(122), plt.imshow(edge_magnitude, cmap='gray'), plt.title('Edge Image(Roberts Operator)')
plt.show()