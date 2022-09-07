cmake_minimum_required(VERSION 3.5)
project(lab1_pkg)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(ament_cmake_python REQUIRED)
find_package(rclcpp REQUIRED)
find_package(rclpy REQUIRED)
find_package(ackermann_msgs REQUIRED)


# Create Cpp executable
# add_executable(relay src/relay.cpp)
#ament_target_dependencies(relay rclcpp ackermann_msgs)
#add_executable(talker src/talker.cpp)
#ament_target_dependencies(talker rclcpp ackermann_msgs)

# install the launch directory
install(DIRECTORY
  launch
  DESTINATION share/${PROJECT_NAME}/
)
# Install Cpp executables
#install(TARGETS
 # relay
  #talker
  #DESTINATION lib/${PROJECT_NAME}
#)

# Install Python modules
ament_python_install_package(${PROJECT_NAME})

# Install Python executables
install(PROGRAMS
   scripts/talker.py
   scripts/relay.py
   DESTINATION lib/${PROJECT_NAME}
)

ament_package()