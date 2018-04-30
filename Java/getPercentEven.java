public static float getPercentEven(int[] a) {
    float percent = 0.0f;
    float even = 0.0f;
    float total = 0.0f;
    for (int i : a) {
        if (i % 2 == 0) {
            even++;
        }
        total++;
    }
    if (total == 0) 
        return 0.0f;
    percent = (even / total) * 100;
    return percent;
}



