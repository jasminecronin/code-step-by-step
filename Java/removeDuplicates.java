public String removeDuplicates(String str) {
	String result = "";
    for (int i = 0; i < str.length(); i++) {
        if (i == 0 || str.charAt(i-1) != str.charAt(i)) {
            result += str.charAt(i);
        }
    }
    return result;
}
