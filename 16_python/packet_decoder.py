from dataclasses import dataclass
from enum import Enum
from typing import Iterable, Iterator, TypeVar
from itertools import islice
from pathlib import Path


@dataclass
class Packet:
    version: int
    type_id: int


@dataclass
class LiteralPacket(Packet):
    values: list[int]

class PacketType(Enum):
    LITERAL = 4
    OPERATOR = 6

@dataclass
class OperatorPacket:
    length_type_id: int

T = TypeVar("T")


def sub_lists(lst: Iterable[T], n: int) -> Iterator[Iterable[T]]:
    """yields sublist of given max length"""
    for i in range(0, len(lst), n):
        yield lst[i : i + n]


def take(iterable: Iterable, n: int):
    return list(next(iterable) for _ in range(n))


def hex_to_bin(hex_packet: str) -> str:
    return f"{int(hex_packet, 16):0>b}"


def packetize(binary_packet: str) -> Iterator[Packet]:

    while iter(binary_packet):
        version = int(binary_packet[:3], 2)
        type_id = int(binary_packet[3:6], 2)

        match type_id:
            case PacketType.LITERAL:
                values = []
                for i, value in enumerate(sub_lists(binary_packet[6:], 5)):
                    values.append(int(value[1:], 2))
                    if value.startswith("0"):
                        break
            case PacketType.OPERATOR:
                length_type_id = int(binary_packet[6:9], 2)

        length = 6 + 5 * (i + 1)
        packet_end = length + 4 - length % 4
        current_packet = binary_packet[:packet_end]
        binary_packet = binary_packet[packet_end:]

        yield Packet(version, type_id, values)


def main() -> None:
    with Path(__file__).with_name("input.txt").open(encoding="utf-8") as f:
        hex_packet = f.read()

    binary_packet = hex_to_bin(hex_packet)
    for packet in packetize(binary_packet):
        print(packet)


if __name__ == "__main__":
    main()
