public void collapsePairs(int[] a) {
    for (int i = 0; i < a.length-1; i += 2) {
        int sum = a[i] + a[i+1];
        if (sum % 2 == 0) {
            a[i] = sum;
            a[i+1] = 0;
        } else {
            a[i+1] = sum;
            a[i] = 0;            
        }
    }
}
