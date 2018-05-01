public double mean(ArrayList<Double> data) {
    if (data.size() == 0) return 0.0;
    double sum = 0;
    int count = 0;
    for (double num : data) {
        sum += num;
        count++;
    }
	return sum / count;
}
