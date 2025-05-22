from dataclasses import dataclass

@dataclass

class full_build:
    month:str = ""
    metal:str = ""
    jewelry:str = ""

    @property
    def options(self):
        return f"{self.month}{self.metal}{self.jewelry}"



def main ():
    build = full_build("September-Sapphire", "PLATINUM", "BRACELET")
    print = (f"You have selected: {full_build.self}")
    print = ("Bye")


if __name__ == "__main__":
    main()
