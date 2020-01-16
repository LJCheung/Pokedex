"""
This module implements the PokedexMode Enum and the Request,
FileHandler and CommandlineInterface classes.
"""
import argparse
import enum
import os
import pathlib


class PokedexMode(enum.Enum):
    """
    Lists the various modes that the Pokedex application can run in.
    """
    POKEMON = "pokemon"
    ABILITY = "ability"
    MOVE = "move"


class Request:
    """Represents a Request received from user input in the terminal."""

    def __init__(self):
        """
        Initializes the Request.
        """
        self.mode = None  # Pokemon, ability, move
        self.input_mode = None  # File or name/id
        self.expanded = False
        self.output = None  # A .txt file
        self.queries = []
        self.results = ""

    def __str__(self):
        """Returns a string representation of a Request."""
        return f"Request: Mode: {self.mode.value}, Input: " \
               f"{self.input_mode} Expanded: {self.expanded}, " \
               f"Output: {self.output}"


class FileHandler:
    """Represents a file handler to read and write to a file."""

    def validate_input(self, req: Request):
        """
        Checks the provided path of a Request.
        :param req: a Request
        :return: None
        """
        filename, file_extension = os.path.splitext(req.input_mode)
        if "." in file_extension and file_extension != ".txt":
            raise Exception("Error - File must be of type .txt")

        elif file_extension == ".txt":

            # Check if file exists
            file = pathlib.Path(req.input_mode)
            if file.exists() is False and req.input_mode is None:
                raise Exception(f"File '{file}' does not exist. "
                                f"Please provide an existing file to "
                                f"process, else provide a pokemon name "
                                f"(string) or id (int) as the input.")

            # Check if file is empty
            if os.path.getsize(req.input_mode) == 0:
                raise Exception("Error - File is empty.")

            self.read_file(req)

        elif "." not in req.input_mode:
            req.queries.append(req.input_mode)

    def read_file(self, req: Request):
        """
        Reads the file provided from a Request as queries to make
        in the Pokedex.
        :param req: a Request
        :return: None
        """
        if len(req.queries) == 0:
            with open(req.input_mode, mode='r') as file:
                req.queries = [line.strip().lower() for line in file]

    def write_file(self, req: Request):
        """
        Writes the results of querying the Pokedex to the provided
        output path if provided.
        :param req: a Request
        :return: None
        """
        if not req.output.endswith(".txt"):
            print("The output file should be a .txt file. The results "
                  "will be printed to the console instead.")
        else:
            with open(req.output, mode='w') as output_file:
                output_file.write(req.results)


class CommandlineInterface:
    """
    Implements the argparse module to accept arguments via the command
    line.
    """

    @classmethod
    def run(cls) -> Request:
        """
        This function specifies what these arguments are and parses it
        into an object of type Request. If something goes wrong with
        provided arguments then the function prints an error message and
        exits the application.
        :return: a Request
        """
        parser = argparse.ArgumentParser()
        parser.add_argument("mode",
                            help="The mode to run the program in. If "
                                 "'pokemon', then the program will "
                                 "query pokemon information. If "
                                 "'ability', then the program will "
                                 "query ability information. If 'move',"
                                 " then the program will query move "
                                 "information.",
                            choices=["pokemon", "ability", "move"],
                            type=str.lower)
        parser.add_argument("input",
                            help="The input provided to the program. "
                                 "If a file name of .txt extension is "
                                 "provided, the program will read the "
                                 "file line by line and execute a bulk "
                                 "query. If a name (a string) or id "
                                 "(a digit) is provided, then the "
                                 "program will run a single query.",
                            type=str.lower)
        parser.add_argument("-e", "--expanded",
                            help="If this flag is provided, the "
                                 "program will expand on the "
                                 "information of certain attributes."
                                 "Please note only Pokemon queries"
                                 "support the expanded mode.",
                            action="store_true")
        parser.add_argument("-o", "--output", default="print",
                            help="The output of the program. This is "
                                 "'print' by default, but can be set to"
                                 " a file name of .txt extension as "
                                 "well.")
        try:
            args = parser.parse_args()
            request = Request()
            request.mode = PokedexMode(args.mode)
            request.input_mode = args.input
            request.expanded = args.expanded
            request.output = args.output

            print(request)
            return request
        except Exception as e:
            print(f"Error! Could not read arguments.\n{e}")
            quit()
