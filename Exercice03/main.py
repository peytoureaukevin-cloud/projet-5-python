words = ["python", "programmation", "langage", "ordinateur", "apprentissage"]

vowels = "aeiouy"

result = [
    (word, sum(1 for letter in word if letter in vowels))
    for word in words
]

print(result)