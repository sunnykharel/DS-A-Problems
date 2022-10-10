

bool divisorGame(int N){
    return !(N&0x1);
    // return (N & 0x0001)^(0x0001)&0x0001;
}