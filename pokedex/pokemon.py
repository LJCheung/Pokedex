"""This module implements the Pokemon, Stat, Ability and Move class."""
import textwrap


class Pokemon:
    """Represents a Pokemon."""

    def __init__(self, name: str, id_: int, height: int, weight: int,
                 stats: list, types: list, abilities: list,
                 moves: list):
        """
        Initializes the Pokemon with a group of attributes.
        :param name: a str
        :param id_: an int
        :param height: an int
        :param weight: an int
        :param stats: a list of dict objects {name, base value, url}
        :param types: a list
        :param abilities: a list of dict objects {name, url}
        :param moves: a list of dict objects {name, level learned, url}
        """
        self.name = name
        self.id_ = id_
        self.height = height  # decimetres
        self.weight = weight  # hectograms
        self.stats = stats
        self.types = types
        self.abilities = abilities
        self.moves = moves

    def format_stats(self, expanded=False, pokemon_stats=None) -> str:
        """
        Formats the information in the stats attribute for output.
        :param expanded: a bool
        :param pokemon_stats: a list of Stat objects
        :return: a string
        """
        stats = ""
        for index in range(len(self.stats)):
            stats += f"\n\t{index + 1}) "
            stats += ', '.join(
                ["{}".format(self.stats[index]['name']),
                 "Base Stat: {}".format(
                     self.stats[index]['base_stat'])])
            if expanded:
                stats += "\n{}".format(pokemon_stats[index])
        return stats

    def format_abilities(self, expanded=False,
                         pokemon_abilities=None) -> str:
        """
        Formats the information in the abilities attribute for output.
        :param expanded: a bool
        :param pokemon_abilities: a list of Abilities objects
        :return: a string
        """
        abilities = ""
        for index in range(len(self.abilities)):
            abilities += f"\n\t{index + 1}) "
            abilities += "{}".format(self.abilities[index]['name'])
            if expanded:
                abilities += "\n{}".format(
                    pokemon_abilities[index].expanded_str())
        return abilities

    def format_moves(self, expanded=False, pokemon_moves=None) -> str:
        """
        Formats the information in the moves attribute for output.
        :param expanded: a bool
        :param pokemon_moves: a list of Move objects
        :return: a string
        """
        moves = ""
        for index in range(len(self.moves)):
            moves += f"\n\t{index + 1}) "
            moves += ', '.join(
                ["{}".format(self.moves[index]['name']),
                 "Level Learned at: {}".format(
                     self.moves[index]['level_learned_at'])])
            if expanded:
                moves += \
                    "\n{}".format(pokemon_moves[index].expanded_str())
        return moves

    def expanded(self, pokemon_stats: list, pokemon_abilities: list,
                 pokemon_moves: list) -> str:
        """
        Return a readable string presentation of a Pokemon with
        expanded attributes.
        :param pokemon_stats: a list of Stat objects
        :param pokemon_abilities: a list of Ability objects
        :param pokemon_moves: a list of Move objects
        :return: a string
        """
        return f"Pokemon Name: {self.name}, Id: {self.id_}, Height: " \
               f"{self.height} decimetres, Weight: {self.weight} " \
               f"hectograms, Types: {', '.join(self.types)}\n" \
               f"Stats: {self.format_stats(True, pokemon_stats)}\n" \
               f"Abilities: " \
               f"{self.format_abilities(True, pokemon_abilities)}\n" \
               f"Moves: {self.format_moves(True, pokemon_moves)}"

    def __str__(self):
        """Return a readable string presentation of a Pokemon."""
        return f"Pokemon Name: {self.name}, Id: {self.id_}, Height: " \
               f"{self.height} decimetres, Weight: {self.weight} " \
               f"hectograms, Types: {', '.join(self.types)}\n" \
               f"Stats: {self.format_stats()}\n" \
               f"Abilities: {self.format_abilities()}\n" \
               f"Moves: {self.format_moves()}"


