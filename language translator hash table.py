class Translator:
    def __init__(self):
        self.translation_table = {}

    def add_translation(self, word, translation):
        self.translation_table[word] = translation

    def translate(self, text):
        words = text.split()
        translated_words = []
        for word in words:
            translated_word = self.translation_table.get(word, word)
            translated_words.append(translated_word)
        return " ".join(translated_words)

# Create an instance of the Translator
translator = Translator()

# Add translations
translator.add_translation("hello", "bonjour")
translator.add_translation("madam", "mundo")
translator.add_translation("what", "quoi")
translator.add_translation("is", "est")
translator.add_translation("your", "ton")
translator.add_translation("full", "complet")
translator.add_translation("name", "nom")

# Translate a sentence
text_to_translate = "hello madam, what is your full name?"
translated_text = translator.translate(text_to_translate)

print(translated_text)