public void banish(int[] arr1, int[] arr2) {
	for (int i = 0; i < arr1.length; i++) {
		boolean found = false;

		for (int j = 0; j < arr2.length; j++) {
			if (arr1[i] == arr2[j]) {
				found = true;
			}
		}
		if (found) {
			for (int j = i + 1; j < arr1.length; j++) {
				arr1[j - 1] = arr1[j];
			}
			arr1[arr1.length - 1] = 0;
			i--;
		}
	}
}