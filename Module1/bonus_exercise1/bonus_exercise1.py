text = """– Czemu tak ciągle gadasz o kobietach, Stan?
– Bo chcę zostać kobietą. Chcę być kobietą. Chce żebyście od dziś mówili na mnie „Loretta”. To moje niezbywalne prawo jako mężczyzny.
– Ale dlaczego chcesz zostać Lorettą, Stan?
– Bo chcę mieć dzieci.
– Dzieci?
– Każdy mężczyzna ma prawo mieć dzieci, jeśli chce.
– Przecież ty nie możesz mieć dzieci!
– Nie prześladuj mnie!
– Nie prześladuję cię, Stan! Nie masz macicy! Gdzie będziesz trzymał swojego embriona? W pudełku?
– Mam pomysł! Przyjmijmy, że Stan nie może póki co mieć dzieci, gdyż nie ma macicy, co nie jest niczyją winą, nawet Rzymian, ale musimy przyznać, że ma prawo do dzieci!
– Świetnie, Judith! Będziemy walczyć z ciemiężycielami…
– Przepraszam.
– A po co?
– Co po co?
– Po co walczyć o jego prawo do posiadania dzieci…
– To symbol naszej beznadziejnej walki z najeźdźcą.
– Symbol jego beznadziejnej walki z rzeczywistością."""


def number_of_letters(letter, text):
    number_of_letters = 0
    for i in text.lower():
        if i == letter:
            number_of_letters = number_of_letters + 1
    return number_of_letters


number_of_a = number_of_letters("a", text)
print(f"Litera a: {number_of_a}")
number_of_e = number_of_letters("e", text)
print(f"Litera e: {number_of_e}")
number_of_i = number_of_letters("i", text)
print(f"Litera i: {number_of_i}")
number_of_o = number_of_letters("o", text)
print(f"Litera o: {number_of_o}")
number_of_u = number_of_letters("u", text)
print(f"Litera u: {number_of_u}")
number_of_y = number_of_letters("y", text)
print(f"Litera y: {number_of_y}")