class Stat:
    """Represents a pokemon Stat."""

    def __init__(self, name: str, id_: int, is_battle_only: bool):
        """
        Initializes the Stat with the name, id and is_battle_only.
        :param name: a str
        :param id_: an int
        :param is_battle_only: a bool
        """
        self.name = name
        self.id_ = id_
        self.is_battle_only = is_battle_only

    def __str__(self):
        """Return a readable string presentation of a Stat."""
        return f"\t\tId: {self.id_}\n" \
               f"\t\tIs Battle Only: {self.is_battle_only}"


class Ability:
    """Represents a pokemon Ability."""

    def __init__(self, name: str, id_: int, generation: str,
                 effect: str, short_effect: str, pokemon: list):
        """
        Initializes the Ability with a group of attributes.
        :param name: a str
        :param id_: an int
        :param generation: a str
        :param effect: a str
        :param short_effect: a str
        :param pokemon: a list
        """
        self.name = name
        self.id_ = id_
        self.generation = generation
        self.effect = effect
        self.short_effect = short_effect
        self.pokemon = pokemon

    def expanded_str(self) -> str:
        """
        Return a readable string presentation of an Ability for a
        Pokemon query on expanded mode.
        :return: a string
        """
        wrapper = textwrap.TextWrapper(width=100,
                                       subsequent_indent='\t\t')

        return f"\t\tId: {self.id_}\n" \
               f"\t\tGeneration: {self.generation}\n" \
               f"\t\tEffect: {wrapper.fill(self.effect)}\n\n" \
               f"\t\tEffect (short): " \
               f"{wrapper.fill(self.short_effect)}\n\n" \
               f"\t\tPokemon: {wrapper.fill(', '.join(self.pokemon))}"

    def __str__(self):
        """Return a readable string presentation of an Ability."""
        return f"Ability Name: {self.name}\n" \
               f"Id: {self.id_}\n" \
               f"Generation: {self.generation}\n" \
               f"Effect: {self.effect}\n\n" \
               f"Effect (short): {self.short_effect}\n\n" \
               f"Pokemon: {', '.join(self.pokemon)}"


class Move:
    """Represents a pokemon Move."""

    def __init__(self, name: str, id_: int, generation: str,
                 accuracy: int, pp: int, power: int, type_: str,
                 damage_class: str, short_effect: str):
        """
        Initializes a Move with a group of attributes.
        :param name: a str
        :param id_: an int
        :param generation: a str
        :param accuracy: an int
        :param pp: an int
        :param power: an int
        :param type_: a str
        :param damage_class: a str
        :param short_effect: a str
        """
        self.name = name
        self.id_ = id_
        self.generation = generation
        self.accuracy = accuracy
        self.pp = pp
        self.power = power
        self.type_ = type_
        self.damage_class = damage_class
        self.short_effect = short_effect

    def expanded_str(self) -> str:
        """
        Return a readable string presentation of a pokemon Move for a
        Pokemon query on expanded mode.
        :return: a string
        """
        return f"\t\tId: {self.id_}\n" \
               f"\t\tGeneration: {self.generation}\n" \
               f"\t\tAccuracy: {self.accuracy}\n" \
               f"\t\tPP: {self.pp}\n" \
               f"\t\tPower: {self.power}\n" \
               f"\t\tType: {self.type_}\n" \
               f"\t\tDamage Class: {self.damage_class}\n" \
               f"\t\tEffect (Short): {self.short_effect}"

    def __str__(self):
        """Return a readable string presentation of a pokemon Move."""
        return f"Move Name: {self.name}\n" \
               f"Id: {self.id_}\n" \
               f"Generation: {self.generation}\n" \
               f"Accuracy: {self.accuracy}\n" \
               f"PP: {self.pp}\n" \
               f"Power: {self.power}\n" \
               f"Type: {self.type_}\n" \
               f"Damage Class: {self.damage_class}\n" \
               f"Effect (Short): {self.short_effect}"
