class Coder:
    @staticmethod
    def encode(message):
        buffer = ''
        for c in message:
            binnary = bin(ord(c))
            binarry_adjusted = binnary[2:].rjust(7, '0')
            buffer += binarry_adjusted + '0'
        return buffer

    @staticmethod
    def decode(bits):
        chunks, chunk_size = len(bits), 8
        bytes_array = [bits[i:i+chunk_size]
                       for i in range(0, chunks, chunk_size)]

        res = ''
        for byte in bytes_array:
            decimal = int(byte[:-1], 2)
            res += chr(decimal)
        return res
