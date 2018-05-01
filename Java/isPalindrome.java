public boolean isPalindrome(String s) {
    if (s.length() > 1) {
        if (Character.toUpperCase(s.charAt(0)) == Character.toUpperCase(s.charAt(s.length()-1))) {
            return isPalindrome(s.substring(1, s.length()-1));
        } else {
            return false;
        }
    } else {
        return true;
    }
}
