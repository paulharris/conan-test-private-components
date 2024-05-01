cmake_minimum_required(VERSION 3.15)
project(thelib CXX)

##############

add_library(private_function src/private_function.cpp)
target_include_directories(private_function PUBLIC "include/private_component")

set_target_properties(private_function PROPERTIES PUBLIC_HEADER "include/private_component/private_function.h")
set_target_properties(private_function PROPERTIES PUBLIC_HEADER "include/private_component/private_function_failure.h")

install(TARGETS private_function
      PUBLIC_HEADER
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/private_component"
      INCLUDES
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/private_component"
      )

##############

add_library(public_function src/public_function.cpp)
target_include_directories(public_function PUBLIC "include/public_component")

set_target_properties(public_function PROPERTIES PUBLIC_HEADER "include/public_component/public_function.h")

install(TARGETS public_function
      PUBLIC_HEADER
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/public_component"
      INCLUDES
         DESTINATION "${CMAKE_INSTALL_INCLUDEDIR}/public_component"
      )

target_link_libraries(public_function
   PRIVATE
      private_function
     )
