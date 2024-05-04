cmake_minimum_required(VERSION 3.15)
project(PackageTest CXX)

find_package(test_separate_component_lib CONFIG REQUIRED COMPONENTS compa_function)

add_executable(example src/example.cpp)
target_link_libraries(example test_separate_component_lib::compa_function)
