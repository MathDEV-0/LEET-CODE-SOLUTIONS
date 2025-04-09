#include <iostream>

class Solution {
    public:
        bool isPalindrome(int x) {
            int carry,inverted = 0 ;
            int inOrder = x;
            
            while(inOrder > 0){
                carry = inOrder % 10;
                inverted = inverted * 10 + carry;
                inOrder = inOrder / 10;
            }
    
            return x == inverted;
        }
    };


int main(){
    Solution solutionA;
    
    std::cout << solutionA.isPalindrome(121) << std::endl;  // Saída: 1 (true)
    std::cout << solutionA.isPalindrome(-121) << std::endl;  // Saída: 0 (false)
    std::cout << solutionA.isPalindrome(10) << std::endl; // Saída: 0 (false)
}
