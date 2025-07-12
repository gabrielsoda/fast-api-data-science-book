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


from typing import Optional
def greeting(name: Optional[str] = None) -> str:
    return f"Hello, {name if name else 'Anonymous'}"



from typing import Tuple
IntStringFloatTuple = Tuple[int, str, float] 
t: IntStringFloatTuple = (1, "hello", 3.14)

#asignación de alias de typos complejos



#type function signatures with callable

from typing import Callable, List 
ConditionFunction = Callable[[int], bool]
def filter_list(l: List[int], condition: ConditionFunction) -> List[int]:
    return [i for i in l if condition(i)]


from typing import Any
def f(x: Any) -> Any: 
    return x

# cuando se complica el codigo podemos poner any para indicar al type checker, en mi caso pylance con pyright que está todo bien y cualquier typo es válido
