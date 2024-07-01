from Crypto.Util.number import long_to_bytes

def process_numbers(firstNumber, numbers):
    results = []
    for num in numbers:
        result = (firstNumber - num) / 2
        results.append(int(result))
        
    byte_strings = [long_to_bytes(res) for res in results]
    print(b''.join(byte_strings).decode('utf-8'))

if __name__ == "__main__":
    firstNumber = 2000128101369
    numbers = [
        991567152401, 
        1119812315025, 
        1148065938747, 
        1672423010575, 
        1068515887359
    ]
    process_numbers(firstNumber, numbers)