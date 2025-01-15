class Solution {
public:
    string winningPlayer(int x, int y) {
        if (float(x)>float(y*0.25)){
            if(y%8>=4){
                return "Alice" ;
            }
            return "Bob";
        }
        else{
            if(x%2==1){
                return "Alice";
            }
            return "Bob";
        }
    }
};
