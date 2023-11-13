uint32_t reverseBits(uint32_t n) {
    uint32_t temp = 0;
    int j = 0;
    for(int i = 31; i >= 0; i--){
        if((n & ((uint32_t)1) << i) != 0){
            temp |= (((uint32_t)1) << j);
        }
        j++;
    }
    return temp;
}