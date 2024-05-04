cmake_minimum_required(VERSION 3.15)
project(thelib CXX)

##############

add_library(compb_function src/compb_function.cpp)
target_include_directories(compb_function PUBLIC "include/compb")

set_target_properties(compb_function PROPERTIES PUBLIC_HEADER "include/compb/compb_function.h")
set_target_properties(compb_function PROPERTIES PUBLIC_HEADER "include/compb/compb_function_failure.h")

install(TARGETS compb_function
      PUBLIC_HEADER
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/compb"
      INCLUDES
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/compb"
      )

##############

add_library(compa_function src/compa_function.cpp)
target_include_directories(compa_function PUBLIC "include/compa")

set_target_properties(compa_function PROPERTIES PUBLIC_HEADER "include/compa/compa_function.h")

install(TARGETS compa_function
      PUBLIC_HEADER
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/compa"
      INCLUDES
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/compa"
      )

target_link_libraries(compa_function
   compb
      compb_function
     )
