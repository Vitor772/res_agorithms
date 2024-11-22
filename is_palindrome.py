def is_palindrome(s):
    # Remove espaços e transforma tudo em minúsculas
    s = ''.join(c.lower() for c in s if c.isalnum())
    return s == s[::-1]

# Exemplo de uso
phrase = "A man a plan a canal Panama"
print(is_palindrome(phrase))  # True
