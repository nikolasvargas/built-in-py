#!/usr/bin/env python3.8
#-*- coding: utf-8 -*-
import timeit

from functools import wraps
from itertools import chain
from string import ascii_uppercase
from typing import Callable, Dict, List

def time_it(fn) -> Callable:
    class_name, function_name = fn.__qualname__.split('.')

    @wraps(fn)
    def wrapper(*args, **kwargs) -> Callable:
        start_time = timeit.default_timer()
        fn_callback = fn(*args, **kwargs)
        ellapsed_time = timeit.default_timer() - start_time
        print(f"{class_name = }")
        print(f"{function_name = }")
        print(f"{ellapsed_time = }")
        return fn_callback
    return wrapper


class StringSet:
    def __init__(self) -> None:
        self.words: Dict[str, List[str]] = {k: [] for k in ascii_uppercase}

    @time_it
    def add(self, word) -> None:
        key: str = word[0].upper()
        if word not in self.words[key]:
            self.words[key].append(word)

    def __repr__(self) -> List[str]:
        return str(list(chain.from_iterable(self.words.values())))

    def __contains__(self, item: str) -> bool:
        if not item:
            return False
        key: str = item[0].upper()
        return self.words[key].__contains__(item)

