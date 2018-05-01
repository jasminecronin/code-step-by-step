public void numberSequence(int n) {
    if (n < 1) throw new IllegalArgumentException();
    if (n == 2) System.out.print("1 1 ");
    else if (n == 1) System.out.print("1 ");
    
    else{
        System.out.print((n + 1) / 2 + " ");
        numberSequence(n - 2);
        System.out.print((n + 1) / 2 + " ");
    }
}
