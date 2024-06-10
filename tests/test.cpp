#include "gtest/gtest.h"
#include "main.cpp"

TEST(SumTest, PositiveNos)
{
    EXPECT_EQ(6, sum(2, 4));
}

int main(int argc, char **argv)
{
    testing::InitGoogleTest(&argc, argv);
    return RUN_ALL_TESTS();
}