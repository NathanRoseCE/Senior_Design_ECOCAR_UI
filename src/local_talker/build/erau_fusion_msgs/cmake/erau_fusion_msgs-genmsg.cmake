# generated from genmsg/cmake/pkg-genmsg.cmake.em

message(STATUS "erau_fusion_msgs: 7 messages, 0 services")

set(MSG_I_FLAGS "-Ierau_fusion_msgs:/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg;-Istd_msgs:/opt/ros/kinetic/share/std_msgs/cmake/../msg")

# Find all generators
find_package(gencpp REQUIRED)
find_package(geneus REQUIRED)
find_package(genlisp REQUIRED)
find_package(gennodejs REQUIRED)
find_package(genpy REQUIRED)

add_custom_target(erau_fusion_msgs_generate_messages ALL)

# verify that message/service dependencies have not changed since configure



get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" "erau_fusion_msgs/veh_object:std_msgs/Header:erau_fusion_msgs/tracked_veh_object"
)

get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" "erau_fusion_msgs/veh_object"
)

get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" "erau_fusion_msgs/veh_object:std_msgs/Header"
)

get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" ""
)

get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" ""
)

get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" "erau_fusion_msgs/Tracked_Lane:std_msgs/Header"
)

get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" NAME_WE)
add_custom_target(_erau_fusion_msgs_generate_messages_check_deps_${_filename}
  COMMAND ${CATKIN_ENV} ${PYTHON_EXECUTABLE} ${GENMSG_CHECK_DEPS_SCRIPT} "erau_fusion_msgs" "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" ""
)

#
#  langs = gencpp;geneus;genlisp;gennodejs;genpy
#

### Section generating for lang: gencpp
### Generating Messages
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_cpp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
)

### Generating Services

### Generating Module File
_generate_module_cpp(erau_fusion_msgs
  ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
  "${ALL_GEN_OUTPUT_FILES_cpp}"
)

add_custom_target(erau_fusion_msgs_generate_messages_cpp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_cpp}
)
add_dependencies(erau_fusion_msgs_generate_messages erau_fusion_msgs_generate_messages_cpp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_cpp _erau_fusion_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(erau_fusion_msgs_gencpp)
add_dependencies(erau_fusion_msgs_gencpp erau_fusion_msgs_generate_messages_cpp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS erau_fusion_msgs_generate_messages_cpp)

### Section generating for lang: geneus
### Generating Messages
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_eus(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
)

### Generating Services

### Generating Module File
_generate_module_eus(erau_fusion_msgs
  ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
  "${ALL_GEN_OUTPUT_FILES_eus}"
)

add_custom_target(erau_fusion_msgs_generate_messages_eus
  DEPENDS ${ALL_GEN_OUTPUT_FILES_eus}
)
add_dependencies(erau_fusion_msgs_generate_messages erau_fusion_msgs_generate_messages_eus)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_eus _erau_fusion_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(erau_fusion_msgs_geneus)
add_dependencies(erau_fusion_msgs_geneus erau_fusion_msgs_generate_messages_eus)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS erau_fusion_msgs_generate_messages_eus)

### Section generating for lang: genlisp
### Generating Messages
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_lisp(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
)

### Generating Services

### Generating Module File
_generate_module_lisp(erau_fusion_msgs
  ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
  "${ALL_GEN_OUTPUT_FILES_lisp}"
)

add_custom_target(erau_fusion_msgs_generate_messages_lisp
  DEPENDS ${ALL_GEN_OUTPUT_FILES_lisp}
)
add_dependencies(erau_fusion_msgs_generate_messages erau_fusion_msgs_generate_messages_lisp)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_lisp _erau_fusion_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(erau_fusion_msgs_genlisp)
add_dependencies(erau_fusion_msgs_genlisp erau_fusion_msgs_generate_messages_lisp)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS erau_fusion_msgs_generate_messages_lisp)

### Section generating for lang: gennodejs
### Generating Messages
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_nodejs(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
)

