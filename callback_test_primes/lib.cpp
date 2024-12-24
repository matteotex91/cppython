#include <iostream>
#include <vector>
#include <functional>
#include <cmath>

// compile command :
// g++ -shared -fPIC -std=c++11 -o lib.so lib.cpp
extern "C"
{
    typedef void (*callback_t)(int);

    void prime_numbers_callback(int limite, callback_t callback)
    {
        for (int i = 2; i <= limite; ++i)
            [&]
            {
                for (int j = 2; j < i / 2; ++j)
                {
                    if (i % j == 0)
                    {
                        return;
                    }
                }
                callback(i);
            }();
    }
}