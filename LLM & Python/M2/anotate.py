import cv2

def annotate_image(image_path, output_path):
    # 1. Read the image
    # Note: OpenCV uses BGR (Blue, Green, Red) format by default
    img = cv2.imread(image_path)
    
    if img is None:
        print("Error: Could not read image.")
        return

    # Create a copy to keep the original image intact
    annotated_img = img.copy()

    # 2. Draw a Rectangle (e.g., for a Bounding Box)
    # Parameters: image, start_point(x,y), end_point(x,y), color(BGR), thickness
    # Use thickness=-1 to create a filled rectangle
    cv2.rectangle(annotated_img, (50, 50), (250, 250), (0, 255, 0), thickness=3)

    # 3. Draw a Line
    # Parameters: image, /start_point(x,y), end_point(x,y), color(BGR), thickness
    cv2.line(annotated_img, (300, 50), (500, 50), (255, 0, 0), thickness=5)

    # 4. Draw a Circle
    # Parameters: image, center_point(x,y), radius, color(BGR), thickness
    cv2.circle(annotated_img, (400, 200), 50, (0, 0, 255), thickness=2)

    # 5. Add Text (Labeling)
    # Parameters: image, text, org(x,y), font, scale, color, thickness, lineType
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(annotated_img, 'OpenCV Annotation', (50, 300), font, 
                1, (255, 255, 255), 2, cv2.LINE_AA)

    # 6. Display the image
    cv2.imshow('Annotated Image', annotated_img)
    
    # 7. Save the annotated image
    cv2.imwrite(output_path, annotated_img)
    print(f"Annotated image saved to {output_path}")

    # Wait for a key press and close windows
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Usage
# Replace 'input.jpg' with your image file path
annotate_image('input.jpg', 'annotated_result.jpg')