### Generating Services

### Generating Module File
_generate_module_nodejs(erau_fusion_msgs
  ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
  "${ALL_GEN_OUTPUT_FILES_nodejs}"
)

add_custom_target(erau_fusion_msgs_generate_messages_nodejs
  DEPENDS ${ALL_GEN_OUTPUT_FILES_nodejs}
)
add_dependencies(erau_fusion_msgs_generate_messages erau_fusion_msgs_generate_messages_nodejs)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_nodejs _erau_fusion_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(erau_fusion_msgs_gennodejs)
add_dependencies(erau_fusion_msgs_gennodejs erau_fusion_msgs_generate_messages_nodejs)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS erau_fusion_msgs_generate_messages_nodejs)

### Section generating for lang: genpy
### Generating Messages
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg"
  "${MSG_I_FLAGS}"
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg;/opt/ros/kinetic/share/std_msgs/cmake/../msg/Header.msg;/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg"
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)
_generate_msg_py(erau_fusion_msgs
  "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg"
  "${MSG_I_FLAGS}"
  ""
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
)

### Generating Services

### Generating Module File
_generate_module_py(erau_fusion_msgs
  ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
  "${ALL_GEN_OUTPUT_FILES_py}"
)

add_custom_target(erau_fusion_msgs_generate_messages_py
  DEPENDS ${ALL_GEN_OUTPUT_FILES_py}
)
add_dependencies(erau_fusion_msgs_generate_messages erau_fusion_msgs_generate_messages_py)

# add dependencies to all check dependencies targets
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/tracked_veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/unfused_vehicles.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/CanBus.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/veh_object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane_Object.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})
get_filename_component(_filename "/home/sabrinayepez/local_talker/src/erau_fusion_msgs/msg/Tracked_Lane.msg" NAME_WE)
add_dependencies(erau_fusion_msgs_generate_messages_py _erau_fusion_msgs_generate_messages_check_deps_${_filename})

# target for backward compatibility
add_custom_target(erau_fusion_msgs_genpy)
add_dependencies(erau_fusion_msgs_genpy erau_fusion_msgs_generate_messages_py)

# register target for catkin_package(EXPORTED_TARGETS)
list(APPEND ${PROJECT_NAME}_EXPORTED_TARGETS erau_fusion_msgs_generate_messages_py)



if(gencpp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gencpp_INSTALL_DIR}/erau_fusion_msgs
    DESTINATION ${gencpp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_cpp)
  add_dependencies(erau_fusion_msgs_generate_messages_cpp std_msgs_generate_messages_cpp)
endif()

if(geneus_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${geneus_INSTALL_DIR}/erau_fusion_msgs
    DESTINATION ${geneus_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_eus)
  add_dependencies(erau_fusion_msgs_generate_messages_eus std_msgs_generate_messages_eus)
endif()

if(genlisp_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genlisp_INSTALL_DIR}/erau_fusion_msgs
    DESTINATION ${genlisp_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_lisp)
  add_dependencies(erau_fusion_msgs_generate_messages_lisp std_msgs_generate_messages_lisp)
endif()

if(gennodejs_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs)
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${gennodejs_INSTALL_DIR}/erau_fusion_msgs
    DESTINATION ${gennodejs_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_nodejs)
  add_dependencies(erau_fusion_msgs_generate_messages_nodejs std_msgs_generate_messages_nodejs)
endif()

if(genpy_INSTALL_DIR AND EXISTS ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs)
  install(CODE "execute_process(COMMAND \"/usr/bin/python2\" -m compileall \"${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs\")")
  # install generated code
  install(
    DIRECTORY ${CATKIN_DEVEL_PREFIX}/${genpy_INSTALL_DIR}/erau_fusion_msgs
    DESTINATION ${genpy_INSTALL_DIR}
  )
endif()
if(TARGET std_msgs_generate_messages_py)
  add_dependencies(erau_fusion_msgs_generate_messages_py std_msgs_generate_messages_py)
endif()
