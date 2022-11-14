import cv2

# Set image path
image_path =r'opencv.png'

# Read Image
image = cv2.imread(image_path)

# Show image
cv2.imshow('Sample image',image)

# wait for key then press key and destroy the windows, its a way to display and not exit the window
cv2.waitKey(0)
cv2.destroyAllWindows()

# get the directory to save the image
directory = r'/mnt/importante/proyectos/opencv/'

# given a name to test image, then writing to that image
filename = 'savedImageTest.png'
cv2.imwrite(filename, image)
print('Succesfully saved')
