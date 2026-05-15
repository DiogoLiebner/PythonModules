from abc import ABC, abstractmethod
import typing


class Creature(ABC):
    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        pass


class CreatureFactory(ABC):
    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self, base: Creature) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:


    def create_evolved(self, base: Creature) -> Creature:


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:

    def create_evolved(self, base: Creature) -> Creature:


