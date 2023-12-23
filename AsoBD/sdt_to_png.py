import os

def conv(path, fn, xor):
    with open(f'pngs/{fn.replace(".sdt", "")}.png', "wb") as new:
        with open(path, "rb") as f:
            byte = f.read(1)
            while byte:
                num = int.from_bytes(byte, "big")

                num ^= xor
                num = num & 0xFF

                new.write(num.to_bytes(1, "big"))
                byte = f.read(1)


if __name__ == '__main__':
    print('script by howkudyou')
    while True:
        fn = input('Enter filename: ')
        if not os.path.exists(fn) or '.sdt' not in fn:
            continue
        conv(fn, 0x19)
