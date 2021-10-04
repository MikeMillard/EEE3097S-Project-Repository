import zlib, sys

rawFile = "2018-09-19-08_59_11_VN100.csv"
compressedFile = "compressed_data.csv"
decompressedFile = "decompressed_data.csv"

def myCompress (rawFile):
    with open(rawFile, mode="rb") as fin, open(compressedFile, mode="wb") as fout:
        data = fin.read()
        compressed_data = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
        print(f"Original size: {sys.getsizeof(data)}")
        # Original size: 1000033
        print(f"Compressed size: {sys.getsizeof(compressed_data)}")
        # Compressed size: 1024

        fout.write(compressed_data)

def myDecompress (compressedFile):
    with open(compressedFile, mode="rb") as fin, open(decompressedFile, mode="wb") as fout:
        data = fin.read()
        decompressed_data = zlib.decompress(data)
        print(f"Compressed size: {sys.getsizeof(data)}")
        # Compressed size: 1024
        print(f"Decompressed size: {sys.getsizeof(decompressed_data)}")
        # Decompressed size: 1000033

        fout.write(decompressed_data)