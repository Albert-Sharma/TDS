import requests

def get_moves(pokemon, version):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon}"
    response = requests.get(url)
    data = response.json()

    moves = set()
    for move in data['moves']:
        for version_detail in move['version_group_details']:
            if version_detail['version_group']['name'] == version:
                moves.add(move['move']['name'])
                break

    return moves

def main(version, pokemonA, pokemonB):
    pokemonA_moves = get_moves(pokemonA, version)
    pokemonB_moves = get_moves(pokemonB, version)

    unique_pokemonA_moves = pokemonA_moves - pokemonB_moves
    
    newline = "\n\t"

    print(f"\nNumber of moves Ekans has that Growlithe does not in the '{version}' version is : {len(unique_pokemonA_moves)}")
    print(f"\nMoves: {newline.join( f'{i}' for i in unique_pokemonA_moves)}")

if __name__ == "__main__":
    version, pokemonA, pokemonB = input("Enter Version : "), input("Name ofthe first Pokemon : "), input("Name of the second Pokemon : ")
    main(version, pokemonA, pokemonB)



