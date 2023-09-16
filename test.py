# from PIL import Image
# import numpy as np

# # Example color correction matrix (adjusts R, G, B channels)
# color_correction_matrix = np.array([
#     [1.2, 0.0, 0.0],
#     [0.0, 1.1, 0.0],
#     [0.0, 0.0, 0.9]
# ])

# def calibrate_image(image_path, calibration_matrix):
#     # Open the image using Pillow
#     img = Image.open(image_path)
    
#     # Convert the image to a NumPy array for matrix operations
#     img_array = np.array(img)
    
#     # Apply the color correction matrix to the image array
#     calibrated_img_array = np.dot(img_array, calibration_matrix.T).astype(np.uint8)
    
#     # Create a new Pillow image from the calibrated array
#     calibrated_img = Image.fromarray(calibrated_img_array)
    
#     return calibrated_img

# # Path to the input image
# input_image_path = "data/1.jpg"

# # Calibrate the image
# calibrated_image = calibrate_image(input_image_path, color_correction_matrix)

# # Save the calibrated image
# calibrated_image.save("calibrated_image.jpg")

# print("Image calibration complete.")

import numpy as np

# Known reflectance values from the target (example)
reference_reflectance = np.array([0.5, 0.8, 0.6])

# Measured color values under reference lighting conditions (example)
reference_color_values = np.array([120, 180, 150])

# Calculate calibration ratios
calibration_ratios = reference_reflectance / reference_color_values

# Simulated raw color values under different lighting conditions
raw_color_values = np.array([110, 160, 140])

# Apply calibration to adjust for lighting conditions
calibrated_color_values = raw_color_values * calibration_ratios

print(f"Raw Color Values: {raw_color_values}")
print(f"Calibrated Color Values: {calibrated_color_values}")
