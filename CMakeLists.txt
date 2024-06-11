cmake_minimum_required(VERSION 3.15)
project(Leetcode_Exercises LANGUAGE CXX)

set(CPP_FILES
    "src/sum.cpp"
)

set(HPP_FILES
    "include/sum.hpp"
)

add_library(${PROJECT_NAME} ${CPP_FILES} ${HPP_FILES})

# Configure the library
target_include_directories(${PROJECT_NAME} PUBLIC
    $<INSTALL_INTERFACE:include>
    $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
)

# if (BUILD_TESTING)
    enable_testing()
    add_subdirectory(tests)
# endif ()