// я здесь пробую чисто арифметическое решение, без превращения в строку
bool isPalindrome(int x) {
    if (x < 0) return false;
    long reverse_x = 0; 
    int temp_x = x;
    int i = 1;
    while (temp_x != 0) {
        reverse_x = reverse_x * 10 + temp_x % 10;
        temp_x = temp_x / 10;
    }
    return x == reverse_x;
}