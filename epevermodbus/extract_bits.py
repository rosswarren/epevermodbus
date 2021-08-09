def extract_bits(data, start_bit, number_of_bits):
    mask = number_of_bits << start_bit
    result = data & mask
    shifted_result = result >> start_bit
    return shifted_result
