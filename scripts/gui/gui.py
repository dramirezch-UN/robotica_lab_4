import sys
import tkinter as tk
from PIL import ImageTk, Image
import os
import rospy
from std_msgs.msg import String
from sensor_msgs.msg import JointState
from trajectory_msgs.msg import JointTrajectory, JointTrajectoryPoint
import math
import time

positions_matrix = [[math.radians(0), math.radians(0), math.radians(0), math.radians(0), math.radians(0)],
                    [math.radians(-25), math.radians(15), math.radians(-20), math.radians(20), math.radians(0)],
                    [math.radians(35), math.radians(-35), math.radians(30), math.radians(-30), math.radians(0)],
                    [math.radians(-85), math.radians(20), math.radians(-55), math.radians(17), math.radians(0)],
                    [math.radians(-80), math.radians(35), math.radians(-55), math.radians(45), math.radians(0)]]

def joint_publisher(index):
    pub = rospy.Publisher('/joint_trajectory', JointTrajectory, queue_size=0)
    rospy.init_node('joint_publisher', anonymous=False)
    
    while not rospy.is_shutdown():
        state = JointTrajectory()
        state.header.stamp = rospy.Time.now()
        state.joint_names = ["joint_1", "joint_2", "joint_3", "joint_4", "joint_5"]
        point = JointTrajectoryPoint()
        point.positions = positions_matrix[index]
        point.time_from_start = rospy.Duration(0.5)
        state.points.append(point)
        pub.publish(state)
        print('published command')
        rospy.sleep(1)

dirname = os.path.dirname(__file__)

# create the root window
root = tk.Tk()

# set the window title and size
root.title("Laboratorio 4")
root.geometry("1980x1080")

# create the subtitle label
subtitle_label1 = tk.Label(root, text="Laboratorio 4", font=("Arial", 20))
subtitle_label1.pack(pady=10)
subtitle_label2 = tk.Label(root, text="Juan Camilo Olaya (jolayam), Luis David Preciado (lpreciadom), Daniel Esteban Ramírez (dramirezch)", font=("Arial", 12))
subtitle_label2.pack(pady=10)
subtitle_label3 = tk.Label(root, text="Poses:", font=("Arial", 12))
subtitle_label3.place(x=17, y=100, anchor=tk.W)

# create a frame for the buttons
button_frame = tk.Frame(root)
button_frame.pack()

# create the button functions
def button1_clicked():
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Button 1 clicked\n")
    img = Image.open(os.path.join(dirname, 'img/1.jpg'))
    img = img.resize((300, 400), Image.LANCZOS)
    photoImg = ImageTk.PhotoImage(img)
    image_label.configure(image=photoImg)
    image_label.image = photoImg
    try:
        joint_publisher(1)
    except rospy.ROSInterruptException:
        pass

def button2_clicked():
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Button 2 clicked\n")
    img = Image.open(os.path.join(dirname, 'img/2.jpg'))
    img = img.resize((300, 400), Image.LANCZOS)
    photoImg = ImageTk.PhotoImage(img)
    image_label.configure(image=photoImg)
    image_label.image = photoImg
    try:
        joint_publisher(2)
    except rospy.ROSInterruptException:
        pass

def button3_clicked():
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Button 3 clicked\n")
    img = Image.open(os.path.join(dirname, 'img/3.jpg'))
    img = img.resize((300, 400), Image.LANCZOS)
    photoImg = ImageTk.PhotoImage(img)
    image_label.configure(image=photoImg)
    image_label.image = photoImg
    try:
        joint_publisher(3)
    except rospy.ROSInterruptException:
        pass

def button4_clicked():
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Button 4 clicked\n")
    img = Image.open(os.path.join(dirname, 'img/4.jpg'))
    img = img.resize((300, 400), Image.LANCZOS)
    photoImg = ImageTk.PhotoImage(img)
    image_label.configure(image=photoImg)
    image_label.image = photoImg
    try:
        joint_publisher(4)
    except rospy.ROSInterruptException:
        pass

def button5_clicked():
    output_text.delete('1.0', tk.END)
    output_text.insert(tk.END, "Button 5 clicked\n")
    img = Image.open(os.path.join(dirname, 'img/5.jpg'))
    img = img.resize((300, 400), Image.LANCZOS)
    photoImg = ImageTk.PhotoImage(img)
    image_label.configure(image=photoImg)
    image_label.image = photoImg
    try:
        joint_publisher(5)
    except rospy.ROSInterruptException:
        pass

# create the buttons
button1 = tk.Button(button_frame, text="0,0,0,0,0", command=button1_clicked)
button2 = tk.Button(button_frame, text="-25,15,-20,20,0", command=button2_clicked)
button3 = tk.Button(button_frame, text="35,-35,30,-30,0", command=button3_clicked)
button4 = tk.Button(button_frame, text="-85,20,-55,17,0", command=button4_clicked)
button5 = tk.Button(button_frame, text="-80,35,-55,45,0", command=button5_clicked)

# pack the buttons into the frame
button1.pack(pady=10)
button2.pack(pady=10)
button3.pack(pady=10)
button4.pack(pady=10)
button5.pack(pady=10)

# create a Text widget for displaying the output
subtitle_label4= tk.Label(root, text="Valores articulares:", font=("Arial", 12))
subtitle_label4.pack(pady=10)
output_text = tk.Text(root, width=100, height=6)
output_text.pack(pady=10)

# create the image label and pack it into the window
img = Image.open(os.path.join(dirname, 'img/unal.png'))
img = img.resize((200, 200), Image.LANCZOS)
photoImg = ImageTk.PhotoImage(img)
image_label = tk.Label(root, image=photoImg)
image_label.pack(pady=10)

# start the main loop
root.mainloop()