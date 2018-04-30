public boolean sameDashes(String str1, String str2) {
	int i1 = str1.indexOf('-');
	int i2 = str2.indexOf('-');

	while (i1 != -1 || i2 != -1) {
		if (i1 != i2) {
			return false;
		}
		str1 = str1.substring(i1 + 1, str1.length());
		str2 = str2.substring(i2 + 1, str2.length());
		i1 = str1.indexOf('-');
		i2 = str2.indexOf('-');
	}
	return true;
}
	



