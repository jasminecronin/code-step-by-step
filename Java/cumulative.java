public void cumulative(ArrayList<Integer> v) {
	int sum = 0;
    for (int i = 0; i < v.size(); i++) {
        sum += v.get(i);
        v.set(i, sum);
    }
}
