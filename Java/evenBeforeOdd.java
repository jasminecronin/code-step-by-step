public static void evenBeforeOdd(int[] a) {
    int temp = 0;
    for (int i = 0; i < a.length; i++) {
        if (a[i] % 2 != 0) {
            for (int j = a.length-1; j > i; j--) { //locate an even number from the back
                if (a[j] % 2 == 0) {
                    temp = a[i];
                    a[i] = a[j];
                    a[j] = temp;
                    break;
                }
            }
        }
    }
}