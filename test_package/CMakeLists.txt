cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(test_private_component_lib CONFIG REQUIRED COMPONENTS public_function)

add_executable(example src/example.cpp)
target_link_libraries(example test_private_component_lib::public_function)
