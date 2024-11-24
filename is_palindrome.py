def is_palindrome(s):
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s

# Exemplo de uso
phrase = "A man a plan a canal Panama"
print(is_palindrome(phrase))
