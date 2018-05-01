public String toString() {
    String str = name;
    double bal = balance;
    str += ", ";
    if (balance < 0) {
        str += "-";
        bal = -balance;
    }
    str += "$";
    str += String.format("%.2f", bal);
    return str;
}
