# %%
import numpy as np

hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111',
}

with open('input.txt') as f:
    data = "".join([hex_to_bin[x] for x in list(f.read())])
data

versions = []
def parse_packets(packets: str):
    version, type, packets = packets[:3], packets[3:6], packets[6:]
    version = int(version, 2)
    type = int(type, 2)

    versions.append(version)
    remainder = ''

    if type == 4:
        n = 5
        packets = [packets[i:i+n] for i in range(0, len(packets), n)]
        literal_value = []
        while len(packets) > 0:
            new_packet = packets.pop(0)
            end, *bits = new_packet
            literal_value.append("".join(bits))
            if end == '0':
                break
        value = int("".join(literal_value), 2)
        packets = "".join(packets)
        
        if '1' in packets:
            remainder = packets
        return value, remainder

    else:
        length_type_id, *packets = packets
        if length_type_id == '0':
            length_bits, packets = packets[:15], packets[15:]
            length_bits = "".join(length_bits)
            length = int(length_bits, 2)
            my_packets = "".join(packets[:length])
            if len(packets) > length:
                other_packets = "".join(packets[length:])
                if '1' in other_packets:
                    remainder = other_packets
            subpackets = []
            while len(my_packets) > 0:
                subpacket, my_packets = parse_packets(my_packets)
                subpackets.append(subpacket)
            
        else:
            number_of_subpackets_bits, packets = packets[:11], packets[11:]
            remainder = "".join(packets)
            number_of_subpackets_bits = "".join(number_of_subpackets_bits)
            number_of_subpackets = int(number_of_subpackets_bits, 2)
            subpackets = []
            for _ in range(number_of_subpackets):
                subpacket, remainder = parse_packets(remainder)
                subpackets.append(subpacket)

        if (type == 0): # Sum
            value = sum(subpackets)
        elif (type == 1): # Product
            value = np.prod(subpackets)
        elif (type == 2): # Minimum
            value = min(subpackets)
        elif (type == 3): # Maximum
            value = max(subpackets)
        elif (type == 5): # l[0] > l[1]
            value = 1 if subpackets[0] > subpackets[1] else 0
        elif (type == 6): # l[0] < l[1]
            value = 1 if subpackets[0] < subpackets[1] else 0
        elif (type == 7): # l[0] == l[1]
            value = 1 if subpackets[0] == subpackets[1] else 0

        return value, remainder

result, _ = parse_packets(data)
print(f"Answer to part 1: {sum(versions)}")
print()
print(f"Answer to part 2: {result}")
# %%
