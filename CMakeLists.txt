cmake_minimum_required(VERSION 3.15)
project(LeetcodeExercises)

# include(${CMAKE_BINARY_DIR}/conan_toolchain.cmake)
# include_directories(${CMAKE_SOURCE_DIR}/include)

find_package(GTest REQUIRED)

#add_executable(leetcode_exercises 
#    "src/main.cpp")

# target_link_libraries(leetcode_exercises gtest::gtest)

add_library(leetcode_exercises_lib 
    "src/sum.cpp"
    "include/sum.hpp" )

# Configure the library
target_include_directories(leetcode_exercises_lib PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

add_executable(tests tests/test.cpp)

target_link_libraries(tests
    leetcode_exercises_lib
    gtest::gtest)
    
# target_link_libraries(tests gtest::gtest)