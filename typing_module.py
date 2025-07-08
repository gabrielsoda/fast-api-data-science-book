#A partir de 3.9 no es neceario typing
#antes se tenía que exportar así
# from typing import Dict, List, Set, Tuple
# además tener en cuenta que los tipos de datos
# deben empezar con mayúsculas
l: list[int] = [1, 2, 3, 4, 5]
t: tuple[int, str, float] = (1, "hello", 3.14) 
s: set[int] = {1, 2, 3, 4, 5}
d: dict[str, int] = {"a": 1, "b": 2, "c": 3}

from typing import List, Union
lu : List[Union[int, float]] = [1, 2.5, 3.14, 5]



 