from scripts.filter import main as filter_main
from scripts.clean import main as clean_main
from scripts.normalise import main as normalise_main
from scripts.seed import main as seed_main

def main():
    filter_main()
    clean_main()
    normalise_main()
    seed_main()

if __name__ == "__main__":
    main()