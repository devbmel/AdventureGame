from typing import Dict, Tuple, List

import .data_fr as dfr
import .data_en as den


data_story: Tuple[Dict[str, str], Dict[str, str]] = (
    {
        "introduction": dfr.introduction_fr,
        "swamp": dfr.swamp_fr,
        "meadow": dfr.meadow_fr,
        "scorching_desert": dfr.scorching_desert_fr,
        "whispering_forest": dfr.whispering_forest_fr,
        "fight_sphinx": dfr.fight_spinx_fr,
        "caverns_of_oblivion": dfr.caverns_of_oblivion_fr,
        "feather": dfr.feather_fr,
        "maze": dfr.maze_fr,
        "wise_choice": dfr.wise_choice_fr,
        "wise_feather": dfr.wise_feather_fr,
        "stars_mountain": dfr.stars_mountain_fr,
        "celestial_guardian": dfr.celestial_guardian_fr,
        "fight_celestial_guardian": dfr.fight_celestial_guardian_fr,
        "celestial_guardian_riddle": dfr.celestial_guardian_riddle_fr,
        "story_third_cristal": dfr.story_third_cristal_fr,
        "ancients_ruin": dfr.ancients_ruin_fr,
        "ancients_ruin_fight": dfr.ancients_ruin_fight_fr,
        "ancients_ruin_ring": dfr.ancients_ruin_ring_fr,
        "story_fourth_cristal": dfr.story_fourth_cristal_fr,
        "light_temple": dfr.light_temple_fr,
        "fight_light_temple": dfr.fight_light_temple_fr,
        "clearing": dfr.clearing_fr,
        "dragon": dfr.dragon_fr,
        "story_fifth_cristal": dfr.story_fifth_cristal_fr,
        "dark_queen_castle": dfr.dark_queen_castle_fr,
        "epilogue": dfr.epilogue_fr         
    },
    {
        "introduction": "",
        "swamp": "",
        "meadow": "",
        "scorching_desert": "",
        "whispering_forest": "",
        "fight_sphinx": "",
        "cavern_of_oblivion": "",
        "feather": "",
        "maze": "",
        "wise": "",
        "stars_mountain": "",
        "celestial_guardian": "",
        "fight_celestial_guardian": "",
        "ancients_ruin": "",
        "light_temple": "",
        "clearing": "",
        "dark_queen_castle": "",
        "epilogue": ""
    }
)

parameters_user_choices: Dict[str, Tuple[str, List[str]]] = {
    "ask_language": (
        "Quel langage souhaitez vous utliser?",
        ["français", "anglais"]
    ),
   "ask_user_first_choice": (
        "Alaric prit un moment pour réfléchir, pesant les avantages et les inconvénients de chaque route. Quel chemin choisiriez-vous pour commencer cette aventure périlleuse ?",
        ["Les Marécages Nauséabonds : Un chemin difficile à travers des terres sombres et dangereuses, mais peut-être riche en récompenses cachées.",
         "La Prairie Tranquille : Un voyage sûr et apaisant à travers une nature paisible, idéal pour se préparer calmement à la suite.",
         "Le Désert Ardent : Une route ardue et éprouvante à travers un désert brûlant, promettant de révéler des secrets enfouis et des trésors inestimables."]
    ),
   "riddle_sphynx": (
        "Je suis toujours en mouvement, jamais immobile. Pourtant, sans moi, rien ne peut vivre. Qui suis-je ?",
        ["Le Vent", "Le Temps", "L'Eau"]
    ),

   
   
}
