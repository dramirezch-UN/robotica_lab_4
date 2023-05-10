cmake_minimum_required(VERSION 2.8.3)
project(lab_4)

find_package(catkin REQUIRED COMPONENTS
  rospy
)

catkin_package()

catkin_install_python(PROGRAMS
  scripts/move_servo.py
  scripts/go_home.py
  scripts/read_angs.py
  scripts/move_all.py
  scripts/gui/gui.py
  DESTINATION ${CATKIN_PACKAGE_BIN_DESTINATION}
)
