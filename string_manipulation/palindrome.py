def is_palindrome(text):
    evaluated_text = ''.join(_.lower() for _ in text if _.isalnum())
    return evaluated_text == evaluated_text[::-1]
