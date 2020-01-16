import tkinter as tk
import requests
from PIL import ImageTk, Image

HEIGHT = 729
WIDTH = 410


class PokeGUI:

    def __init__(self):
        self.root = tk.Tk()

        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        # background image
        self.img = Image.open("pokedex.jpg")
        self.resized = self.img.resize((410, 729), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resized)
        self.canvas.create_image((0, 0), anchor=tk.NW, image=self.img)

        # container for upperframe label
        self.upper_frame = tk.Frame(self.root)
        self.upper_frame.place(relx=0.45, rely=0.28, relwidth=0.53, relheight=0.21, anchor='n')

        # where the results will appear
        self.label = tk.Label(self.upper_frame, font=('Courier New', 14), anchor=tk.NW, justify='left', img="25.jpg")
        self.label.place(relwidth=1, relheight=1)

        # container for text entry field
        self.mid_frame = tk.Frame(self.root)
        self.mid_frame.place(relx=0.37, rely=0.685, relwidth=0.29, relheight=0.095, anchor='n')

        self.entry = tk.Entry(self.mid_frame, font=('Courier New', 15))
        self.entry.place(relwidth=1, relheight=1)

        # container for search button
        self.lower_frame = tk.Frame(self.root)
        self.lower_frame.place(relx=0.37, rely=0.80, relwidth=0.3, relheight=0.04, anchor='n')

        self.button = tk.Button(self.lower_frame, text="Search", font=('Courier New', 15), command=lambda: APIHandler.get_data(self, self.entry.get()))
        self.button.place(relheight=1, relwidth=1)

        # open window
        self.root.mainloop()


class APIHandler:
    """
    Represents the handler that communicates with the PokeAPI via
    HTTP GET requests to get data.
    """
    url = "https://pokeapi.co/api/v2/pokemon/{}"

    @classmethod
    def get_data(cls, gui: PokeGUI, id_: int):
        """
        Sends a GET request to the PokeAPI based on user provided input.
        If the request fails, then the response returned is a
        error message string that will be output later on.
        :param id_: an int
        :return: a str or a dict
        """
        target_url = APIHandler.url.format(id_)
        response = requests.get(target_url)

        if response.status_code != 200:
            output = f"Pokemon with name/id {id_} could not be found."
            # return f"{mode.title()} with name/id {id_} " \
            #        f"could not be found."
        else:
            # debugging:
            # print("Response object from aiohttp:\n", response)
            # print("Response object type:\n", type(response))
            pokemon = response.json()
            output = cls.format_response(pokemon)

        gui.label['text'] = output

            # return json_dict

    @classmethod
    def format_response(cls, pokemon):
        try:
            name = pokemon['name'].title()
            height = pokemon['height']
            weight = pokemon['weight']

            abilities = ""
            for index in range(len(pokemon['abilities'])):
                abilities += f"\n    {index + 1}) "
                abilities += "{}".format(
                    pokemon['abilities'][index]['ability']['name'].title())

            img = pokemon['sprites']['front_default']

            final_str = "Name: %s\nHeight: %s\nWeight: %s\nAbilities: %s\nImg: %s" % (name, height, weight, abilities, img)
        except:
            final_str = 'The requested pokemon could not be found.'

        return final_str


def main():
    """Main driver for the Pokedex after the user provides input
    from the terminal via the CommandlineInterface."""
    PokeGUI()


if __name__ == "__main__":
    main()
