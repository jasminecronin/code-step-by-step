public ArrayList<Integer> intersect(ArrayList<Integer> v1, ArrayList<Integer> v2) {
    ArrayList<Integer> a = new ArrayList<Integer>();
    int step1 = 0;
    int step2 = 0;
    while (step1 < v1.size() && step2 < v2.size()) {
        if (v1.get(step1) == v2.get(step2)) {
            a.add(v1.get(step1));
            step1++;
            step2++;
        } else if (v1.get(step1) < v2.get(step2)) {
            step1++;
        } else {
            step2++;
        }
    }
    return a;
}
