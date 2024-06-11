cmake_minimum_required(VERSION 3.15)
project(${CMAKE_PROJECT_NAME}_Unit_Test CXX)

include(CTest)

set(UT_SOURCES
    "test.cpp"
)

add_executable(${PROJECT_NAME} ${UT_SOURCES})

find_package(GTest REQUIRED)
target_link_libraries(${PROJECT_NAME} PRIVATE ${CMAKE_PROJECT_NAME}
    GTest::gtest)

add_test(
    NAME ${PROJECT_NAME}
    COMMAND ${PROJECT_NAME}
    WORKING_DIRECTORY ${CMAKE_CURRENT_LIST_DIR})