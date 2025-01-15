class Solution {
public:
    int minimizeXor(int num1, int num2) {
        int targetBits = __builtin_popcount(num2); 
        int currentBits = __builtin_popcount(num1); 
        
        int result = num1;
        if (currentBits == targetBits){
            return num1;
        }
        else if (currentBits > targetBits) {
            for (int i = 0; i < 32 && currentBits > targetBits; ++i) {
                if (result & (1 << i)) {
                    result ^= (1 << i); 
                    currentBits--;
                }
            }
        } 
        else if (currentBits < targetBits) {
            for (int i = 0; i < 32 && currentBits < targetBits; ++i) {
                if (!(result & (1 << i))) { 
                    result |= (1 << i);   
                    currentBits++;
                }
            }
        }
        
        return result;
    }
};
