import tkinter
from tkinter.constants import LEFT, RIGHT
import cv2
import PIL.Image, PIL.ImageTk
import time


class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.window.attributes('-fullscreen', True)
        self.window.configure(bg='black')
        # open video source (by default this will try to open the computer webcam)
        self.cams = [MyVideoCapture(0), MyVideoCapture(4), MyVideoCapture(8)]
        # self.configureCams()
        # Create a canvas that can fit the above video source size
        
        self.frame = tkinter.Frame(self.window, width=self.window.winfo_screenwidth(), height=self.window.winfo_screenheight())
        self.frame.grid(row=0, column=0)
        self.frame.pack(fill=tkinter.BOTH, expand=True)

        self.display1 = tkinter.Label(self.frame)

        self.display1.grid(row=0, column=1)  #Display 1
        self.display2 = tkinter.Label(self.frame)

        self.display2.grid(row=0, column=0) #Display 2
        self.display3 = tkinter.Label(self.frame)

        self.display3.grid(row=0, column=3) #Display 2
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 10

        self.update()

        self.window.mainloop()

    def configureCams(self):
        for cam in self.cams:
            cam.vid.set(3, self.window.winfo_screenwidth()/3)
            cam.vid.set(4, self.window.winfo_screenheight()/3)
    
    def descale(self, frame):
        return cv2.resize(frame, (int(self.window.winfo_screenwidth()/3), int(self.window.winfo_screenheight())))



    def update(self):
        # Get a frame from the video source
        for vid in self.cams:
            ret, frame = vid.get_frame()

            if ret:
                if vid.source == 4:
                    image = (PIL.Image.fromarray(self.descale(frame)))
                    self.photo = PIL.ImageTk.PhotoImage(image)
                    self.display1.imgtk = self.photo
                    self.display1.configure(image=self.photo)
                elif vid.source == 8:
                    image = (PIL.Image.fromarray(self.descale(frame)))
                    self.photo = PIL.ImageTk.PhotoImage(image)
                    self.display3.imgtk = self.photo
                    self.display3.configure(image=self.photo)
                else:
                    image = (PIL.Image.fromarray(self.descale(frame)))
                    self.photo = PIL.ImageTk.PhotoImage(image)
                    self.display2.imgtk = self.photo
                    self.display2.configure(image=self.photo)

        self.window.after(self.delay, self.update)


class MyVideoCapture:
    def __init__(self, video_source):
        # Open the video source
        self.source = video_source
        self.vid = cv2.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (ret, None)
        else:
            return (ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release() 
# Create a window and pass it to the Application object
App(tkinter.Tk(), "Tkinter and OpenCV")