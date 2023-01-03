from mtcnn.mtcnn import MTCNN
import cv2 
import gradio
def draw_image_with_boxes(image):
    detector = MTCNN()
    faces = detector.detect_faces(image)
    for result in faces:
       x, y, width, height = result['box']
      #  ROI = result[y:y+height, x:x+width]
       image = cv2.rectangle(image,(x,y), (x+width, y+height),(255,0,0),1)
    return image
img = gr.inputs.Image(shape=(192,192))
exp = ["./test1.jpeg","./test1.jpeg"]
interface = gr.Interface(fn=draw_image_with_boxes,inputs=img,outputs=img,examples=exp)
interface.launch(inline=False,debug=True)