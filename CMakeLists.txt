cmake_minimum_required(VERSION 3.15)
project(LeetcodeExercises)

# include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)
include_directories(${CMAKE_SOURCE_DIR}/include)

# find_package(GTest REQUIRED)

add_executable(leetcode_exercises src/main.cpp)
# target_link_libraries(leetcode_exercises gtest::gtest)

# add_executable(tests tests/test.cpp)
# target_link_libraries(tests gtest::gtest)