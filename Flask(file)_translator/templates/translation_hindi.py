import googletrans
from googletrans import Translator


translator = Translator()


        # Adding all the translations to a dictionary (translations)
translations = translator.translate("ಹಣ").text
print(translations)
