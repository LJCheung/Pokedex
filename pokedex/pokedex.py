"""
This module contains the implementation of the PokeGUI and Pokedex
Classes.
"""
import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO

HEIGHT = 729
WIDTH = 410


class PokeGUI:
    """This class represents the GUI for the Pokedex."""

    def __init__(self):
        """
        Initializes and generates the application window.
        """
        self.root = tk.Tk()
        self.root.title('Pokedex')

        self.canvas = tk.Canvas(self.root, height=HEIGHT, width=WIDTH)
        self.canvas.pack()

        # background image
        self.img = Image.open("pokedex.jpg")
        self.resized = self.img.resize((410, 729), Image.ANTIALIAS)
        self.img = ImageTk.PhotoImage(self.resized)
        self.canvas.create_image((0, 0), anchor=tk.NW, image=self.img)

        # container for pokemon image frame
        self.pokeimg_frame = tk.Frame(self.root)
        self.pokeimg_frame.place(relx=0.285, rely=0.28, relwidth=0.19,
                                 relheight=0.11, anchor='n')

        # label for pokemon image frame
        self.pokeimg_label = tk.Label(self.pokeimg_frame, anchor='w',
                                      bg="#013df5")
        # must keep a reference per
        # https://effbot.org/tkinterbook/photoimage.htm
        self.pokeimg_label.image = ""
        self.pokeimg_label.place(relwidth=1, relheight=1)

        # container for info frame
        self.info_frame = tk.Frame(self.root)
        self.info_frame.place(relx=0.55, rely=0.30, relwidth=0.32,
                              relheight=0.1, anchor='n')

        # label for info frame
        self.info_label = tk.Label(self.info_frame, bg="#013df5",
                                   font=('Courier New', 14, 'bold'),
                                   anchor=tk.NW, justify='left')
        self.info_label.place(relwidth=1, relheight=1)

        # container for abilities frame
        self.abilities_frame = tk.Frame(self.root)
        self.abilities_frame.place(relx=0.46, rely=0.39, relwidth=0.515,
                                   relheight=0.10, anchor='n')

        # label for abilities frame
        self.abilities_label = tk.Label(self.abilities_frame,
                                        bg="#013df5",
                                        font=('Courier New', 14,
                                              'bold'), anchor=tk.NW,
                                        justify='left', wraplength=220)
        self.abilities_label.place(relwidth=1, relheight=1)

        # container for text entry field
        self.mid_frame = tk.Frame(self.root, bg="#5ab16a")
        self.mid_frame.place(relx=0.37, rely=0.685, relwidth=0.29,
                             relheight=0.095, anchor='n')

        self.entry = tk.Entry(self.mid_frame, font=('Courier New', 15),
                              bg="#5ab16a", highlightthickness=0,
                              justify="center")
        self.entry.place(relwidth=1, relheight=1)

        # container for search button
        self.lower_frame = tk.Frame(self.root)
        self.lower_frame.place(relx=0.37, rely=0.80, relwidth=0.3,
                               relheight=0.04, anchor='n')

        self.button = tk.Button(self.lower_frame, text="Search",
                                font=('Courier New', 15, "bold"),
                                command=lambda: APIHandler.get_data(
                                    self, self.entry.get()))
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
    def get_sprite(cls, img_url: str) -> ImageTk.PhotoImage:
        """
        Sends a GET request to access the pokemon sprite image.
        :param img_url: a string
        :return: a ImageTk.PhotoImage
        """
        img_response = requests.get(img_url)
        img_data = img_response.content
        poke_img = Image.open(BytesIO(img_data))
        resized_img = poke_img.resize((80, 80), Image.ANTIALIAS)

        return ImageTk.PhotoImage(resized_img)

    @classmethod
    def get_data(cls, gui: PokeGUI, id_):
        """
        Sends a GET request to the PokeAPI based on user provided input.
        If the request fails, then the response returned is a
        error message string that will be output later on.
        :param gui: a PokeGUI
        :param id_: an int
        :return: a str or a dict
        """

        if id_ != "":
            target_url = APIHandler.url.format(id_.lower())
            response = requests.get(target_url)

            if response.status_code != 200:
                output = \
                    f"Pokemon with name/id '{id_}' could not be found."
                gui.abilities_label['text'] = output
                gui.info_label['text'] = ""
                gui.pokeimg_label['image'] = ""
            else:
                pokemon = response.json()

                # format name, height and weight
                info = "Name: %s\nHeight: %s m\nWeight: %s kg" \
                       % (pokemon['name'].title(), pokemon['height']/10,
                          int(pokemon['weight']/10))
                gui.info_label['text'] = info

                # get sprite
                img_url = pokemon['sprites']['front_default']
                poke_img = cls.get_sprite(img_url)
                gui.pokeimg_label['image'] = poke_img
                gui.pokeimg_label.image = poke_img

                # format abilities
                abilities = "Abilities:"
                for index in range(len(pokemon['abilities'])):
                    abilities += f"\n    {index + 1}) "
                    abilities += "{}".format(
                        pokemon['abilities'][index]['ability']['name'].title())
                gui.abilities_label['text'] = abilities


def main():
    """Main driver for the Pokedex."""
    PokeGUI()


if __name__ == "__main__":
    main()
